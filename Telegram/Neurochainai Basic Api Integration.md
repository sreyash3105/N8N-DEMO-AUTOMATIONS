```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Telegram_Trigger(("Telegram Trigger")):::trigger
    Code["Code"]
    HTTP_Request3["HTTP Request3"]
    Telegram2["Telegram2"]
    Telegram1["Telegram1"]
    Telegram4["Telegram4"]
    Telegram3["Telegram3"]
    Telegram5["Telegram5"]
    Telegram6["Telegram6"]
    Telegram7["Telegram7"]
    NeurochainAI___REST_API["NeurochainAI - REST API"]
    TYPING___ACTION["TYPING - ACTION"]
    AI_Response["AI Response"]
    No_response["No response"]
    Prompt_too_short["Prompt too short"]
    Switch2{"Switch2"}:::logic
    Code1["Code1"]
    Switch{"Switch"}:::logic
    NeurochainAI___Flux["NeurochainAI - Flux"]
    Switch1{"Switch1"}:::logic

    Code --> HTTP_Request3
    Code1 --> Telegram2
    Switch --> Code1
    Switch --> TYPING___ACTION
    Switch --> TYPING___ACTION
    Switch1 --> Telegram6
    Switch1 --> Telegram3
    Switch2 --> No_response
    Switch2 --> Prompt_too_short
    Telegram1 --> Telegram4
    Telegram2 --> NeurochainAI___Flux
    Telegram3 --> Telegram5
    Telegram6 --> Telegram7
    HTTP_Request3 --> Telegram1
    TYPING___ACTION --> NeurochainAI___REST_API
    Telegram_Trigger --> Switch
    NeurochainAI___Flux --> Code
    NeurochainAI___Flux --> Switch1
    NeurochainAI___REST_API --> AI_Response
    NeurochainAI___REST_API --> Switch2
```
