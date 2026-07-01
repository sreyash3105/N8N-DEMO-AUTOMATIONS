```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Schedule_Trigger(("Schedule Trigger")):::trigger
    Search_daily["Search daily"]
    Search_weekly["Search weekly"]
    confirmation_email1["confirmation email1"]
    Execute_Workflow["Execute Workflow"]
    Create_Event["Create Event"]
    Execute_Workflow_Trigger(("Execute Workflow Trigger")):::trigger
    Unsubscribe_Form(("Unsubscribe Form")):::trigger
    Set_Email_Vars["Set Email Vars"]
    Log_Last_Sent["Log Last Sent"]
    Search_surprise["Search surprise"]
    Should_Send___True["Should Send = True"]
    Should_Send_["Should Send?"]
    Create_Subscriber["Create Subscriber"]
    Update_Subscriber["Update Subscriber"]
    Subscribe_Form(("Subscribe Form")):::trigger
    Execution_Data["Execution Data"]
    Window_Buffer_Memory[("Window Buffer Memory")]
    Wikipedia["Wikipedia"]
    Content_Generation_Agent["Content Generation Agent"]:::ai
    Groq_Chat_Model["Groq Chat Model"]
    Generate_Image(["Generate Image"]):::ai
    Resize_Image["Resize Image"]
    Send_Message["Send Message"]

    Wikipedia --> Content_Generation_Agent
    Create_Event --> Execute_Workflow
    Resize_Image --> Set_Email_Vars
    Search_daily --> Create_Event
    Send_Message --> Log_Last_Sent
    Should_Send_ --> Should_Send___True
    Search_weekly --> Create_Event
    Execution_Data --> Content_Generation_Agent
    Generate_Image --> Resize_Image
    Set_Email_Vars --> Send_Message
    Subscribe_Form --> Create_Subscriber
    Groq_Chat_Model --> Content_Generation_Agent
    Search_surprise --> Should_Send_
    Schedule_Trigger --> Search_surprise
    Schedule_Trigger --> Search_daily
    Schedule_Trigger --> Search_weekly
    Unsubscribe_Form --> Update_Subscriber
    Create_Subscriber --> confirmation_email1
    Should_Send___True --> Create_Event
    Window_Buffer_Memory --> Content_Generation_Agent
    Content_Generation_Agent --> Generate_Image
    Execute_Workflow_Trigger --> Execution_Data
```
