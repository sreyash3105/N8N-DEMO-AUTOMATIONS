```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Telegram_Trigger(("Telegram Trigger")):::trigger
    CheckCommand{"CheckCommand"}:::logic
    Settings["Settings"]
    Chat_mode(["Chat_mode"]):::ai
    Greeting(["Greeting"]):::ai
    Text_reply["Text reply"]
    Send_Typing_action["Send Typing action"]
    Merge["Merge"]
    Create_an_image(["Create an image"]):::ai
    Send_error_message["Send error message"]
    Send_image["Send image"]
    PreProcessing["PreProcessing"]

    Merge --> CheckCommand
    Greeting --> Text_reply
    Settings --> Send_Typing_action
    Settings --> Merge
    Chat_mode --> Text_reply
    CheckCommand --> Chat_mode
    CheckCommand --> Greeting
    CheckCommand --> Create_an_image
    CheckCommand --> Send_error_message
    PreProcessing --> Settings
    Create_an_image --> Send_image
    Telegram_Trigger --> PreProcessing
    Send_Typing_action --> Merge
```
