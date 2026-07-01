```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    OpenAI(["OpenAI"]):::ai
    When_clicking__Execute_Workflow_(("When clicking 'Execute Workflow'")):::trigger
    Set["Set"]
    Set1["Set1"]
    Chat_OpenAI(["Chat OpenAI"]):::ai
    Custom___Wikipedia["Custom - Wikipedia"]
    Custom___LLM_Chain_Node["Custom - LLM Chain Node"]
    Agent["Agent"]:::ai

    Set --> Custom___LLM_Chain_Node
    Set1 --> Agent
    OpenAI --> Custom___LLM_Chain_Node
    Chat_OpenAI --> Agent
    Custom___Wikipedia --> Agent
    When_clicking__Execute_Workflow_ --> Set
    When_clicking__Execute_Workflow_ --> Set1
```
