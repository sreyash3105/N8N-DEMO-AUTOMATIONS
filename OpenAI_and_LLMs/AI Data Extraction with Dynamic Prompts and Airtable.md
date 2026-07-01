```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Event_Type{"fas:fa-code-branch Event Type"}:::logic
    Get_Prompt_Fields["fas:fa-cogs Get Prompt Fields"]
    Get_File_Data["fas:fa-globe Get File Data"]
    Extract_from_File["fas:fa-cogs Extract from File"]
    Get_Result["fas:fa-cogs Get Result"]
    Loop_Over_Items["fas:fa-cogs Loop Over Items"]
    Row_Reference["fas:fa-cogs Row Reference"]
    Generate_Field_Value(["fas:fa-robot Generate Field Value"]):::ai
    Fields_to_Update["fas:fa-cogs Fields to Update"]
    Loop_Over_Items1["fas:fa-cogs Loop Over Items1"]
    Row_Ref["fas:fa-cogs Row Ref"]
    Get_File_Data1["fas:fa-globe Get File Data1"]
    Extract_from_File1["fas:fa-cogs Extract from File1"]
    Get_Result1["fas:fa-cogs Get Result1"]
    Generate_Field_Value1(["fas:fa-robot Generate Field Value1"]):::ai
    Filter_Valid_Rows["fas:fa-cogs Filter Valid Rows"]
    Filter_Valid_Fields["fas:fa-cogs Filter Valid Fields"]
    Event_Ref["fas:fa-cogs Event Ref"]
    Event_Ref1["fas:fa-cogs Event Ref1"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    OpenAI_Chat_Model1(["fas:fa-robot OpenAI Chat Model1"]):::ai
    Get_Webhook_Payload["fas:fa-globe Get Webhook Payload"]
    Parse_Event["fas:fa-cogs Parse Event"]
    Get_Table_Schema["fas:fa-robot Get Table Schema"]
    Fetch_Records["fas:fa-robot Fetch Records"]
    Update_Row["fas:fa-robot Update Row"]
    Get_Row["fas:fa-robot Get Row"]
    Add_Row_ID_to_Payload["fas:fa-cogs Add Row ID to Payload"]
    Update_Record["fas:fa-robot Update Record"]
    Airtable_Webhook(("fas:fa-bolt Airtable Webhook")):::trigger
    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Set_Airtable_Vars["fas:fa-cogs Set Airtable Vars"]
    Get_Table_Schema1["fas:fa-robot Get Table Schema1"]
    Get__Input__Field["fas:fa-cogs Get 'Input' Field"]
    RecordsChanged_Webhook["fas:fa-globe RecordsChanged Webhook"]
    FieldsChanged_Webhook["fas:fa-globe FieldsChanged Webhook"]

    Get_Row --> Filter_Valid_Rows
    Row_Ref --> Get_File_Data1
    Event_Ref --> Filter_Valid_Fields
    Event_Ref1 --> Get_Row
    Event_Type --> Event_Ref1
    Event_Type --> Event_Ref
    Event_Type --> Event_Ref
    Get_Result --> Update_Row
    Update_Row --> Loop_Over_Items
    Get_Result1 --> Add_Row_ID_to_Payload
    Parse_Event --> Event_Type
    Fetch_Records --> Loop_Over_Items
    Get_File_Data --> Extract_from_File
    Row_Reference --> Get_File_Data
    Update_Record --> Loop_Over_Items1
    Get_File_Data1 --> Extract_from_File1
    Loop_Over_Items --> Row_Reference
    Airtable_Webhook --> Get_Table_Schema
    Fields_to_Update --> Generate_Field_Value1
    Get_Table_Schema --> Get_Prompt_Fields
    Loop_Over_Items1 --> Row_Ref
    Extract_from_File --> Generate_Field_Value
    Filter_Valid_Rows --> Loop_Over_Items1
    Get__Input__Field --> RecordsChanged_Webhook
    Get_Prompt_Fields --> Get_Webhook_Payload
    Get_Table_Schema1 --> Get__Input__Field
    OpenAI_Chat_Model --> Generate_Field_Value1
    Set_Airtable_Vars --> Get_Table_Schema1
    Set_Airtable_Vars --> FieldsChanged_Webhook
    Extract_from_File1 --> Fields_to_Update
    OpenAI_Chat_Model1 --> Generate_Field_Value
    Filter_Valid_Fields --> Fetch_Records
    Get_Webhook_Payload --> Parse_Event
    Generate_Field_Value --> Get_Result
    Add_Row_ID_to_Payload --> Update_Record
    Generate_Field_Value1 --> Get_Result1
    When_clicking__Test_workflow_ --> Set_Airtable_Vars
```
