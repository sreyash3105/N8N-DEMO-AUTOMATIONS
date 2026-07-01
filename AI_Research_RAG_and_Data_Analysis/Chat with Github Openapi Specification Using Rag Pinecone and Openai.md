```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    HTTP_Request["fas:fa-globe HTTP Request"]
    Pinecone_Vector_Store["fas:fa-robot Pinecone Vector Store"]
    Default_Data_Loader["fas:fa-robot Default Data Loader"]
    Recursive_Character_Text_Splitter["fas:fa-robot Recursive Character Text Splitter"]
    When_chat_message_received(("fas:fa-robot When chat message received")):::trigger
    AI_Agent["fas:fa-robot AI Agent"]:::ai
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    Vector_Store_Tool["fas:fa-robot Vector Store Tool"]
    OpenAI_Chat_Model1(["fas:fa-robot OpenAI Chat Model1"]):::ai
    Generate_User_Query_Embedding(["fas:fa-robot Generate User Query Embedding"]):::ai
    Pinecone_Vector_Store__Querying_["fas:fa-robot Pinecone Vector Store (Querying)"]
    Generate_Embeddings(["fas:fa-robot Generate Embeddings"]):::ai

    HTTP_Request --> Pinecone_Vector_Store
    OpenAI_Chat_Model --> AI_Agent
    Vector_Store_Tool --> AI_Agent
    OpenAI_Chat_Model1 --> Vector_Store_Tool
    Default_Data_Loader --> Pinecone_Vector_Store
    Generate_Embeddings --> Pinecone_Vector_Store
    Window_Buffer_Memory --> AI_Agent
    When_chat_message_received --> AI_Agent
    Generate_User_Query_Embedding --> Pinecone_Vector_Store__Querying_
    Pinecone_Vector_Store__Querying_ --> Vector_Store_Tool
    Recursive_Character_Text_Splitter --> Default_Data_Loader
    When_clicking__Test_workflow_ --> HTTP_Request
```
