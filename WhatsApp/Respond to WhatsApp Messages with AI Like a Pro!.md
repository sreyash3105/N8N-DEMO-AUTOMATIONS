```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    WhatsApp_Trigger(("WhatsApp Trigger")):::trigger
    Get_Audio_URL["Get Audio URL"]
    Get_Video_URL["Get Video URL"]
    Get_Image_URL["Get Image URL"]
    Download_Video["Download Video"]
    Download_Audio["Download Audio"]
    Download_Image["Download Image"]
    Window_Buffer_Memory[("Window Buffer Memory")]
    Get_User_s_Message["Get User's Message"]
    Split_Out_Message_Parts["Split Out Message Parts"]
    Wikipedia["Wikipedia"]
    Redirect_Message_Types{"Redirect Message Types"}:::logic
    Get_Text["Get Text"]
    Respond_to_User["Respond to User"]
    Image_Explainer(["Image Explainer"]):::ai
    Format_Response["Format Response"]
    Google_Gemini_Chat_Model["Google Gemini Chat Model"]
    Google_Gemini_Audio["Google Gemini Audio"]
    Google_Gemini_Video["Google Gemini Video"]
    Google_Gemini_Chat_Model1["Google Gemini Chat Model1"]
    Google_Gemini_Chat_Model2["Google Gemini Chat Model2"]
    Format_Response1["Format Response1"]
    Text_Summarizer(["Text Summarizer"]):::ai
    AI_Agent["AI Agent"]:::ai

    AI_Agent --> Respond_to_User
    Get_Text --> Text_Summarizer
    Wikipedia --> AI_Agent
    Get_Audio_URL --> Download_Audio
    Get_Image_URL --> Download_Image
    Get_Video_URL --> Download_Video
    Download_Audio --> Google_Gemini_Audio
    Download_Image --> Image_Explainer
    Download_Video --> Google_Gemini_Video
    Format_Response --> Get_User_s_Message
    Image_Explainer --> Get_User_s_Message
    Text_Summarizer --> Get_User_s_Message
    Format_Response1 --> Get_User_s_Message
    WhatsApp_Trigger --> Split_Out_Message_Parts
    Get_User_s_Message --> AI_Agent
    Google_Gemini_Audio --> Format_Response1
    Google_Gemini_Video --> Format_Response
    Window_Buffer_Memory --> AI_Agent
    Redirect_Message_Types --> Get_Audio_URL
    Redirect_Message_Types --> Get_Video_URL
    Redirect_Message_Types --> Get_Image_URL
    Redirect_Message_Types --> Get_Text
    Split_Out_Message_Parts --> Redirect_Message_Types
    Google_Gemini_Chat_Model --> AI_Agent
    Google_Gemini_Chat_Model1 --> Image_Explainer
    Google_Gemini_Chat_Model2 --> Text_Summarizer
```
