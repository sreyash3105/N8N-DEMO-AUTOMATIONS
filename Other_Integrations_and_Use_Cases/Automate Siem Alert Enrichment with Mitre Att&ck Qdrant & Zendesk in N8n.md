```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_chat_message_received(("fas:fa-robot When chat message received")):::trigger
    AI_Agent["fas:fa-robot AI Agent"]:::ai
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Split_Out["fas:fa-cogs Split Out"]
    Embeddings_OpenAI1(["fas:fa-robot Embeddings OpenAI1"]):::ai
    Default_Data_Loader["fas:fa-robot Default Data Loader"]
    Token_Splitter1["fas:fa-robot Token Splitter1"]
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    Embeddings_OpenAI2(["fas:fa-robot Embeddings OpenAI2"]):::ai
    Extract_from_File["fas:fa-cogs Extract from File"]
    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    AI_Agent1["fas:fa-robot AI Agent1"]:::ai
    OpenAI_Chat_Model1(["fas:fa-robot OpenAI Chat Model1"]):::ai
    Embeddings_OpenAI(["fas:fa-robot Embeddings OpenAI"]):::ai
    Loop_Over_Items["fas:fa-cogs Loop Over Items"]
    Structured_Output_Parser["fas:fa-robot Structured Output Parser"]
    Pull_Mitre_Data_From_Gdrive["fab:fa-google Pull Mitre Data From Gdrive"]
    Embed_JSON_in_Qdrant_Collection["fas:fa-robot Embed JSON in Qdrant Collection"]
    Query_Qdrant_Vector_Store["fas:fa-robot Query Qdrant Vector Store"]
    Qdrant_Vector_Store_query["fas:fa-robot Qdrant Vector Store query"]
    Get_all_Zendesk_Tickets["fas:fa-cogs Get all Zendesk Tickets"]
    Update_Zendesk_with_Mitre_Data["fas:fa-cogs Update Zendesk with Mitre Data"]
    Move_on_to_next_ticket["fas:fa-cogs Move on to next ticket"]

    AI_Agent1 --> Update_Zendesk_with_Mitre_Data
    Split_Out --> Embed_JSON_in_Qdrant_Collection
    Loop_Over_Items --> AI_Agent1
    Token_Splitter1 --> Default_Data_Loader
    Embeddings_OpenAI --> Qdrant_Vector_Store_query
    Extract_from_File --> Split_Out
    OpenAI_Chat_Model --> AI_Agent
    Embeddings_OpenAI1 --> Embed_JSON_in_Qdrant_Collection
    Embeddings_OpenAI2 --> Query_Qdrant_Vector_Store
    OpenAI_Chat_Model1 --> AI_Agent1
    Default_Data_Loader --> Embed_JSON_in_Qdrant_Collection
    Window_Buffer_Memory --> AI_Agent
    Move_on_to_next_ticket --> Loop_Over_Items
    Get_all_Zendesk_Tickets --> Loop_Over_Items
    Structured_Output_Parser --> AI_Agent1
    Qdrant_Vector_Store_query --> AI_Agent1
    Query_Qdrant_Vector_Store --> AI_Agent
    When_chat_message_received --> AI_Agent
    Pull_Mitre_Data_From_Gdrive --> Extract_from_File
    Update_Zendesk_with_Mitre_Data --> Move_on_to_next_ticket
    When_clicking__Test_workflow_ --> Pull_Mitre_Data_From_Gdrive
```
