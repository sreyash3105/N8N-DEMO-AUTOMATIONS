```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Google_Calendar["fab:fa-google Google Calendar"]
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    Get_Email["fas:fa-envelope Get Email"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Listen_for_incoming_events(("fab:fa-telegram Listen for incoming events")):::trigger
    Telegram["fab:fa-telegram Telegram"]
    If{"fas:fa-code-branch If"}:::logic
    Speech_to_Text(["fas:fa-robot Speech to Text"]):::ai
    Voice_or_Text["fas:fa-cogs Voice or Text"]
    Get_Voice_File["fab:fa-telegram Get Voice File"]
    Angie__AI_Assistant_____["fas:fa-robot Angie, AI Assistant 👩🏻‍🏫"]:::ai
    Tasks["fas:fa-cogs Tasks"]
    Contacts["fas:fa-cogs Contacts"]

    If --> Get_Voice_File
    If --> Angie__AI_Assistant_____
    Tasks --> Angie__AI_Assistant_____
    Contacts --> Angie__AI_Assistant_____
    Get_Email --> Angie__AI_Assistant_____
    Voice_or_Text --> If
    Get_Voice_File --> Speech_to_Text
    Speech_to_Text --> Angie__AI_Assistant_____
    Google_Calendar --> Angie__AI_Assistant_____
    OpenAI_Chat_Model --> Angie__AI_Assistant_____
    Window_Buffer_Memory --> Angie__AI_Assistant_____
    Listen_for_incoming_events --> Voice_or_Text
    Angie__AI_Assistant_____ --> Telegram
```
