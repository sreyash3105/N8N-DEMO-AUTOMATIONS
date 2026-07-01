```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    If{"If"}:::logic
    Edit_Fields1["Edit Fields1"]
    Edit_Fields2["Edit Fields2"]
    OpenAI(["OpenAI"]):::ai
    Chat_Trigger(("Chat Trigger")):::trigger
    Postgres_Chat_Memory[("Postgres Chat Memory")]
    Postgres_Chat_Memory1[("Postgres Chat Memory1")]
    Products_in_Daatabase["Products in Daatabase"]
    Knowledge_Base["Knowledge Base"]
    External_API["External API"]
    OpenAI2(["OpenAI2"]):::ai

    If --> Edit_Fields1
    If --> OpenAI2
    OpenAI --> Edit_Fields2
    Chat_Trigger --> If
    Edit_Fields1 --> OpenAI
    Edit_Fields2 --> OpenAI2
    External_API --> OpenAI2
    Knowledge_Base --> OpenAI2
    Postgres_Chat_Memory --> OpenAI2
    Postgres_Chat_Memory1 --> OpenAI
    Products_in_Daatabase --> OpenAI2
```
