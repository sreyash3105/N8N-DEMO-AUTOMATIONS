```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Capture_Frames["fas:fa-cogs Capture Frames"]
    Split_Out_Frames["fas:fa-cogs Split Out Frames"]
    Download_Video["fas:fa-globe Download Video"]
    Convert_to_Binary["fas:fa-cogs Convert to Binary"]
    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Combine_Script["fas:fa-cogs Combine Script"]
    Upload_to_GDrive["fab:fa-google Upload to GDrive"]
    Stay_Within_Service_Limits["fas:fa-robot Stay Within Service Limits"]
    For_Every_15_Frames["fas:fa-cogs For Every 15 Frames"]
    Resize_Frame["fas:fa-cogs Resize Frame"]
    Aggregate_Frames["fas:fa-cogs Aggregate Frames"]
    Use_Text_to_Speech(["fas:fa-robot Use Text-to-Speech"]):::ai
    Generate_Narration_Script(["fas:fa-robot Generate Narration Script"]):::ai

    Resize_Frame --> Aggregate_Frames
    Capture_Frames --> Split_Out_Frames
    Combine_Script --> Use_Text_to_Speech
    Download_Video --> Capture_Frames
    Aggregate_Frames --> Generate_Narration_Script
    Split_Out_Frames --> For_Every_15_Frames
    Convert_to_Binary --> Resize_Frame
    OpenAI_Chat_Model --> Generate_Narration_Script
    Use_Text_to_Speech --> Upload_to_GDrive
    For_Every_15_Frames --> Combine_Script
    For_Every_15_Frames --> Convert_to_Binary
    Generate_Narration_Script --> Stay_Within_Service_Limits
    Stay_Within_Service_Limits --> For_Every_15_Frames
    When_clicking__Test_workflow_ --> Download_Video
```
