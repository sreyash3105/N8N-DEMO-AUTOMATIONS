```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    HTTP_Request["fas:fa-globe HTTP Request"]
    Extract_from_File["fas:fa-cogs Extract from File"]
    Create_HR_Policies["fas:fa-robot Create HR Policies"]
    Embeddings_OpenAI(["fas:fa-robot Embeddings OpenAI"]):::ai
    Default_Data_Loader["fas:fa-robot Default Data Loader"]
    Recursive_Character_Text_Splitter["fas:fa-robot Recursive Character Text Splitter"]
    Telegram_Trigger(("fab:fa-telegram Telegram Trigger")):::trigger
    Verify_Message_Type{"fas:fa-code-branch Verify Message Type"}:::logic
    OpenAI(["fas:fa-robot OpenAI"]):::ai
    Telegram1["fab:fa-telegram Telegram1"]
    Unsupported_Message_Type["fab:fa-telegram Unsupported Message Type"]
    AI_Agent["fas:fa-robot AI Agent"]:::ai
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Postgres_Chat_Memory[("fas:fa-database Postgres Chat Memory")]
    Answer_questions_with_a_vector_store["fas:fa-robot Answer questions with a vector store"]
    Postgres_PGVector_Store["fas:fa-robot Postgres PGVector Store"]
    OpenAI_Chat_Model1(["fas:fa-robot OpenAI Chat Model1"]):::ai
    Embeddings_OpenAI1(["fas:fa-robot Embeddings OpenAI1"]):::ai
    Telegram["fab:fa-telegram Telegram"]
    Edit_Fields["fas:fa-cogs Edit Fields"]

    OpenAI --> AI_Agent
    AI_Agent --> Telegram
    Telegram1 --> OpenAI
    Edit_Fields --> AI_Agent
    HTTP_Request --> Extract_from_File
    Telegram_Trigger --> Verify_Message_Type
    Embeddings_OpenAI --> Create_HR_Policies
    Extract_from_File --> Create_HR_Policies
    OpenAI_Chat_Model --> AI_Agent
    Embeddings_OpenAI1 --> Postgres_PGVector_Store
    OpenAI_Chat_Model1 --> Answer_questions_with_a_vector_store
    Default_Data_Loader --> Create_HR_Policies
    Verify_Message_Type --> Edit_Fields
    Verify_Message_Type --> Telegram1
    Verify_Message_Type --> Unsupported_Message_Type
    Postgres_Chat_Memory --> AI_Agent
    Postgres_PGVector_Store --> Answer_questions_with_a_vector_store
    Recursive_Character_Text_Splitter --> Default_Data_Loader
    When_clicking__Test_workflow_ --> HTTP_Request
    Answer_questions_with_a_vector_store --> AI_Agent
```
