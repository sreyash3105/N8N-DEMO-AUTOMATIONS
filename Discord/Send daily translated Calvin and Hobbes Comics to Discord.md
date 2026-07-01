```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Schedule_Trigger(("fas:fa-bolt Schedule Trigger")):::trigger
    OpenAI(["fas:fa-robot OpenAI"]):::ai
    param["fas:fa-cogs param"]
    Discord["fas:fa-cogs Discord"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Information_Extractor["fas:fa-robot Information Extractor"]
    HTTP_Request["fas:fa-globe HTTP Request"]

    param --> HTTP_Request
    OpenAI --> Discord
    HTTP_Request --> Information_Extractor
    Schedule_Trigger --> param
    OpenAI_Chat_Model --> Information_Extractor
    Information_Extractor --> OpenAI
```
