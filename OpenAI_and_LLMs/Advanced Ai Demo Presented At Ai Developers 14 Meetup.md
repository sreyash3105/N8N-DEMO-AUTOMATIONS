```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Send_message["fab:fa-slack Send message"]
    Execute_JavaScript["fas:fa-cogs Execute JavaScript"]
    Recursive_Character_Text_Splitter["fas:fa-robot Recursive Character Text Splitter"]
    Embeddings_OpenAI(["fas:fa-robot Embeddings OpenAI"]):::ai
    Default_Data_Loader["fas:fa-robot Default Data Loader"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Embeddings_OpenAI2(["fas:fa-robot Embeddings OpenAI2"]):::ai
    Vector_Store_Retriever["fas:fa-robot Vector Store Retriever"]
    Download_PDF["fas:fa-file-pdf Download PDF"]
    PDFs_to_download["fas:fa-file-pdf PDFs to download"]
    Read_Pinecone_Vector_Store["fas:fa-robot Read Pinecone Vector Store"]
    Question_and_Answer_Chain["fas:fa-robot Question and Answer Chain"]
    Anthropic_Chat_Model["fas:fa-robot Anthropic Chat Model"]
    Get_calendar_availability["fas:fa-robot Get calendar availability"]
    Appointment_booking_agent["fas:fa-robot Appointment booking agent"]:::ai
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    Insert_into_Pinecone_vector_store["fas:fa-robot Insert into Pinecone vector store"]
    Book_appointment["fas:fa-robot Book appointment"]
    When_chat_message_received(("fas:fa-robot When chat message received")):::trigger
    OpenAI_Chat_Model1(["fas:fa-robot OpenAI Chat Model1"]):::ai
    Add_automation_label["fas:fa-envelope Add automation label"]
    On_new_email_to_nathan_s_inbox(("fas:fa-envelope On new email to nathan's inbox")):::trigger
    Add_music_label["fas:fa-envelope Add music label"]
    Assign_label_with_AI{"fas:fa-robot Assign label with AI"}:::logic
    Webhook(("fas:fa-bolt Webhook")):::trigger
    Whether_email_contains_n8n{"fas:fa-code-branch Whether email contains n8n"}:::logic

    Webhook --> Whether_email_contains_n8n
    Download_PDF --> Insert_into_Pinecone_vector_store
    Book_appointment --> Appointment_booking_agent
    PDFs_to_download --> Download_PDF
    Embeddings_OpenAI --> Insert_into_Pinecone_vector_store
    OpenAI_Chat_Model --> Question_and_Answer_Chain
    Embeddings_OpenAI2 --> Read_Pinecone_Vector_Store
    OpenAI_Chat_Model1 --> Assign_label_with_AI
    Default_Data_Loader --> Insert_into_Pinecone_vector_store
    Anthropic_Chat_Model --> Appointment_booking_agent
    Assign_label_with_AI --> Add_automation_label
    Assign_label_with_AI --> Add_music_label
    Window_Buffer_Memory --> Appointment_booking_agent
    Vector_Store_Retriever --> Question_and_Answer_Chain
    Get_calendar_availability --> Appointment_booking_agent
    Read_Pinecone_Vector_Store --> Vector_Store_Retriever
    When_chat_message_received --> Question_and_Answer_Chain
    Whether_email_contains_n8n --> Execute_JavaScript
    Whether_email_contains_n8n --> Send_message
    On_new_email_to_nathan_s_inbox --> Assign_label_with_AI
    Recursive_Character_Text_Splitter --> Default_Data_Loader
```
