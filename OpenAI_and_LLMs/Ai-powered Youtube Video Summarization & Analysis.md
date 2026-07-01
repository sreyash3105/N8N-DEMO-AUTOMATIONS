```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Webhook(("fas:fa-bolt Webhook")):::trigger
    YouTube_Transcript["fas:fa-cogs YouTube Transcript"]
    Split_Out["fas:fa-cogs Split Out"]
    Respond_to_Webhook(("fas:fa-bolt Respond to Webhook")):::trigger
    Telegram["fab:fa-telegram Telegram"]
    Get_YouTube_URL["fas:fa-cogs Get YouTube URL"]
    YouTube_Video_ID["fas:fa-cogs YouTube Video ID"]
    Get_YouTube_Video["fas:fa-cogs Get YouTube Video"]
    gpt_4o_mini(["fas:fa-robot gpt-4o-mini"]):::ai
    Summarize___Analyze_Transcript(["fas:fa-robot Summarize & Analyze Transcript"]):::ai
    Concatenate["fas:fa-cogs Concatenate"]
    Response_Object["fas:fa-cogs Response Object"]

    Webhook --> Get_YouTube_URL
    Split_Out --> Concatenate
    Concatenate --> Summarize___Analyze_Transcript
    gpt_4o_mini --> Summarize___Analyze_Transcript
    Get_YouTube_URL --> YouTube_Video_ID
    Response_Object --> Respond_to_Webhook
    Response_Object --> Telegram
    YouTube_Video_ID --> Get_YouTube_Video
    Summarize___Analyze_Transcript --> Response_Object
```
