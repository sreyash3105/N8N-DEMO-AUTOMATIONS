```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Execute_Workflow_Trigger(("Execute Workflow Trigger")):::trigger
    Get_Google_sheet_contents["Get Google sheet contents"]
    Set_Google_Sheet_URL["Set Google Sheet URL"]
    Get_column_names["Get column names"]
    Prepare_output["Prepare output"]
    List_columns_tool["List columns tool"]
    Get_customer_tool["Get customer tool"]
    Get_column_values_tool["Get column values tool"]
    Prepare_column_data["Prepare column data"]
    Filter["Filter"]
    Check_operation{"Check operation"}:::logic
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    Chat_Trigger(("Chat Trigger")):::trigger
    AI_Agent["AI Agent"]:::ai

    Filter --> Prepare_output
    Chat_Trigger --> AI_Agent
    Check_operation --> Get_column_names
    Check_operation --> Prepare_column_data
    Check_operation --> Filter
    Get_column_names --> Prepare_output
    Get_customer_tool --> AI_Agent
    List_columns_tool --> AI_Agent
    OpenAI_Chat_Model --> AI_Agent
    Prepare_column_data --> Prepare_output
    Set_Google_Sheet_URL --> Get_Google_sheet_contents
    Get_column_values_tool --> AI_Agent
    Execute_Workflow_Trigger --> Set_Google_Sheet_URL
    Get_Google_sheet_contents --> Check_operation
```
