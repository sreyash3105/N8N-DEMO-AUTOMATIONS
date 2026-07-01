```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    AI_Agent["AI Agent"]:::ai
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    Window_Buffer_Memory[("Window Buffer Memory")]
    Get_Airtable_Record_Data["Get Airtable Record Data"]
    Wait_1_Minute["Wait 1 Minute"]
    Format_Fields["Format Fields"]
    Post_Caption_into_Airtable_Record["Post Caption into Airtable Record"]
    Airtable_Trigger__New_Record(("Airtable Trigger: New Record")):::trigger
    Background_Info["Background Info"]

    AI_Agent --> Format_Fields
    Format_Fields --> Post_Caption_into_Airtable_Record
    Wait_1_Minute --> Get_Airtable_Record_Data
    Background_Info --> AI_Agent
    OpenAI_Chat_Model --> AI_Agent
    Window_Buffer_Memory --> AI_Agent
    Get_Airtable_Record_Data --> AI_Agent
    Airtable_Trigger__New_Record --> Wait_1_Minute
```
