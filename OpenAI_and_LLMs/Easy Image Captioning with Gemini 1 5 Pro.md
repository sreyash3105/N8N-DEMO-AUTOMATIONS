```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Google_Gemini_Chat_Model["fab:fa-google Google Gemini Chat Model"]
    Structured_Output_Parser["fas:fa-robot Structured Output Parser"]
    Get_Info["fas:fa-cogs Get Info"]
    Resize_For_AI["fas:fa-cogs Resize For AI"]
    Calculate_Positioning["fas:fa-cogs Calculate Positioning"]
    Apply_Caption_to_Image["fas:fa-cogs Apply Caption to Image"]
    Merge_Image___Caption["fas:fa-cogs Merge Image & Caption"]
    Merge_Caption___Positions["fas:fa-cogs Merge Caption & Positions"]
    Get_Image["fas:fa-globe Get Image"]
    Image_Captioning_Agent(["fas:fa-robot Image Captioning Agent"]):::ai

    Get_Info --> Merge_Image___Caption
    Get_Image --> Resize_For_AI
    Get_Image --> Get_Info
    Resize_For_AI --> Image_Captioning_Agent
    Calculate_Positioning --> Merge_Caption___Positions
    Merge_Image___Caption --> Calculate_Positioning
    Merge_Image___Caption --> Merge_Caption___Positions
    Image_Captioning_Agent --> Merge_Image___Caption
    Google_Gemini_Chat_Model --> Image_Captioning_Agent
    Structured_Output_Parser --> Image_Captioning_Agent
    Merge_Caption___Positions --> Apply_Caption_to_Image
    When_clicking__Test_workflow_ --> Get_Image
```
