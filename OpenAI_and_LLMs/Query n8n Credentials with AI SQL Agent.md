```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking 'Test workflow'")):::trigger
    Map_Workflows___Credentials["fas:fa-cogs Map Workflows & Credentials"]
    Save_to_Database["fas:fa-cogs Save to Database"]
    Chat_Trigger(("fas:fa-robot Chat Trigger")):::trigger
    Query_Workflow_Credentials_Database["fas:fa-robot Query Workflow Credentials Database"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    Workflow_Credentials_Helper_Agent["fas:fa-robot Workflow Credentials Helper Agent"]:::ai
    n8n["fas:fa-cogs n8n"]

    n8n --> Map_Workflows___Credentials
    Chat_Trigger --> Workflow_Credentials_Helper_Agent
    OpenAI_Chat_Model --> Workflow_Credentials_Helper_Agent
    Window_Buffer_Memory --> Workflow_Credentials_Helper_Agent
    Map_Workflows___Credentials --> Save_to_Database
    When_clicking__Test_workflow_ --> n8n
    Query_Workflow_Credentials_Database --> Workflow_Credentials_Helper_Agent
```
