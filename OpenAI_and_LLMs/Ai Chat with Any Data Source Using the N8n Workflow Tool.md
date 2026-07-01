```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    On_new_manual_Chat_Message(("fas:fa-robot On new manual Chat Message")):::trigger
    Execute_Workflow_Trigger(("fas:fa-bolt Execute Workflow Trigger")):::trigger
    Hacker_News["fas:fa-cogs Hacker News"]
    Clean_up_data["fas:fa-cogs Clean up data"]
    AI_Agent["fas:fa-robot AI Agent"]:::ai
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Stringify["fas:fa-cogs Stringify"]
    Custom_tool_to_call_the_wf_below["fas:fa-robot Custom tool to call the wf below"]

    Hacker_News --> Clean_up_data
    Clean_up_data --> Stringify
    OpenAI_Chat_Model --> AI_Agent
    Execute_Workflow_Trigger --> Hacker_News
    On_new_manual_Chat_Message --> AI_Agent
    Custom_tool_to_call_the_wf_below --> AI_Agent
```
