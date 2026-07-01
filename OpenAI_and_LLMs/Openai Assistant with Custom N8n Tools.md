```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    On_new_manual_Chat_Message(("fas:fa-robot On new manual Chat Message")):::trigger
    OpenAI_Assistant(["fas:fa-robot OpenAI Assistant"]):::ai
    Execute_Workflow_Trigger(("fas:fa-bolt Execute Workflow Trigger")):::trigger
    Mapping_data["fas:fa-cogs Mapping data"]
    List_countries_{"fas:fa-code-branch List countries?"}:::logic
    Mapping_data1["fas:fa-cogs Mapping data1"]
    Return_country_list["fas:fa-cogs Return country list"]
    Return_specific_capital["fas:fa-cogs Return specific capital"]
    Tool_to_call_the_workflow_below["fas:fa-robot Tool to call the workflow below"]
    Concatenate_country_names["fas:fa-cogs Concatenate country names"]
    Get_the_matching_country_s_details["fas:fa-cogs Get the matching country's details"]
    Tool__Get_current_date_and_time["fas:fa-robot Tool: Get current date and time"]

    Mapping_data --> Concatenate_country_names
    Mapping_data1 --> Get_the_matching_country_s_details
    List_countries_ --> Mapping_data
    List_countries_ --> Get_the_matching_country_s_details
    Execute_Workflow_Trigger --> List_countries_
    Concatenate_country_names --> Return_country_list
    On_new_manual_Chat_Message --> OpenAI_Assistant
    Tool_to_call_the_workflow_below --> OpenAI_Assistant
    Tool__Get_current_date_and_time --> OpenAI_Assistant
    Get_the_matching_country_s_details --> Return_specific_capital
```
