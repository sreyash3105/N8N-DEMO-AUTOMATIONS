```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Baserow_Event(("Baserow Event")):::trigger
    Event_Type{"Event Type"}:::logic
    Table_Fields_API["Table Fields API"]
    Get_Prompt_Fields["Get Prompt Fields"]
    Get_Event_Body["Get Event Body"]
    List_Table_API["List Table API"]
    Get_Valid_Rows["Get Valid Rows"]
    Get_File_Data["Get File Data"]
    Extract_from_File["Extract from File"]
    Update_Row["Update Row"]
    Get_Result["Get Result"]
    Loop_Over_Items["Loop Over Items"]
    Row_Reference["Row Reference"]
    Generate_Field_Value(["Generate Field Value"]):::ai
    Get_Row["Get Row"]
    Rows_to_List["Rows to List"]
    Fields_to_Update["Fields to Update"]
    Loop_Over_Items1["Loop Over Items1"]
    Row_Ref["Row Ref"]
    Get_File_Data1["Get File Data1"]
    Extract_from_File1["Extract from File1"]
    Update_Row1["Update Row1"]
    Get_Result1["Get Result1"]
    Generate_Field_Value1(["Generate Field Value1"]):::ai
    Filter_Valid_Rows["Filter Valid Rows"]
    Filter_Valid_Fields["Filter Valid Fields"]
    Event_Ref["Event Ref"]
    Event_Ref1["Event Ref1"]
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    OpenAI_Chat_Model1(["OpenAI Chat Model1"]):::ai

    Get_Row --> Loop_Over_Items1
    Row_Ref --> Get_File_Data1
    Event_Ref --> Filter_Valid_Fields
    Event_Ref1 --> Rows_to_List
    Event_Type --> Event_Ref1
    Event_Type --> Event_Ref
    Event_Type --> Event_Ref
    Get_Result --> Update_Row
    Update_Row --> Loop_Over_Items
    Get_Result1 --> Update_Row1
    Update_Row1 --> Loop_Over_Items1
    Rows_to_List --> Filter_Valid_Rows
    Baserow_Event --> Table_Fields_API
    Get_File_Data --> Extract_from_File
    Row_Reference --> Get_File_Data
    Get_Event_Body --> Event_Type
    Get_File_Data1 --> Extract_from_File1
    Get_Valid_Rows --> Loop_Over_Items
    List_Table_API --> Get_Valid_Rows
    Loop_Over_Items --> Row_Reference
    Fields_to_Update --> Generate_Field_Value1
    Loop_Over_Items1 --> Row_Ref
    Table_Fields_API --> Get_Prompt_Fields
    Extract_from_File --> Generate_Field_Value
    Filter_Valid_Rows --> Get_Row
    Get_Prompt_Fields --> Get_Event_Body
    OpenAI_Chat_Model --> Generate_Field_Value1
    Extract_from_File1 --> Fields_to_Update
    OpenAI_Chat_Model1 --> Generate_Field_Value
    Filter_Valid_Fields --> List_Table_API
    Generate_Field_Value --> Get_Result
    Generate_Field_Value1 --> Get_Result1
```
