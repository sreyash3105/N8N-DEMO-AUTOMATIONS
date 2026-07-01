```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    No_Operation__do_nothing["fas:fa-cogs No Operation, do nothing"]
    Add_to_Messages_Stack["fas:fa-cogs Add to Messages Stack"]
    Should_Continue_{"fas:fa-code-branch Should Continue?"}:::logic
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    Twilio_Trigger(("fas:fa-bolt Twilio Trigger")):::trigger
    Get_Latest_Message_Stack["fas:fa-cogs Get Latest Message Stack"]
    Send_Reply["fas:fa-cogs Send Reply"]
    Wait_5_seconds["fas:fa-robot Wait 5 seconds"]
    Get_Chat_History[("fas:fa-robot Get Chat History")]
    Window_Buffer_Memory1[("fas:fa-robot Window Buffer Memory1")]
    Get_Messages_Buffer["fas:fa-cogs Get Messages Buffer"]
    AI_Agent["fas:fa-robot AI Agent"]:::ai

    AI_Agent --> Send_Reply
    Twilio_Trigger --> Add_to_Messages_Stack
    Twilio_Trigger --> Wait_5_seconds
    Wait_5_seconds --> Get_Latest_Message_Stack
    Get_Chat_History --> Get_Messages_Buffer
    Should_Continue_ --> Get_Chat_History
    Should_Continue_ --> No_Operation__do_nothing
    OpenAI_Chat_Model --> AI_Agent
    Get_Messages_Buffer --> AI_Agent
    Window_Buffer_Memory --> AI_Agent
    Window_Buffer_Memory1 --> Get_Chat_History
    Get_Latest_Message_Stack --> Should_Continue_
```
