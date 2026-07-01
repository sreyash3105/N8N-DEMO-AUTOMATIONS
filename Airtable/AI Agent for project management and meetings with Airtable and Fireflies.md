```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    AI_Agent["AI Agent"]:::ai
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    Create_Tasks["Create Tasks"]
    Notify_Client_About_Tasks["Notify Client About Tasks"]
    Execute_Workflow_Trigger(("Execute Workflow Trigger")):::trigger
    Split_Out["Split Out"]
    Create_Task["Create Task"]
    Create_Event["Create Event"]
    Webhook(("Webhook")):::trigger
    Get_Meeting_Content["Get Meeting Content"]

    Webhook --> Get_Meeting_Content
    Split_Out --> Create_Task
    Create_Event --> AI_Agent
    Create_Tasks --> AI_Agent
    OpenAI_Chat_Model --> AI_Agent
    Get_Meeting_Content --> AI_Agent
    Execute_Workflow_Trigger --> Split_Out
    Notify_Client_About_Tasks --> AI_Agent
```
