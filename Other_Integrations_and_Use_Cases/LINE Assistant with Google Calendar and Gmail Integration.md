```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    AI_Agent["AI Agent"]:::ai
    Window_Buffer_Memory[("Window Buffer Memory")]
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    Wikipedia["Wikipedia"]
    OpenAI(["OpenAI"]):::ai
    Switch_Between_Text_and_Others{"Switch Between Text and Others"}:::logic
    Line_Receiving(("Line Receiving")):::trigger
    Error_Handling_from_AI_Response{"Error Handling from AI Response"}:::logic
    Text_Cleansing["Text Cleansing"]
    Line_Answering__Error_Case_["Line Answering (Error Case)"]
    Line_Answering__Ordinary_Case_["Line Answering (Ordinary Case)"]
    Google_Calendar_Create["Google Calendar Create"]
    Google_Calendar_Read["Google Calendar Read"]
    Gmail_Read["Gmail Read"]

    OpenAI --> Error_Handling_from_AI_Response
    AI_Agent --> OpenAI
    Wikipedia --> AI_Agent
    Gmail_Read --> AI_Agent
    Line_Receiving --> Switch_Between_Text_and_Others
    Text_Cleansing --> Line_Answering__Ordinary_Case_
    OpenAI_Chat_Model --> AI_Agent
    Google_Calendar_Read --> AI_Agent
    Window_Buffer_Memory --> AI_Agent
    Google_Calendar_Create --> AI_Agent
    Switch_Between_Text_and_Others --> AI_Agent
    Switch_Between_Text_and_Others --> Line_Answering__Error_Case_
    Error_Handling_from_AI_Response --> Text_Cleansing
    Error_Handling_from_AI_Response --> Line_Answering__Error_Case_
```
