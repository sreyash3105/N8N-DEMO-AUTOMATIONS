```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Get_RFP_Data["Get RFP Data"]
    Item_List_Output_Parser["Item List Output Parser"]
    For_Each_Question___["For Each Question..."]
    Set_Variables["Set Variables"]
    Create_new_RFP_Response_Document["Create new RFP Response Document"]
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    Send_Chat_Notification["Send Chat Notification"]
    Send_Email_Notification["Send Email Notification"]
    Add_Metadata_to_Response_Doc["Add Metadata to Response Doc"]
    Record_Question___Answer_in_Response_Doc["Record Question & Answer in Response Doc"]
    Answer_Question_with_Context(["Answer Question with Context"]):::ai
    Wait_for_Request(("Wait for Request")):::trigger
    Extract_Questions_From_RFP(["Extract Questions From RFP"]):::ai

    Get_RFP_Data --> Set_Variables
    Set_Variables --> Create_new_RFP_Response_Document
    Wait_for_Request --> Get_RFP_Data
    OpenAI_Chat_Model --> Extract_Questions_From_RFP
    For_Each_Question___ --> Send_Email_Notification
    For_Each_Question___ --> Answer_Question_with_Context
    Item_List_Output_Parser --> Extract_Questions_From_RFP
    Send_Email_Notification --> Send_Chat_Notification
    Extract_Questions_From_RFP --> For_Each_Question___
    Add_Metadata_to_Response_Doc --> Extract_Questions_From_RFP
    Answer_Question_with_Context --> Record_Question___Answer_in_Response_Doc
    Create_new_RFP_Response_Document --> Add_Metadata_to_Response_Doc
    Record_Question___Answer_in_Response_Doc --> For_Each_Question___
```
