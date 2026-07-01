```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Telegram_Trigger(("Telegram Trigger")):::trigger
    Embeddings_OpenAI(["Embeddings OpenAI"]):::ai
    Default_Data_Loader["Default Data Loader"]
    Recursive_Character_Text_Splitter["Recursive Character Text Splitter"]
    Stop_and_Error["Stop and Error"]
    Question_and_Answer_Chain["Question and Answer Chain"]
    Vector_Store_Retriever["Vector Store Retriever"]
    Pinecone_Vector_Store1["Pinecone Vector Store1"]
    Groq_Chat_Model["Groq Chat Model"]
    Check_If_is_a_document{"Check If is a document"}:::logic
    Change_to_application_pdf["Change to application/pdf"]
    Telegram_get_File["Telegram get File"]
    Embeddings(["Embeddings"]):::ai
    Telegram_Response["Telegram Response"]
    Telegram_Response_about_Database["Telegram Response about Database"]
    Stop_and_Error1["Stop and Error1"]
    Pinecone_Vector_Store["Pinecone Vector Store"]
    Limit_to_1["Limit to 1"]

    Embeddings --> Pinecone_Vector_Store1
    Limit_to_1 --> Telegram_Response_about_Database
    Groq_Chat_Model --> Question_and_Answer_Chain
    Telegram_Trigger --> Check_If_is_a_document
    Embeddings_OpenAI --> Pinecone_Vector_Store
    Telegram_Response --> Stop_and_Error
    Telegram_get_File --> Change_to_application_pdf
    Default_Data_Loader --> Pinecone_Vector_Store
    Pinecone_Vector_Store --> Limit_to_1
    Check_If_is_a_document --> Telegram_get_File
    Check_If_is_a_document --> Question_and_Answer_Chain
    Pinecone_Vector_Store1 --> Vector_Store_Retriever
    Vector_Store_Retriever --> Question_and_Answer_Chain
    Change_to_application_pdf --> Pinecone_Vector_Store
    Question_and_Answer_Chain --> Telegram_Response
    Telegram_Response_about_Database --> Stop_and_Error1
    Recursive_Character_Text_Splitter --> Default_Data_Loader
```
