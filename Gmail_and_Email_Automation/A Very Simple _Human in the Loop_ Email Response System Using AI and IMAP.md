```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Email_Trigger__IMAP_["Email Trigger (IMAP)"]
    Markdown["Markdown"]
    Send_Email["Send Email"]
    Email_Summarization_Chain["Email Summarization Chain"]
    Write_email["Write email"]:::ai
    OpenAI(["OpenAI"]):::ai
    Approve_Email["Approve Email"]
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    Set_Email_text["Set Email text"]
    Approved_{"Approved?"}:::logic

    OpenAI --> Write_email
    Markdown --> Email_Summarization_Chain
    Approved_ --> Send_Email
    Write_email --> Set_Email_text
    Approve_Email --> Approved_
    Set_Email_text --> Approve_Email
    OpenAI_Chat_Model --> Email_Summarization_Chain
    Email_Trigger__IMAP_ --> Markdown
    Email_Summarization_Chain --> Write_email
```
