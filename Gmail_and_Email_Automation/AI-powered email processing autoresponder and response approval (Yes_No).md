```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Email_Trigger__IMAP_["Email Trigger (IMAP)"]
    Markdown["Markdown"]
    DeepSeek_R1(["DeepSeek R1"]):::ai
    Send_Email["Send Email"]
    Qdrant_Vector_Store["Qdrant Vector Store"]
    Embeddings_OpenAI(["Embeddings OpenAI"]):::ai
    Email_Summarization_Chain["Email Summarization Chain"]
    Write_email["Write email"]:::ai
    OpenAI(["OpenAI"]):::ai
    Set_Email["Set Email"]
    Approve_{"Approve?"}:::logic
    Send_Draft["Send Draft"]

    OpenAI --> Write_email
    Approve_ --> Send_Email
    Approve_ --> Set_Email
    Markdown --> Email_Summarization_Chain
    Set_Email --> Write_email
    Send_Draft --> Approve_
    DeepSeek_R1 --> Email_Summarization_Chain
    Write_email --> Send_Draft
    Embeddings_OpenAI --> Qdrant_Vector_Store
    Qdrant_Vector_Store --> Write_email
    Email_Trigger__IMAP_ --> Markdown
    Email_Summarization_Chain --> Set_Email
```
