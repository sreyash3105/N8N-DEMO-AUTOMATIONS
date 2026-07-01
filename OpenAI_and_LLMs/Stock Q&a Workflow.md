```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Embeddings_OpenAI1(["Embeddings OpenAI1"]):::ai
    On_new_manual_Chat_Message(("On new manual Chat Message")):::trigger
    Retrieval_QA_Chain["Retrieval QA Chain"]
    Respond_to_Webhook(("Respond to Webhook")):::trigger
    Vector_Store_Retriever["Vector Store Retriever"]
    Webhook1(("Webhook1")):::trigger
    When_clicking__Execute_Workflow_(("When clicking 'Execute Workflow'")):::trigger
    Google_Drive["Google Drive"]
    Binary_to_Document["Binary to Document"]
    Recursive_Character_Text_Splitter["Recursive Character Text Splitter"]
    Embeddings_OpenAI(["Embeddings OpenAI"]):::ai
    Qdrant_Vector_Store["Qdrant Vector Store"]
    Qdrant_Vector_Store1["Qdrant Vector Store1"]
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai

    Webhook1 --> Retrieval_QA_Chain
    Google_Drive --> Qdrant_Vector_Store
    Embeddings_OpenAI --> Qdrant_Vector_Store
    OpenAI_Chat_Model --> Retrieval_QA_Chain
    Binary_to_Document --> Qdrant_Vector_Store
    Embeddings_OpenAI1 --> Qdrant_Vector_Store1
    Retrieval_QA_Chain --> Respond_to_Webhook
    Qdrant_Vector_Store1 --> Vector_Store_Retriever
    Vector_Store_Retriever --> Retrieval_QA_Chain
    On_new_manual_Chat_Message --> Retrieval_QA_Chain
    When_clicking__Execute_Workflow_ --> Google_Drive
    Recursive_Character_Text_Splitter --> Binary_to_Document
```
