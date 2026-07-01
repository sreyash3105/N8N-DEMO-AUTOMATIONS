```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    stats_aggregate_creators["fas:fa-globe stats_aggregate_creators"]
    stats_aggregate_workflows["fas:fa-globe stats_aggregate_workflows"]
    Global_Variables["fas:fa-cogs Global Variables"]
    Parse_Workflow_Data["fas:fa-cogs Parse Workflow Data"]
    Parse_Creators_Data["fas:fa-cogs Parse Creators Data"]
    Take_Top_25_Creators["fas:fa-cogs Take Top 25 Creators"]
    Aggregate["fas:fa-cogs Aggregate"]
    Filter_By_Creator_Username["fas:fa-cogs Filter By Creator Username"]
    gpt_4o_mini(["fas:fa-robot gpt-4o-mini"]):::ai
    When_Executed_by_Another_Workflow(("fas:fa-bolt When Executed by Another Workflow")):::trigger
    When_chat_message_received(("fas:fa-robot When chat message received")):::trigger
    Workflow_Tool["fas:fa-robot Workflow Tool"]
    creator_summary["fas:fa-cogs creator-summary"]
    Workflow_Response["fas:fa-cogs Workflow Response"]
    n8n_Creator_Stats_Agent["fas:fa-robot n8n Creator Stats Agent"]:::ai
    Save_creator_summary_md["fas:fa-cogs Save creator-summary.md"]
    Summary_Report["fas:fa-cogs Summary Report"]
    Ollama_Chat_Model["fas:fa-robot Ollama Chat Model"]
    Creators_Data["fas:fa-cogs Creators Data"]
    Workflows_Data["fas:fa-cogs Workflows Data"]
    Merge_Creators___Workflows["fas:fa-cogs Merge Creators & Workflows"]
    Split_Out_Creators["fas:fa-cogs Split Out Creators"]
    Split_Out_Workflows["fas:fa-cogs Split Out Workflows"]
    Sort_By_Top_Weekly_Creator_Inserts["fas:fa-cogs Sort By Top Weekly Creator Inserts"]
    Sort_By_Top_Weekly_Workflow_Inserts["fas:fa-cogs Sort By Top Weekly Workflow Inserts"]
    Take_Top_300_Workflows["fas:fa-cogs Take Top 300 Workflows"]
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]

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
