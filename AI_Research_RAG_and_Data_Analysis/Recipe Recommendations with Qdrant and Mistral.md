```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking 'Test workflow'")):::trigger
    Get_This_Week_s_Menu["fas:fa-globe Get This Week's Menu"]
    Extract_Available_Courses["fas:fa-cogs Extract Available Courses"]
    Extract_Server_Data["fas:fa-cogs Extract Server Data"]
    Get_Course_Metadata["fas:fa-cogs Get Course Metadata"]
    Get_Recipe["fas:fa-globe Get Recipe"]
    Embeddings_Mistral_Cloud["fas:fa-robot Embeddings Mistral Cloud"]
    Default_Data_Loader["fas:fa-robot Default Data Loader"]
    Merge_Course___Recipe["fas:fa-cogs Merge Course & Recipe"]
    Prepare_Documents["fas:fa-cogs Prepare Documents"]
    Recursive_Character_Text_Splitter["fas:fa-robot Recursive Character Text Splitter"]
    Chat_Trigger(("fas:fa-robot Chat Trigger")):::trigger
    Extract_Recipe_Details["fas:fa-cogs Extract Recipe Details"]
    Qdrant_Recommend_API["fas:fa-robot Qdrant Recommend API"]
    Execute_Workflow_Trigger(("fas:fa-bolt Execute Workflow Trigger")):::trigger
    Mistral_Cloud_Chat_Model["fas:fa-robot Mistral Cloud Chat Model"]
    Get_Tool_Response["fas:fa-cogs Get Tool Response"]
    Wait_for_Rate_Limits["fas:fa-robot Wait for Rate Limits"]
    Get_Mistral_Embeddings["fas:fa-globe Get Mistral Embeddings"]
    Use_Qdrant_Recommend_API["fas:fa-globe Use Qdrant Recommend API"]
    Get_Recipes_From_DB["fas:fa-cogs Get Recipes From DB"]
    Save_Recipes_to_DB["fas:fa-cogs Save Recipes to DB"]
    AI_Agent["fas:fa-robot AI Agent"]:::ai
    Qdrant_Vector_Store["fas:fa-robot Qdrant Vector Store"]

    Get_Recipe --> Extract_Recipe_Details
    Chat_Trigger --> AI_Agent
    Prepare_Documents --> Qdrant_Vector_Store
    Prepare_Documents --> Save_Recipes_to_DB
    Default_Data_Loader --> Qdrant_Vector_Store
    Extract_Server_Data --> Extract_Available_Courses
    Get_Course_Metadata --> Merge_Course___Recipe
    Get_Recipes_From_DB --> Get_Tool_Response
    Get_This_Week_s_Menu --> Extract_Server_Data
    Qdrant_Recommend_API --> AI_Agent
    Wait_for_Rate_Limits --> Get_Mistral_Embeddings
    Merge_Course___Recipe --> Prepare_Documents
    Extract_Recipe_Details --> Merge_Course___Recipe
    Get_Mistral_Embeddings --> Use_Qdrant_Recommend_API
    Embeddings_Mistral_Cloud --> Qdrant_Vector_Store
    Execute_Workflow_Trigger --> Wait_for_Rate_Limits
    Mistral_Cloud_Chat_Model --> AI_Agent
    Use_Qdrant_Recommend_API --> Get_Recipes_From_DB
    Extract_Available_Courses --> Get_Course_Metadata
    Extract_Available_Courses --> Get_Recipe
    When_clicking__Test_workflow_ --> Get_This_Week_s_Menu
    Recursive_Character_Text_Splitter --> Default_Data_Loader
```
