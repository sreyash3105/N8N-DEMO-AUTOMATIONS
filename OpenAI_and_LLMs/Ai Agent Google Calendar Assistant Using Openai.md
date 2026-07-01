```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_chat_message_received(("fas:fa-robot When chat message received")):::trigger
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    Google_Calendar___Get_Events["fab:fa-google Google Calendar - Get Events"]
    Google_Calendar___Create_events["fab:fa-google Google Calendar - Create events"]
    Calendar_AI_Agent["fas:fa-robot Calendar AI Agent"]:::ai

    OpenAI_Chat_Model --> Calendar_AI_Agent
    Window_Buffer_Memory --> Calendar_AI_Agent
    When_chat_message_received --> Calendar_AI_Agent
    Google_Calendar___Get_Events --> Calendar_AI_Agent
    Google_Calendar___Create_events --> Calendar_AI_Agent
```
