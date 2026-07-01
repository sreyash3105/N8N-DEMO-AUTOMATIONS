```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_chat_message_received(("When chat message received")):::trigger
    Window_Buffer_Memory[("Window Buffer Memory")]
    Calculator["Calculator"]
    Edit_Fields["Edit Fields"]
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    RAG["RAG"]
    Qdrant_Vector_Store["Qdrant Vector Store"]
    Embeddings_OpenAI(["Embeddings OpenAI"]):::ai
    OpenAI_Chat_Model1(["OpenAI Chat Model1"]):::ai
    personal_shopper["personal_shopper"]
    Information_Extractor["Information Extractor"]
    OpenAI_Chat_Model2(["OpenAI Chat Model2"]):::ai
    Google_Drive2["Google Drive2"]
    Google_Drive1["Google Drive1"]
    Embeddings_OpenAI3(["Embeddings OpenAI3"]):::ai
    Default_Data_Loader2["Default Data Loader2"]
    Token_Splitter1["Token Splitter1"]
    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    HTTP_Request["HTTP Request"]
    Qdrant_Vector_Store1["Qdrant Vector Store1"]
    AI_Agent["AI Agent"]:::ai

    RAG --> AI_Agent
    Calculator --> AI_Agent
    Edit_Fields --> Information_Extractor
    HTTP_Request --> Google_Drive2
    Google_Drive1 --> Qdrant_Vector_Store1
    Google_Drive2 --> Google_Drive1
    Token_Splitter1 --> Default_Data_Loader2
    personal_shopper --> AI_Agent
    Embeddings_OpenAI --> Qdrant_Vector_Store
    OpenAI_Chat_Model --> AI_Agent
    Embeddings_OpenAI3 --> Qdrant_Vector_Store1
    OpenAI_Chat_Model1 --> RAG
    OpenAI_Chat_Model2 --> Information_Extractor
    Qdrant_Vector_Store --> RAG
    Default_Data_Loader2 --> Qdrant_Vector_Store1
    Window_Buffer_Memory --> AI_Agent
    Information_Extractor --> AI_Agent
    When_chat_message_received --> Edit_Fields
    When_clicking__Test_workflow_ --> HTTP_Request
```
