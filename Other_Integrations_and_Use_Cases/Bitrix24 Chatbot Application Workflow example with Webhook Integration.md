```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Bitrix24_Handler(("Bitrix24 Handler")):::trigger
    Credentials["Credentials"]
    Validate_Token{"Validate Token"}:::logic
    Route_Event{"Route Event"}:::logic
    Process_Message["Process Message"]
    Process_Join["Process Join"]
    Process_Install["Process Install"]
    Register_Bot["Register Bot"]
    Send_Message["Send Message"]
    Send_Join_Message["Send Join Message"]
    Process_Delete["Process Delete"]
    Success_Response(("Success Response")):::trigger
    Error_Response(("Error Response")):::trigger

    Credentials --> Validate_Token
    Route_Event --> Process_Message
    Route_Event --> Process_Join
    Route_Event --> Process_Install
    Route_Event --> Process_Delete
    Process_Join --> Send_Join_Message
    Register_Bot --> Success_Response
    Send_Message --> Success_Response
    Process_Delete --> Success_Response
    Validate_Token --> Route_Event
    Validate_Token --> Error_Response
    Process_Install --> Register_Bot
    Process_Message --> Send_Message
    Bitrix24_Handler --> Credentials
    Send_Join_Message --> Success_Response
```
