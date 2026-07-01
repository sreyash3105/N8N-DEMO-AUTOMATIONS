```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    No_Recording_Transcript_available["fas:fa-cogs No Recording/Transcript available"]
    Zoom__Get_data_of_last_meeting["fas:fa-cogs Zoom: Get data of last meeting"]
    Filter_transcript_URL["fas:fa-cogs Filter transcript URL"]
    Filter__Only_1_item["fas:fa-cogs Filter: Only 1 item"]
    Zoom__Get_transcript_file["fas:fa-globe Zoom: Get transcript file"]
    Extract_text_from_transcript_file["fas:fa-cogs Extract text from transcript file"]
    Format_transcript_text["fas:fa-cogs Format transcript text"]
    Zoom__Get_participants_data["fas:fa-globe Zoom: Get participants data"]
    Create_meeting_summary(["fas:fa-robot Create meeting summary"]):::ai
    Sort_for_mail_delivery["fas:fa-cogs Sort for mail delivery"]
    Format_to_html["fas:fa-cogs Format to html"]
    Send_meeting_summary["fas:fa-envelope Send meeting summary"]
    Create_tasks["fas:fa-robot Create tasks"]
    Create_tasks_and_follow_up_call["fas:fa-robot Create tasks and follow-up call"]:::ai
    Create_follow_up_call["fas:fa-cogs Create follow-up call"]
    Filter__Last_24_hours["fas:fa-cogs Filter: Last 24 hours"]
    Execute_Workflow_Trigger(("fas:fa-bolt Execute Workflow Trigger")):::trigger
    Split_Out["fas:fa-cogs Split Out"]
    ClickUp["fas:fa-cogs ClickUp"]
    Zoom__Get_transcripts_data["fas:fa-globe Zoom: Get transcripts data"]

    Split_Out --> ClickUp
    Create_tasks --> Create_tasks_and_follow_up_call
    Format_to_html --> Send_meeting_summary
    OpenAI_Chat_Model --> Create_tasks_and_follow_up_call
    Filter__Only_1_item --> Filter__Only_1_item
    Filter__Only_1_item --> Zoom__Get_transcript_file
    Create_follow_up_call --> Create_tasks_and_follow_up_call
    Filter_transcript_URL --> Filter__Only_1_item
    Filter__Last_24_hours --> Zoom__Get_transcripts_data
    Create_meeting_summary --> Sort_for_mail_delivery
    Create_meeting_summary --> Create_tasks_and_follow_up_call
    Format_transcript_text --> Zoom__Get_participants_data
    Sort_for_mail_delivery --> Format_to_html
    Execute_Workflow_Trigger --> Split_Out
    Zoom__Get_transcript_file --> Extract_text_from_transcript_file
    Zoom__Get_transcripts_data --> Filter_transcript_URL
    Zoom__Get_transcripts_data --> No_Recording_Transcript_available
    Zoom__Get_participants_data --> Create_meeting_summary
    Zoom__Get_data_of_last_meeting --> Filter__Last_24_hours
    Extract_text_from_transcript_file --> Format_transcript_text
    When_clicking__Test_workflow_ --> Zoom__Get_data_of_last_meeting
```
