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
    Email_Classifier{"Email Classifier"}:::logic
    Email_Summarization_Chain["Email Summarization Chain"]
    Write_email["Write email"]:::ai
    Review_email(["Review email"]):::ai
    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    Create_collection["Create collection"]
    Refresh_collection["Refresh collection"]
    Get_folder["Get folder"]
    Download_Files["Download Files"]
    Default_Data_Loader["Default Data Loader"]
    Token_Splitter["Token Splitter"]
    Qdrant_Vector_Store1["Qdrant Vector Store1"]
    Embeddings_OpenAI1(["Embeddings OpenAI1"]):::ai
    Do_nothing["Do nothing"]
    OpenAI(["OpenAI"]):::ai
    DeepSeek(["DeepSeek"]):::ai
    OpenAI_4_o_mini(["OpenAI 4-o-mini"]):::ai

    OpenAI --> Write_email
    DeepSeek --> Review_email
    Markdown --> Email_Summarization_Chain
    Get_folder --> Download_Files
    DeepSeek_R1 --> Email_Summarization_Chain
    Write_email --> Review_email
    Review_email --> Send_Email
    Download_Files --> Qdrant_Vector_Store1
    Token_Splitter --> Default_Data_Loader
    OpenAI_4_o_mini --> Email_Classifier
    Email_Classifier --> Write_email
    Email_Classifier --> Do_nothing
    Embeddings_OpenAI --> Qdrant_Vector_Store
    Embeddings_OpenAI1 --> Qdrant_Vector_Store1
    Refresh_collection --> Get_folder
    Default_Data_Loader --> Qdrant_Vector_Store1
    Qdrant_Vector_Store --> Write_email
    Email_Trigger__IMAP_ --> Markdown
    Email_Summarization_Chain --> Email_Classifier
    When_clicking__Test_workflow_ --> Create_collection
    When_clicking__Test_workflow_ --> Refresh_collection
```
