```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Respond_to_Webhook(("Respond to Webhook")):::trigger
    AI_Agent["AI Agent"]:::ai
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    Qdrant_Vector_Store["Qdrant Vector Store"]
    Create_collection["Create collection"]
    Refresh_collection["Refresh collection"]
    Get_folder["Get folder"]
    Download_Files["Download Files"]
    Embeddings_OpenAI(["Embeddings OpenAI"]):::ai
    Default_Data_Loader["Default Data Loader"]
    Token_Splitter["Token Splitter"]
    Verify(("Verify")):::trigger
    Respond(("Respond")):::trigger
    is_Message_{"is Message?"}:::logic
    Only_message["Only message"]
    Send["Send"]
    Window_Buffer_Memory[("Window Buffer Memory")]

    Verify --> Respond_to_Webhook
    Respond --> is_Message_
    AI_Agent --> Send
    Get_folder --> Download_Files
    is_Message_ --> AI_Agent
    is_Message_ --> Only_message
    Download_Files --> Qdrant_Vector_Store
    Token_Splitter --> Default_Data_Loader
    Embeddings_OpenAI --> Qdrant_Vector_Store
    OpenAI_Chat_Model --> AI_Agent
    Refresh_collection --> Get_folder
    Default_Data_Loader --> Qdrant_Vector_Store
    Window_Buffer_Memory --> AI_Agent
    When_clicking__Test_workflow_ --> Create_collection
    When_clicking__Test_workflow_ --> Refresh_collection
```
