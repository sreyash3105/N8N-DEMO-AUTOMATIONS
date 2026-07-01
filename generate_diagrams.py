import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def clean_node_id(name: str) -> str:
    """Converts a node name into a safe, valid Mermaid ID."""
    safe_id = re.sub(r'[^a-zA-Z0-9]', '_', name)
    if not safe_id or safe_id[0].isdigit():
        safe_id = "n_" + safe_id
    return safe_id

def determine_shape(node_type: str) -> tuple:
    """Returns the left and right brackets for Mermaid based on node type."""
    node_type = node_type.lower()
    if "trigger" in node_type or "webhook" in node_type or "schedule" in node_type:
        return ("((", "))")  # Circle/oval for triggers
    elif "switch" in node_type or "if" in node_type or "router" in node_type:
        return ("{", "}")    # Diamond for logic/conditions
    elif "model" in node_type or "llm" in node_type or "openai" in node_type:
        return ("([", "])")  # Stadium for AI models
    elif "memory" in node_type or "database" in node_type:
        return ("[(", ")]")  # Cylinder for data/memory
    else:
        return ("[", "]")    # Rectangle for standard actions

def determine_icon(node_type: str, name: str) -> str:
    """Returns a native FontAwesome icon string for the node."""
    t = node_type.lower()
    n = name.lower()
    
    if "telegram" in t or "telegram" in n: return "fab:fa-telegram "
    if "whatsapp" in t or "whatsapp" in n: return "fab:fa-whatsapp "
    if "slack" in t or "slack" in n: return "fab:fa-slack "
    if "gmail" in t or "email" in t or "gmail" in n: return "fas:fa-envelope "
    if "google" in t or "google" in n: return "fab:fa-google "
    if "wordpress" in t or "wordpress" in n: return "fab:fa-wordpress "
    if "database" in t or "postgres" in t or "supabase" in t: return "fas:fa-database "
    if "pdf" in t or "pdf" in n: return "fas:fa-file-pdf "
    if "llm" in t or "openai" in t or "ai" in t or "agent" in n: return "fas:fa-robot "
    if "trigger" in t or "webhook" in t: return "fas:fa-bolt "
    if "switch" in t or "if" in t or "router" in t: return "fas:fa-code-branch "
    if "schedule" in t or "cron" in t: return "fas:fa-clock "
    if "http" in t or "request" in t: return "fas:fa-globe "
    
    # Default icon if none match
    return "fas:fa-cogs "

def parse_n8n_json(filepath: Path):
    """Safely loads n8n JSON, handling both full workflow objects and node arrays."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
    
    # Handle files with "Extra data" (often happens if multiple JSON objects are in the file, 
    # or if there's trailing garbage, we can try to find the first valid object)
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        # Fallback: try to extract just the main JSON object if there's trailing junk
        match = re.search(r'(\{.*\})', content, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(1))
            except Exception:
                return None
        else:
            return None

    # Handle if the export was just an array of nodes instead of a full workflow
    if isinstance(data, list):
        return {"nodes": data, "connections": {}}
    return data

def generate_mermaid_for_workflow(filepath: Path) -> bool:
    data = parse_n8n_json(filepath)
    if not data:
        print(f"⚠️ Could not parse JSON in {filepath.name}")
        return False

    nodes = data.get("nodes", [])
    connections = data.get("connections", {})

    if not nodes:
        return False

    mermaid_lines = [
        "```mermaid", 
        "graph TD",
        "    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;",
        "    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;",
        "    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;",
        ""
    ]

    # 1. Filter out Sticky Notes and map the rest
    node_map = {}
    for node in nodes:
        name = node.get("name", "Unknown")
        node_type = node.get("type", "")
        
        # SKIP Sticky Notes - they clutter the diagram!
        if "stickyNote" in node_type:
            continue
            
        safe_id = clean_node_id(name)
        node_map[name] = {"id": safe_id, "type": node_type}
        
        left, right = determine_shape(node_type)
        safe_name = name.replace('"', "'")
        icon = determine_icon(node_type, name)
        
        line = f'    {safe_id}{left}"{icon}{safe_name}"{right}'
        
        # Apply CSS classes based on type to make it pretty
        t = node_type.lower()
        if "trigger" in t or "webhook" in t:
            line += ":::trigger"
        elif "llm" in t or "model" in t or "openai" in t or "agent" in t:
            line += ":::ai"
        elif "if" in t or "switch" in t:
            line += ":::logic"
            
        mermaid_lines.append(line)

    mermaid_lines.append("")

    # 2. Define all connections
    connection_count = 0
    for source_name, outputs in connections.items():
        source_info = node_map.get(source_name)
        if not source_info:
            continue

        for output_type, output_arrays in outputs.items():
            for target_list in output_arrays:
                if not target_list:
                    continue
                if isinstance(target_list, list):
                    for target_obj in target_list:
                        target_name = target_obj.get("node")
                        if target_name in node_map:
                            mermaid_lines.append(f"    {source_info['id']} --> {node_map[target_name]['id']}")
                            connection_count += 1
                elif isinstance(target_list, dict):
                    target_name = target_list.get("node")
                    if target_name in node_map:
                        mermaid_lines.append(f"    {source_info['id']} --> {node_map[target_name]['id']}")
                        connection_count += 1

    mermaid_lines.append("```\n")

    # Don't create markdown for empty/useless diagrams
    if len(node_map) == 0 or (connection_count == 0 and len(node_map) > 3):
        return False

    out_file = filepath.with_suffix('.md')
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(mermaid_lines))
    
    return True

def main():
    print("🧹 Cleaning up old diagram files...")
    deleted = 0
    for md_file in BASE_DIR.rglob("*.md"):
        # Only delete .md files that have a corresponding .json file (keeps READMEs safe)
        if md_file.with_suffix('.json').exists():
            md_file.unlink()
            deleted += 1
    print(f"🗑️  Deleted {deleted} old diagrams.\n")

    print("🎨 Generating clean Mermaid diagrams from workflows...\n")

    json_files = list(BASE_DIR.rglob("*.json"))
    json_files = [f for f in json_files if "node_modules" not in str(f) and not f.name.endswith("package.json")]

    success_count = 0
    for filepath in json_files:
        if generate_mermaid_for_workflow(filepath):
            success_count += 1

    print(f"✅ Generated {success_count} Beautiful Mermaid markdown files!")

if __name__ == "__main__":
    main()
