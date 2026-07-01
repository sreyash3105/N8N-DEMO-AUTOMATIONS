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
    Take_Top_25_Creators["Take Top 25 Creators"]
    Aggregate["Aggregate"]
    Filter_By_Creator_Username["Filter By Creator Username"]
    gpt_4o_mini(["gpt-4o-mini"]):::ai
    When_Executed_by_Another_Workflow(("When Executed by Another Workflow")):::trigger
    When_chat_message_received(("When chat message received")):::trigger
    Workflow_Tool["Workflow Tool"]
    creator_summary["creator-summary"]
    Workflow_Response["Workflow Response"]
    n8n_Creator_Stats_Agent["n8n Creator Stats Agent"]:::ai
    Save_creator_summary_md["Save creator-summary.md"]
    Summary_Report["Summary Report"]
    Ollama_Chat_Model["Ollama Chat Model"]
    Creators_Data["Creators Data"]
    Workflows_Data["Workflows Data"]
    Merge_Creators___Workflows["Merge Creators & Workflows"]
    Split_Out_Creators["Split Out Creators"]
    Split_Out_Workflows["Split Out Workflows"]
    Sort_By_Top_Weekly_Creator_Inserts["Sort By Top Weekly Creator Inserts"]
    Sort_By_Top_Weekly_Workflow_Inserts["Sort By Top Weekly Workflow Inserts"]
    Take_Top_300_Workflows["Take Top 300 Workflows"]
    Window_Buffer_Memory[("Window Buffer Memory")]

    Aggregate --> Workflow_Response
    gpt_4o_mini --> n8n_Creator_Stats_Agent
    Creators_Data --> Merge_Creators___Workflows
    Workflow_Tool --> n8n_Creator_Stats_Agent
    Workflows_Data --> Merge_Creators___Workflows
    creator_summary --> Save_creator_summary_md
    Global_Variables --> stats_aggregate_creators
    Global_Variables --> stats_aggregate_workflows
    Split_Out_Creators --> Sort_By_Top_Weekly_Creator_Inserts
    Parse_Creators_Data --> Split_Out_Creators
    Parse_Workflow_Data --> Split_Out_Workflows
    Split_Out_Workflows --> Sort_By_Top_Weekly_Workflow_Inserts
    Take_Top_25_Creators --> Creators_Data
    Window_Buffer_Memory --> n8n_Creator_Stats_Agent
    Take_Top_300_Workflows --> Workflows_Data
    n8n_Creator_Stats_Agent --> Summary_Report
    n8n_Creator_Stats_Agent --> creator_summary
    stats_aggregate_creators --> Parse_Creators_Data
    stats_aggregate_workflows --> Parse_Workflow_Data
    Filter_By_Creator_Username --> Aggregate
    Merge_Creators___Workflows --> Filter_By_Creator_Username
    When_chat_message_received --> n8n_Creator_Stats_Agent
    When_Executed_by_Another_Workflow --> Global_Variables
    Sort_By_Top_Weekly_Creator_Inserts --> Take_Top_25_Creators
    Sort_By_Top_Weekly_Workflow_Inserts --> Take_Top_300_Workflows
```
