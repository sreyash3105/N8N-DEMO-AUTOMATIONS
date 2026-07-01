```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Local_File_Trigger(("fas:fa-bolt Local File Trigger")):::trigger
    When_clicking__Test_workflow_(("fas:fa-bolt When clicking 'Test workflow'")):::trigger
    Set_Variables["fas:fa-cogs Set Variables"]
    Read_File["fas:fa-cogs Read File"]
    Embeddings_Mistral_Cloud["fas:fa-robot Embeddings Mistral Cloud"]
    Default_Data_Loader["fas:fa-robot Default Data Loader"]
    Recursive_Character_Text_Splitter["fas:fa-robot Recursive Character Text Splitter"]
    Prepare_Embedding_Document["fas:fa-cogs Prepare Embedding Document"]
    Chat_Trigger(("fas:fa-robot Chat Trigger")):::trigger
    Question_and_Answer_Chain["fas:fa-robot Question and Answer Chain"]
    Mistral_Cloud_Chat_Model["fas:fa-robot Mistral Cloud Chat Model"]
    Vector_Store_Retriever["fas:fa-robot Vector Store Retriever"]
    Embeddings_Mistral_Cloud1["fas:fa-robot Embeddings Mistral Cloud1"]
    Remap_for_File_Added_Flow["fas:fa-cogs Remap for File_Added Flow"]
    Search_For_Existing_Point["fas:fa-globe Search For Existing Point"]
    Has_Existing_Point_{"fas:fa-code-branch Has Existing Point?"}:::logic
    Delete_Existing_Point["fas:fa-globe Delete Existing Point"]
    Search_For_Existing_Point1["fas:fa-globe Search For Existing Point1"]
    Has_Existing_Point_1{"fas:fa-code-branch Has Existing Point?1"}:::logic
    Delete_Existing_Point1["fas:fa-globe Delete Existing Point1"]
    Handle_File_Event{"fas:fa-code-branch Handle File Event"}:::logic
    Qdrant_Vector_Store["fas:fa-robot Qdrant Vector Store"]
    Qdrant_Vector_Store1["fas:fa-robot Qdrant Vector Store1"]

    Read_File --> Prepare_Embedding_Document
    Chat_Trigger --> Question_and_Answer_Chain
    Set_Variables --> Handle_File_Event
    Handle_File_Event --> Search_For_Existing_Point
    Handle_File_Event --> Search_For_Existing_Point1
    Handle_File_Event --> Read_File
    Local_File_Trigger --> Set_Variables
    Default_Data_Loader --> Qdrant_Vector_Store
    Has_Existing_Point_ --> Delete_Existing_Point1
    Has_Existing_Point_1 --> Delete_Existing_Point
    Qdrant_Vector_Store1 --> Vector_Store_Retriever
    Delete_Existing_Point --> Remap_for_File_Added_Flow
    Vector_Store_Retriever --> Question_and_Answer_Chain
    Embeddings_Mistral_Cloud --> Qdrant_Vector_Store
    Mistral_Cloud_Chat_Model --> Question_and_Answer_Chain
    Embeddings_Mistral_Cloud1 --> Qdrant_Vector_Store1
    Remap_for_File_Added_Flow --> Read_File
    Search_For_Existing_Point --> Has_Existing_Point_
    Prepare_Embedding_Document --> Qdrant_Vector_Store
    Search_For_Existing_Point1 --> Has_Existing_Point_1
    When_clicking__Test_workflow_ --> Set_Variables
    Recursive_Character_Text_Splitter --> Default_Data_Loader
```
