```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    On_clicking__execute_(("On clicking 'execute'")):::trigger
    FunctionItem["FunctionItem"]
    HTTP_Request["HTTP Request"]
    Airtable["Airtable"]
    Set["Set"]

    Set --> Airtable
    FunctionItem --> HTTP_Request
    HTTP_Request --> Set
    On_clicking__execute_ --> FunctionItem
```
