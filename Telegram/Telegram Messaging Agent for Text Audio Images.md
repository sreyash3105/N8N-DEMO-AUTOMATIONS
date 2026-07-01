```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Check_User___Chat_ID{"fas:fa-code-branch Check User & Chat ID"}:::logic
    Error_message["fab:fa-telegram Error message"]
    Listen_for_Telegram_Events(("fab:fa-telegram Listen for Telegram Events")):::trigger
    Set_Webhook_Test_URL["fas:fa-globe Set Webhook Test URL"]
    Get_Telegram_Webhook_Info["fab:fa-telegram Get Telegram Webhook Info"]
    Image_Schema["fas:fa-cogs Image Schema"]
    gpt_4o_mini(["fas:fa-robot gpt-4o-mini"]):::ai
    Get_Audio_File["fab:fa-telegram Get Audio File"]
    Get_Image["fab:fa-telegram Get Image"]
    Analyze_Image(["fas:fa-robot Analyze Image"]):::ai
    Transcribe_Recording(["fas:fa-robot Transcribe Recording"]):::ai
    gpt_4o_mini1(["fas:fa-robot gpt-4o-mini1"]):::ai
    Test_Webhook_Status["fab:fa-telegram Test Webhook Status"]
    Production_Webhook_Status["fab:fa-telegram Production Webhook Status"]
    Set_Webhook_Production_URL["fas:fa-globe Set Webhook Production URL"]
    Edit_Fields["fas:fa-cogs Edit Fields"]
    Audio_Task_Message["fab:fa-telegram Audio Task Message"]
    Audio_Other_Message["fab:fa-telegram Audio Other Message"]
    Text_Task_Message["fab:fa-telegram Text Task Message"]
    Text_Other_Message["fab:fa-telegram Text Other Message"]
    Image_Message["fab:fa-telegram Image Message"]
    Convert_to_Image_File["fas:fa-cogs Convert to Image File"]
    Extract_from_File_to_Base64["fas:fa-cogs Extract from File to Base64"]
    Text_Classifier_Audio{"fas:fa-robot Text Classifier Audio"}:::logic
    Text_Classifier{"fas:fa-robot Text Classifier"}:::logic
    Telegram_Token___Webhooks["fab:fa-telegram Telegram Token & Webhooks"]
    Get_Webhook_Status["fab:fa-telegram Get Webhook Status"]
    Validation["fas:fa-cogs Validation"]
    Message_Router{"fas:fa-code-branch Message Router"}:::logic

    Get_Image --> Extract_from_File_to_Base64
    Validation --> Check_User___Chat_ID
    Edit_Fields --> Text_Classifier
    gpt_4o_mini --> Text_Classifier_Audio
    Image_Schema --> Get_Image
    gpt_4o_mini1 --> Text_Classifier
    Analyze_Image --> Image_Message
    Get_Audio_File --> Transcribe_Recording
    Message_Router --> Get_Audio_File
    Message_Router --> Edit_Fields
    Message_Router --> Image_Schema
    Message_Router --> Error_message
    Text_Classifier --> Text_Task_Message
    Text_Classifier --> Text_Other_Message
    Check_User___Chat_ID --> Message_Router
    Check_User___Chat_ID --> Error_message
    Set_Webhook_Test_URL --> Test_Webhook_Status
    Transcribe_Recording --> Text_Classifier_Audio
    Convert_to_Image_File --> Analyze_Image
    Text_Classifier_Audio --> Audio_Task_Message
    Text_Classifier_Audio --> Audio_Other_Message
    Get_Telegram_Webhook_Info --> Get_Webhook_Status
    Telegram_Token___Webhooks --> Set_Webhook_Production_URL
    Telegram_Token___Webhooks --> Set_Webhook_Test_URL
    Telegram_Token___Webhooks --> Get_Telegram_Webhook_Info
    Listen_for_Telegram_Events --> Validation
    Set_Webhook_Production_URL --> Production_Webhook_Status
    Extract_from_File_to_Base64 --> Convert_to_Image_File
```
