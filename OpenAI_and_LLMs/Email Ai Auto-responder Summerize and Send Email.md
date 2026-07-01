```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Email_Trigger__IMAP_["fas:fa-envelope Email Trigger (IMAP)"]
    Markdown["fas:fa-cogs Markdown"]
    DeepSeek_R1(["fas:fa-robot DeepSeek R1"]):::ai
    Send_Email["fas:fa-envelope Send Email"]
    Qdrant_Vector_Store["fas:fa-robot Qdrant Vector Store"]
    Embeddings_OpenAI(["fas:fa-robot Embeddings OpenAI"]):::ai
    Email_Classifier{"fas:fa-robot Email Classifier"}:::logic
    Email_Summarization_Chain["fas:fa-robot Email Summarization Chain"]
    Write_email["fas:fa-robot Write email"]:::ai
    Review_email(["fas:fa-robot Review email"]):::ai
    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Create_collection["fas:fa-globe Create collection"]
    Refresh_collection["fas:fa-globe Refresh collection"]
    Get_folder["fab:fa-google Get folder"]
    Download_Files["fab:fa-google Download Files"]
    Default_Data_Loader["fas:fa-robot Default Data Loader"]
    Token_Splitter["fas:fa-robot Token Splitter"]
    Qdrant_Vector_Store1["fas:fa-robot Qdrant Vector Store1"]
    Embeddings_OpenAI1(["fas:fa-robot Embeddings OpenAI1"]):::ai
    Do_nothing["fas:fa-cogs Do nothing"]
    OpenAI(["fas:fa-robot OpenAI"]):::ai
    DeepSeek(["fas:fa-robot DeepSeek"]):::ai
    OpenAI_4_o_mini(["fas:fa-robot OpenAI 4-o-mini"]):::ai

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
