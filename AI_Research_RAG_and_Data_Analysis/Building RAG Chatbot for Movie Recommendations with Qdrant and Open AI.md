```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    GitHub["fas:fa-cogs GitHub"]
    Extract_from_File["fas:fa-cogs Extract from File"]
    Embeddings_OpenAI(["fas:fa-robot Embeddings OpenAI"]):::ai
    Default_Data_Loader["fas:fa-robot Default Data Loader"]
    Token_Splitter["fas:fa-robot Token Splitter"]
    Qdrant_Vector_Store["fas:fa-robot Qdrant Vector Store"]
    When_chat_message_received(("fas:fa-robot When chat message received")):::trigger
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Call_n8n_Workflow_Tool["fas:fa-robot Call n8n Workflow Tool"]
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    Execute_Workflow_Trigger(("fas:fa-bolt Execute Workflow Trigger")):::trigger
    Merge["fas:fa-cogs Merge"]
    Split_Out["fas:fa-cogs Split Out"]
    Split_Out1["fas:fa-cogs Split Out1"]
    Merge1["fas:fa-cogs Merge1"]
    Aggregate["fas:fa-cogs Aggregate"]
    AI_Agent["fas:fa-robot AI Agent"]:::ai
    Embedding_Recommendation_Request_with_Open_AI["fas:fa-globe Embedding Recommendation Request with Open AI"]
    Embedding_Anti_Recommendation_Request_with_Open_AI["fas:fa-globe Embedding Anti-Recommendation Request with Open AI"]
    Extracting_Embedding["fas:fa-cogs Extracting Embedding"]
    Extracting_Embedding1["fas:fa-cogs Extracting Embedding1"]
    Calling_Qdrant_Recommendation_API["fas:fa-globe Calling Qdrant Recommendation API"]
    Retrieving_Recommended_Movies_Meta_Data["fas:fa-globe Retrieving Recommended Movies Meta Data"]
    Selecting_Fields_Relevant_for_Agent["fas:fa-robot Selecting Fields Relevant for Agent"]

    Merge --> Calling_Qdrant_Recommendation_API
    GitHub --> Extract_from_File
    Merge1 --> Selecting_Fields_Relevant_for_Agent
    Split_Out --> Merge1
    Split_Out1 --> Merge1
    Token_Splitter --> Default_Data_Loader
    Embeddings_OpenAI --> Qdrant_Vector_Store
    Extract_from_File --> Qdrant_Vector_Store
    OpenAI_Chat_Model --> AI_Agent
    Default_Data_Loader --> Qdrant_Vector_Store
    Extracting_Embedding --> Merge
    Window_Buffer_Memory --> AI_Agent
    Extracting_Embedding1 --> Merge
    Call_n8n_Workflow_Tool --> AI_Agent
    Execute_Workflow_Trigger --> Embedding_Recommendation_Request_with_Open_AI
    Execute_Workflow_Trigger --> Embedding_Anti_Recommendation_Request_with_Open_AI
    When_chat_message_received --> AI_Agent
    Calling_Qdrant_Recommendation_API --> Retrieving_Recommended_Movies_Meta_Data
    Calling_Qdrant_Recommendation_API --> Split_Out1
    When_clicking__Test_workflow_ --> GitHub
    Selecting_Fields_Relevant_for_Agent --> Aggregate
    Retrieving_Recommended_Movies_Meta_Data --> Split_Out
    Embedding_Recommendation_Request_with_Open_AI --> Extracting_Embedding
    Embedding_Anti_Recommendation_Request_with_Open_AI --> Extracting_Embedding1
```
