```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Gmail["fas:fa-envelope Gmail"]
    TaddyTopDaily["fas:fa-globe TaddyTopDaily"]
    Genre["fas:fa-cogs Genre"]
    Split_Out["fas:fa-cogs Split Out"]
    Whisper_Transcribe_Audio["fas:fa-globe Whisper Transcribe Audio"]
    Final_Data["fas:fa-cogs Final Data"]
    Merge_Results["fas:fa-cogs Merge Results"]
    HTML["fas:fa-cogs HTML"]
    Summarize_Podcast(["fas:fa-robot Summarize Podcast"]):::ai
    Schedule(("fas:fa-bolt Schedule")):::trigger
    Request_Audio_Crop["fas:fa-globe Request Audio Crop"]
    Get_Download_Link["fas:fa-globe Get Download Link"]
    Download_Cut_MP3["fas:fa-globe Download Cut MP3"]
    Download_Podcast["fas:fa-globe Download Podcast"]
    Wait["fas:fa-robot Wait"]
    If_Downloads_Ready{"fas:fa-code-branch If Downloads Ready"}:::logic

    HTML --> Gmail
    Wait --> Get_Download_Link
    Genre --> TaddyTopDaily
    Schedule --> Genre
    Split_Out --> Download_Podcast
    Final_Data --> Merge_Results
    Merge_Results --> HTML
    TaddyTopDaily --> Split_Out
    Download_Cut_MP3 --> Whisper_Transcribe_Audio
    Download_Podcast --> Request_Audio_Crop
    Get_Download_Link --> If_Downloads_Ready
    Summarize_Podcast --> Final_Data
    If_Downloads_Ready --> Download_Cut_MP3
    If_Downloads_Ready --> Wait
    Request_Audio_Crop --> Get_Download_Link
    Whisper_Transcribe_Audio --> Summarize_Podcast
```
