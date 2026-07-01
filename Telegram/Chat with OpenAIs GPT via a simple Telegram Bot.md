```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Telegram_Trigger(("Telegram Trigger")):::trigger
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    AI_Agent["AI Agent"]:::ai
    Telegram["Telegram"]

    AI_Agent --> Telegram
    Telegram_Trigger --> AI_Agent
    OpenAI_Chat_Model --> AI_Agent
```
