"""
N8N Workflow Bulk Cleanup Script
=================================
A generic sanitization utility for n8n workflow JSON files.
Run this script before committing or sharing workflows to ensure 
sensitive or instance-specific data is not leaked.

Default Behaviors:
  1. Strips `instanceId` from all meta blocks  →  ""
  2. Scrubs literal phone numbers in `recipientPhoneNumber` →  YOUR_RECIPIENT_PHONE_NUMBER
     (Ignores dynamic n8n expressions like `={{ $json.phone }}`)

Customizable Behaviors (Edit the lists below):
  - Replace specific `phoneNumberId` values
  - Clean up specific custom placeholders (e.g. API keys, cookies)

Usage:
  python cleanup_workflows.py
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# ── Configuration ─────────────────────────────────────────────────────────────

# Add any specific WhatsApp Business phone number IDs you want to sanitize here.
# E.g. ["123456789012345", "987654321098765"]
PHONE_NUMBER_IDS = []
PHONE_NUMBER_ID_PLACEHOLDER = "YOUR_WHATSAPP_PHONE_NUMBER_ID"

# Add any specific text values (like old placeholders or accidental leaked keys) 
# that you want to scrub across all Set node assignments.
# Format: {"Text to find": "Text to replace with"}
CUSTOM_TEXT_REPLACEMENTS = {
    "<COPY_YOUR_LINKEDIN_COOKIES_HERE>": "YOUR_LINKEDIN_COOKIE_HERE"
}

# Regex: matches any literal phone number (digits only, no {{ expression }})
# Ignores dynamic n8n expressions like ={{ $json.phone }}
HARDCODED_PHONE_REGEX = re.compile(r"^\+?[\d\s\-()]{7,20}$")
RECIPIENT_PLACEHOLDER = "YOUR_RECIPIENT_PHONE_NUMBER"

# ── Stats ─────────────────────────────────────────────────────────────────────
stats = {
    "files_scanned": 0,
    "files_modified": 0,
    "instanceId_stripped": 0,
    "recipientPhone_fixed": 0,
    "phoneNumberId_fixed": 0,
    "custom_text_replaced": 0,
}

changes_log = []

# ── Node-level fixes ──────────────────────────────────────────────────────────

def fix_node(node: dict, filename: str) -> bool:
    """Sanitize a single workflow node. Returns True if anything changed."""
    changed = False
    params = node.get("parameters", {})

    # 1. Fix hardcoded phoneNumberId
    if "phoneNumberId" in params:
        if params["phoneNumberId"] in PHONE_NUMBER_IDS:
            old = params["phoneNumberId"]
            params["phoneNumberId"] = PHONE_NUMBER_ID_PLACEHOLDER
            stats["phoneNumberId_fixed"] += 1
            changes_log.append(f"  [{filename}] phoneNumberId: {old} → {PHONE_NUMBER_ID_PLACEHOLDER}")
            changed = True

    # 2. Fix any literal hardcoded recipientPhoneNumber (not an expression)
    if "recipientPhoneNumber" in params:
        val = str(params["recipientPhoneNumber"])
        is_expression = val.strip().startswith("=")
        if not is_expression and HARDCODED_PHONE_REGEX.match(val.strip()):
            params["recipientPhoneNumber"] = RECIPIENT_PLACEHOLDER
            stats["recipientPhone_fixed"] += 1
            changes_log.append(f"  [{filename}] recipientPhoneNumber: {val!r} → {RECIPIENT_PLACEHOLDER}")
            changed = True

    # 3. Process custom text replacements in assignments (Set nodes)
    assignments = params.get("assignments", {}).get("assignments", [])
    for assignment in assignments:
        current_val = assignment.get("value")
        if current_val in CUSTOM_TEXT_REPLACEMENTS:
            replacement = CUSTOM_TEXT_REPLACEMENTS[current_val]
            assignment["value"] = replacement
            stats["custom_text_replaced"] += 1
            changes_log.append(f"  [{filename}] Replaced custom text: {current_val} → {replacement}")
            changed = True

    return changed


# ── File-level processing ─────────────────────────────────────────────────────

def process_file(filepath: Path) -> bool:
    """Process a single JSON workflow file. Returns True if the file was modified."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"  ⚠️  Skipping (parse error): {filepath.name} — {e}")
        return False

    changed = False
    filename = filepath.name

    # Strip instanceId from meta block
    if "meta" in data and "instanceId" in data["meta"]:
        old_id = data["meta"]["instanceId"]
        if old_id:
            data["meta"]["instanceId"] = ""
            stats["instanceId_stripped"] += 1
            changes_log.append(f"  [{filename}] instanceId stripped: {old_id[:16]}...")
            changed = True

    # Fix all nodes
    for node in data.get("nodes", []):
        if fix_node(node, filename):
            changed = True

    # Write back only if something changed
    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        stats["files_modified"] += 1

    return changed


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    print("🔍 Scanning N8N workflow files...\n")

    json_files = list(BASE_DIR.rglob("*.json"))
    json_files = [
        f for f in json_files
        if "node_modules" not in str(f)
        and f.name != "package.json"
        and f.name != "package-lock.json"
    ]

    for filepath in sorted(json_files):
        stats["files_scanned"] += 1
        process_file(filepath)

    # Report
    print("=" * 60)
    print("✅ CLEANUP COMPLETE\n")
    print(f"  Files scanned:           {stats['files_scanned']}")
    print(f"  Files modified:          {stats['files_modified']}")
    print(f"  instanceId stripped:     {stats['instanceId_stripped']}")
    print(f"  recipientPhone fixed:    {stats['recipientPhone_fixed']}")
    print(f"  phoneNumberId fixed:     {stats['phoneNumberId_fixed']}")
    print(f"  Custom text replaced:    {stats['custom_text_replaced']}")

    if changes_log:
        print("\n📋 Changes made:")
        for line in changes_log:
            print(line)
    else:
        print("\nNo changes needed — everything is already clean!")

    print("=" * 60)


if __name__ == "__main__":
    main()
