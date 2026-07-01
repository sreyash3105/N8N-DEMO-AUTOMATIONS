```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Email_Trigger__IMAP_["Email Trigger (IMAP)"]
    Markdown["Markdown"]
    Send_Email["Send Email"]
    Qdrant_Vector_Store["Qdrant Vector Store"]
    Embeddings_OpenAI(["Embeddings OpenAI"]):::ai
    Email_Summarization_Chain["Email Summarization Chain"]
    Write_email["Write email"]:::ai
    OpenAI(["OpenAI"]):::ai
    Gmail["Gmail"]
    Text_Classifier{"Text Classifier"}:::logic
    Edit_Fields["Edit Fields"]
    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    Create_collection["Create collection"]
    Refresh_collection["Refresh collection"]
    Get_folder["Get folder"]
    Download_Files["Download Files"]
    Default_Data_Loader["Default Data Loader"]
    Token_Splitter["Token Splitter"]
    Qdrant_Vector_Store1["Qdrant Vector Store1"]
    Embeddings_OpenAI1(["Embeddings OpenAI1"]):::ai
    DeepSeek_Chat_Model["DeepSeek Chat Model"]
    Email_Reviewer["Email Reviewer"]:::ai

    Gmail --> Text_Classifier
    OpenAI --> Write_email
    OpenAI --> Email_Reviewer
    OpenAI --> Text_Classifier
    Markdown --> Email_Summarization_Chain
    Get_folder --> Download_Files
    Edit_Fields --> Gmail
    Write_email --> Edit_Fields
    Download_Files --> Qdrant_Vector_Store1
    Email_Reviewer --> Edit_Fields
    Token_Splitter --> Default_Data_Loader
    Text_Classifier --> Send_Email
    Text_Classifier --> Email_Reviewer
    Embeddings_OpenAI --> Qdrant_Vector_Store
    Embeddings_OpenAI1 --> Qdrant_Vector_Store1
    Refresh_collection --> Get_folder
    DeepSeek_Chat_Model --> Email_Summarization_Chain
    Default_Data_Loader --> Qdrant_Vector_Store1
    Qdrant_Vector_Store --> Write_email
    Qdrant_Vector_Store --> Email_Reviewer
    Email_Trigger__IMAP_ --> Markdown
    Email_Summarization_Chain --> Write_email
    When_clicking__Test_workflow_ --> Create_collection
    When_clicking__Test_workflow_ --> Refresh_collection
```
