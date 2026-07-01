```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    stats_aggregate_creators["stats_aggregate_creators"]
    stats_aggregate_workflows["stats_aggregate_workflows"]
    Global_Variables["Global Variables"]
    Parse_Workflow_Data["Parse Workflow Data"]
    Parse_Creators_Data["Parse Creators Data"]
    Aggregate["Aggregate"]
    gpt_4o_mini(["gpt-4o-mini"]):::ai
    When_Executed_by_Another_Workflow(("When Executed by Another Workflow")):::trigger
    Workflow_Tool["Workflow Tool"]
    creator_summary["creator-summary"]
    Workflow_Response["Workflow Response"]
    Save_creator_summary_md["Save creator-summary.md"]
    Creators_Data["Creators Data"]
    Workflows_Data["Workflows Data"]
    Merge_Creators___Workflows["Merge Creators & Workflows"]
    Split_Out_Creators["Split Out Creators"]
    Split_Out_Workflows["Split Out Workflows"]
    Sort_By_Top_Weekly_Creator_Inserts["Sort By Top Weekly Creator Inserts"]
    Sort_By_Top_Weekly_Workflow_Inserts["Sort By Top Weekly Workflow Inserts"]
    Schedule_Trigger(("Schedule Trigger")):::trigger
    Take_Top_10_Creators["Take Top 10 Creators"]
    Take_Top_50_Workflows["Take Top 50 Workflows"]
    Google_Drive["Google Drive"]
    Convert_Markdown_to_HTML["Convert Markdown to HTML"]
    n8n_Creators_Stats_Agent["n8n Creators Stats Agent"]:::ai
    Google_Gemini_Chat_Model["Google Gemini Chat Model"]
    Create_Top_10_Workflows_List(["Create Top 10 Workflows List"]):::ai
    Convert_Top_10_Markdown_to_HTML["Convert Top 10 Markdown to HTML"]
    Gmail_Creators___Workflows_Report["Gmail Creators & Workflows Report"]
    Telegram_Top_10_Workflows_List["Telegram Top 10 Workflows List"]
    Gmail_Top_10_Workflows_List["Gmail Top 10 Workflows List"]

    Aggregate --> Workflow_Response
    gpt_4o_mini --> n8n_Creators_Stats_Agent
    Creators_Data --> Merge_Creators___Workflows
    Workflow_Tool --> n8n_Creators_Stats_Agent
    Workflows_Data --> Merge_Creators___Workflows
    creator_summary --> Save_creator_summary_md
    Global_Variables --> stats_aggregate_creators
    Global_Variables --> stats_aggregate_workflows
    Schedule_Trigger --> n8n_Creators_Stats_Agent
    Split_Out_Creators --> Sort_By_Top_Weekly_Creator_Inserts
    Parse_Creators_Data --> Split_Out_Creators
    Parse_Workflow_Data --> Split_Out_Workflows
    Split_Out_Workflows --> Sort_By_Top_Weekly_Workflow_Inserts
    Take_Top_10_Creators --> Creators_Data
    Take_Top_50_Workflows --> Workflows_Data
    Convert_Markdown_to_HTML --> Gmail_Creators___Workflows_Report
    Google_Gemini_Chat_Model --> Create_Top_10_Workflows_List
    n8n_Creators_Stats_Agent --> creator_summary
    n8n_Creators_Stats_Agent --> Google_Drive
    n8n_Creators_Stats_Agent --> Convert_Markdown_to_HTML
    n8n_Creators_Stats_Agent --> Create_Top_10_Workflows_List
    stats_aggregate_creators --> Parse_Creators_Data
    stats_aggregate_workflows --> Parse_Workflow_Data
    Merge_Creators___Workflows --> Aggregate
    Create_Top_10_Workflows_List --> Convert_Top_10_Markdown_to_HTML
    Create_Top_10_Workflows_List --> Telegram_Top_10_Workflows_List
    Convert_Top_10_Markdown_to_HTML --> Gmail_Top_10_Workflows_List
    When_Executed_by_Another_Workflow --> Global_Variables
    Sort_By_Top_Weekly_Creator_Inserts --> Take_Top_10_Creators
    Sort_By_Top_Weekly_Workflow_Inserts --> Take_Top_50_Workflows
```
