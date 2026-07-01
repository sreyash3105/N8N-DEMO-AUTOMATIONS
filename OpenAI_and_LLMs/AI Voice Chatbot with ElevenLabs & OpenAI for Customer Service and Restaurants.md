```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    AI_Agent["AI Agent"]:::ai
    Vector_Store_Tool["Vector Store Tool"]
    Qdrant_Vector_Store["Qdrant Vector Store"]
    Embeddings_OpenAI(["Embeddings OpenAI"]):::ai
    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    Create_collection["Create collection"]
    Refresh_collection["Refresh collection"]
    Get_folder["Get folder"]
    Download_Files["Download Files"]
    Default_Data_Loader["Default Data Loader"]
    Token_Splitter["Token Splitter"]
    Qdrant_Vector_Store1["Qdrant Vector Store1"]
    Embeddings_OpenAI1(["Embeddings OpenAI1"]):::ai
    Respond_to_ElevenLabs(("Respond to ElevenLabs")):::trigger
    OpenAI(["OpenAI"]):::ai
    Listen(("Listen")):::trigger
    Window_Buffer_Memory[("Window Buffer Memory")]
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai

    Listen --> AI_Agent
    OpenAI --> AI_Agent
    AI_Agent --> Respond_to_ElevenLabs
    Get_folder --> Download_Files
    Download_Files --> Qdrant_Vector_Store1
    Token_Splitter --> Default_Data_Loader
    Embeddings_OpenAI --> Qdrant_Vector_Store
    OpenAI_Chat_Model --> Vector_Store_Tool
    Vector_Store_Tool --> AI_Agent
    Embeddings_OpenAI1 --> Qdrant_Vector_Store1
    Refresh_collection --> Get_folder
    Default_Data_Loader --> Qdrant_Vector_Store1
    Qdrant_Vector_Store --> Vector_Store_Tool
    Window_Buffer_Memory --> AI_Agent
    When_clicking__Test_workflow_ --> Create_collection
    When_clicking__Test_workflow_ --> Refresh_collection
```
