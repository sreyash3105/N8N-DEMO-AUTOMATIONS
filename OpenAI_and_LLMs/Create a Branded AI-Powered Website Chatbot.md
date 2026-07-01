```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Window_Buffer_Memory[("Window Buffer Memory")]
    Respond_to_Webhook(("Respond to Webhook")):::trigger
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    Make_Appointment["Make Appointment"]
    Execute_Workflow_Trigger(("Execute Workflow Trigger")):::trigger
    varResponse["varResponse"]
    freeTimeSlots["freeTimeSlots"]
    Get_Events["Get Events"]
    Get_Availability["Get Availability"]
    Send_Message["Send Message"]
    Chat_Trigger(("Chat Trigger")):::trigger
    Switch{"Switch"}:::logic
    varMessageResponse["varMessageResponse"]
    Send_Message1["Send Message1"]
    AI_Agent["AI Agent"]:::ai
    If{"If"}:::logic
    Respond_With_Initial_Message(("Respond With Initial Message")):::trigger

    If --> AI_Agent
    If --> Respond_With_Initial_Message
    Switch --> Get_Events
    Switch --> Send_Message1
    AI_Agent --> Respond_to_Webhook
    Get_Events --> freeTimeSlots
    Chat_Trigger --> If
    Send_Message --> AI_Agent
    Send_Message1 --> varMessageResponse
    freeTimeSlots --> varResponse
    Get_Availability --> AI_Agent
    Make_Appointment --> AI_Agent
    OpenAI_Chat_Model --> AI_Agent
    Window_Buffer_Memory --> AI_Agent
    Execute_Workflow_Trigger --> Switch
```
