```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Local_File_Trigger(("Local File Trigger")):::trigger
    Get_Files_and_Folders["Get Files and Folders"]
    Files_and_Folders_to_Array["Files and Folders to Array"]
    Mistral_Cloud_Chat_Model["Mistral Cloud Chat Model"]
    Structured_Output_Parser["Structured Output Parser"]
    Set_Variables["Set Variables"]
    Move_Files_into_Folders["Move Files into Folders"]
    If_Has_Target_Files___{"If Has Target Files..."}:::logic
    Get_Suggestions_to_List["Get Suggestions to List"]
    AI_File_Manager(["AI File Manager"]):::ai

    Set_Variables --> Get_Files_and_Folders
    AI_File_Manager --> Get_Suggestions_to_List
    Local_File_Trigger --> Set_Variables
    Get_Files_and_Folders --> Files_and_Folders_to_Array
    If_Has_Target_Files___ --> AI_File_Manager
    Get_Suggestions_to_List --> Move_Files_into_Folders
    Mistral_Cloud_Chat_Model --> AI_File_Manager
    Structured_Output_Parser --> AI_File_Manager
    Files_and_Folders_to_Array --> If_Has_Target_Files___
```
