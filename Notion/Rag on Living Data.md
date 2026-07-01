```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Embeddings_OpenAI(["fas:fa-robot Embeddings OpenAI"]):::ai
    Token_Splitter["fas:fa-robot Token Splitter"]
    Loop_Over_Items["fas:fa-cogs Loop Over Items"]
    Question_and_Answer_Chain["fas:fa-robot Question and Answer Chain"]
    Vector_Store_Retriever["fas:fa-robot Vector Store Retriever"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    When_chat_message_received(("fas:fa-robot When chat message received")):::trigger
    Schedule_Trigger(("fas:fa-bolt Schedule Trigger")):::trigger
    Limit["fas:fa-cogs Limit"]
    Limit1["fas:fa-cogs Limit1"]
    Delete_old_embeddings_if_exist["fas:fa-database Delete old embeddings if exist"]
    Get_page_blocks["fas:fa-cogs Get page blocks"]
    Default_Data_Loader["fas:fa-robot Default Data Loader"]
    Input_Reference["fas:fa-cogs Input Reference"]
    Notion_Trigger(("fas:fa-bolt Notion Trigger")):::trigger
    Get_updated_pages["fas:fa-cogs Get updated pages"]
    Supabase_Vector_Store1["fas:fa-database Supabase Vector Store1"]
    Supabase_Vector_Store["fas:fa-database Supabase Vector Store"]
    Concatenate_to_single_string["fas:fa-cogs Concatenate to single string"]

    Limit --> Get_page_blocks
    Limit1 --> Loop_Over_Items
    Notion_Trigger --> Input_Reference
    Token_Splitter --> Default_Data_Loader
    Get_page_blocks --> Concatenate_to_single_string
    Input_Reference --> Loop_Over_Items
    Loop_Over_Items --> Delete_old_embeddings_if_exist
    Schedule_Trigger --> Get_updated_pages
    Embeddings_OpenAI --> Supabase_Vector_Store
    Embeddings_OpenAI --> Supabase_Vector_Store1
    Get_updated_pages --> Input_Reference
    OpenAI_Chat_Model --> Question_and_Answer_Chain
    Default_Data_Loader --> Supabase_Vector_Store
    Supabase_Vector_Store --> Limit1
    Supabase_Vector_Store1 --> Vector_Store_Retriever
    Vector_Store_Retriever --> Question_and_Answer_Chain
    When_chat_message_received --> Question_and_Answer_Chain
    Concatenate_to_single_string --> Supabase_Vector_Store
    Delete_old_embeddings_if_exist --> Limit
```
