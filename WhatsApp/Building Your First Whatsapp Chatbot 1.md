```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    WhatsApp_Trigger(("fab:fa-whatsapp WhatsApp Trigger")):::trigger
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    Vector_Store_Tool["fas:fa-robot Vector Store Tool"]
    Embeddings_OpenAI(["fas:fa-robot Embeddings OpenAI"]):::ai
    OpenAI_Chat_Model1(["fas:fa-robot OpenAI Chat Model1"]):::ai
    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Embeddings_OpenAI1(["fas:fa-robot Embeddings OpenAI1"]):::ai
    Default_Data_Loader["fas:fa-robot Default Data Loader"]
    Recursive_Character_Text_Splitter["fas:fa-robot Recursive Character Text Splitter"]
    Extract_from_File["fas:fa-cogs Extract from File"]
    get_Product_Brochure["fas:fa-globe get Product Brochure"]
    Reply_To_User["fab:fa-whatsapp Reply To User"]
    Reply_To_User1["fab:fa-whatsapp Reply To User1"]
    Product_Catalogue[("fas:fa-robot Product Catalogue")]
    Create_Product_Catalogue[("fas:fa-robot Create Product Catalogue")]
    Handle_Message_Types{"fas:fa-code-branch Handle Message Types"}:::logic
    AI_Sales_Agent["fas:fa-robot AI Sales Agent"]:::ai

    AI_Sales_Agent --> Reply_To_User
    WhatsApp_Trigger --> Handle_Message_Types
    Embeddings_OpenAI --> Product_Catalogue
    Extract_from_File --> Create_Product_Catalogue
    OpenAI_Chat_Model --> AI_Sales_Agent
    Product_Catalogue --> Vector_Store_Tool
    Vector_Store_Tool --> AI_Sales_Agent
    Embeddings_OpenAI1 --> Create_Product_Catalogue
    OpenAI_Chat_Model1 --> Vector_Store_Tool
    Default_Data_Loader --> Create_Product_Catalogue
    Handle_Message_Types --> AI_Sales_Agent
    Handle_Message_Types --> Reply_To_User1
    Window_Buffer_Memory --> AI_Sales_Agent
    get_Product_Brochure --> Extract_from_File
    Recursive_Character_Text_Splitter --> Default_Data_Loader
    When_clicking__Test_workflow_ --> get_Product_Brochure
```
