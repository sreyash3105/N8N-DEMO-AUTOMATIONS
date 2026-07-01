```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    OpenAI_Assistant(["fas:fa-robot OpenAI Assistant"]):::ai
    Calculator["fas:fa-robot Calculator"]
    Chat_Memory_Manager[("fas:fa-robot Chat Memory Manager")]
    Chat_Memory_Manager1[("fas:fa-robot Chat Memory Manager1")]
    Aggregate["fas:fa-cogs Aggregate"]
    Edit_Fields["fas:fa-cogs Edit Fields"]
    Limit["fas:fa-cogs Limit"]
    Chat_Trigger(("fas:fa-robot Chat Trigger")):::trigger
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]

    Limit --> Edit_Fields
    Aggregate --> OpenAI_Assistant
    Calculator --> OpenAI_Assistant
    Chat_Trigger --> Chat_Memory_Manager
    OpenAI_Assistant --> Chat_Memory_Manager1
    Chat_Memory_Manager --> Aggregate
    Chat_Memory_Manager1 --> Limit
    Window_Buffer_Memory --> Chat_Trigger
    Window_Buffer_Memory --> Chat_Memory_Manager
    Window_Buffer_Memory --> Chat_Memory_Manager1
```
