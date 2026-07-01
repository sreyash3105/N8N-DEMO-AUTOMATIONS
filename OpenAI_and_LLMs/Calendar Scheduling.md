```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Gmail_Trigger(("Gmail Trigger")):::trigger
    Chat_OpenAI(["Chat OpenAI"]):::ai
    Workflow_Tool["Workflow Tool"]
    Chat_OpenAI1(["Chat OpenAI1"]):::ai
    Google_Calendar["Google Calendar"]
    Execute_Workflow_Trigger(("Execute Workflow Trigger")):::trigger
    Format_response["Format response"]
    Stringify_Response["Stringify Response"]
    Extract_start__end_and_name["Extract start, end and name"]
    Filter_only_confirmed_and_with_set_time["Filter only confirmed and with set time"]
    Is_appointment_request{"Is appointment request"}:::logic
    Classify_appointment(["Classify appointment"]):::ai
    Structured_Output_Parser["Structured Output Parser"]
    Sort["Sort"]
    Mark_as_read["Mark as read"]
    Send_Reply["Send Reply"]
    Agent["Agent"]:::ai

    Sort --> Format_response
    Agent --> Send_Reply
    Agent --> Mark_as_read
    Chat_OpenAI --> Classify_appointment
    Chat_OpenAI1 --> Agent
    Gmail_Trigger --> Classify_appointment
    Workflow_Tool --> Agent
    Format_response --> Stringify_Response
    Google_Calendar --> Filter_only_confirmed_and_with_set_time
    Classify_appointment --> Is_appointment_request
    Is_appointment_request --> Agent
    Execute_Workflow_Trigger --> Google_Calendar
    Structured_Output_Parser --> Classify_appointment
    Extract_start__end_and_name --> Sort
    Filter_only_confirmed_and_with_set_time --> Extract_start__end_and_name
```
