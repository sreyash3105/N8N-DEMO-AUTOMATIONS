```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Microsoft_Outlook23["fas:fa-cogs Microsoft Outlook23"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Set_Category["fas:fa-cogs Set Category"]
    Structured_Output_Parser["fas:fa-robot Structured Output Parser"]
    If{"fas:fa-code-branch If"}:::logic
    Set_Importance["fas:fa-cogs Set Importance"]
    AI__Analyse_Email["fas:fa-robot AI: Analyse Email"]:::ai
    Check_Mail_Schedule_Trigger(("fas:fa-bolt Check Mail Schedule Trigger")):::trigger
    Update_Contacts_Schedule_Trigger(("fas:fa-bolt Update Contacts Schedule Trigger")):::trigger
    Monday_com___Get_Contacts["fas:fa-cogs Monday.com - Get Contacts"]
    Airtable___Contacts["fas:fa-robot Airtable - Contacts"]
    Convert_to_Markdown["fas:fa-cogs Convert to Markdown"]
    Email_Messages["fas:fa-cogs Email Messages"]
    Rules["fas:fa-robot Rules"]
    Categories["fas:fa-robot Categories"]
    Delete_Rules["fas:fa-robot Delete Rules"]
    Contact["fas:fa-robot Contact"]
    Loop_Over_Items["fas:fa-cogs Loop Over Items"]
    Merge["fas:fa-cogs Merge"]

    If --> Set_Importance
    If --> Loop_Over_Items
    Merge --> AI__Analyse_Email
    Rules --> Merge
    Contact --> Merge
    Categories --> Merge
    Delete_Rules --> Merge
    Set_Category --> If
    Email_Messages --> Loop_Over_Items
    Set_Importance --> Loop_Over_Items
    Loop_Over_Items --> Contact
    AI__Analyse_Email --> Set_Category
    OpenAI_Chat_Model --> AI__Analyse_Email
    Convert_to_Markdown --> Email_Messages
    Microsoft_Outlook23 --> Convert_to_Markdown
    Structured_Output_Parser --> AI__Analyse_Email
    Monday_com___Get_Contacts --> Airtable___Contacts
    Check_Mail_Schedule_Trigger --> Microsoft_Outlook23
    Update_Contacts_Schedule_Trigger --> Monday_com___Get_Contacts
    When_clicking__Test_workflow_ --> Microsoft_Outlook23
    When_clicking__Test_workflow_ --> Rules
    When_clicking__Test_workflow_ --> Categories
    When_clicking__Test_workflow_ --> Delete_Rules
```
