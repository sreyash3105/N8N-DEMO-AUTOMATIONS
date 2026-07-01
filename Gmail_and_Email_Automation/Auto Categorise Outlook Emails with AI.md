```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    Ollama_Chat_Model1["Ollama Chat Model1"]
    Microsoft_Outlook10["Microsoft Outlook10"]
    Microsoft_Outlook12["Microsoft Outlook12"]
    Loop_Over_Items1["Loop Over Items1"]
    Microsoft_Outlook13["Microsoft Outlook13"]
    Microsoft_Outlook15["Microsoft Outlook15"]
    Microsoft_Outlook16["Microsoft Outlook16"]
    Microsoft_Outlook17["Microsoft Outlook17"]
    Microsoft_Outlook18["Microsoft Outlook18"]
    Microsoft_Outlook19["Microsoft Outlook19"]
    Markdown1["Markdown1"]
    varEmal1["varEmal1"]
    Microsoft_Outlook20["Microsoft Outlook20"]
    Microsoft_Outlook21["Microsoft Outlook21"]
    Filter1["Filter1"]
    If1{"If1"}:::logic
    Microsoft_Outlook22["Microsoft Outlook22"]
    Catch_Errors1["Catch Errors1"]
    varJSON1["varJSON1"]
    Microsoft_Outlook23["Microsoft Outlook23"]
    varID___Category1["varID & Category1"]
    Microsoft_Outlook_Move_Message1["Microsoft Outlook Move Message1"]
    AI_Agent1["AI Agent1"]:::ai
    Merge1["Merge1"]
    Switch1{"Switch1"}:::logic

    If1 --> Microsoft_Outlook_Move_Message1
    If1 --> Merge1
    Merge1 --> Loop_Over_Items1
    Filter1 --> Loop_Over_Items1
    Switch1 --> Microsoft_Outlook12
    Switch1 --> Microsoft_Outlook13
    Switch1 --> Microsoft_Outlook18
    Switch1 --> Microsoft_Outlook16
    Switch1 --> Microsoft_Outlook20
    Switch1 --> Microsoft_Outlook22
    Switch1 --> Microsoft_Outlook21
    varEmal1 --> varID___Category1
    varJSON1 --> Switch1
    varJSON1 --> Catch_Errors1
    AI_Agent1 --> varJSON1
    Markdown1 --> varEmal1
    Catch_Errors1 --> Loop_Over_Items1
    Loop_Over_Items1 --> Markdown1
    varID___Category1 --> AI_Agent1
    Ollama_Chat_Model1 --> AI_Agent1
    Microsoft_Outlook10 --> Merge1
    Microsoft_Outlook12 --> Microsoft_Outlook10
    Microsoft_Outlook13 --> Microsoft_Outlook15
    Microsoft_Outlook15 --> Merge1
    Microsoft_Outlook16 --> Microsoft_Outlook17
    Microsoft_Outlook17 --> Merge1
    Microsoft_Outlook18 --> Microsoft_Outlook19
    Microsoft_Outlook19 --> Merge1
    Microsoft_Outlook20 --> If1
    Microsoft_Outlook21 --> Merge1
    Microsoft_Outlook22 --> If1
    Microsoft_Outlook23 --> Filter1
    Microsoft_Outlook_Move_Message1 --> Merge1
    When_clicking__Test_workflow_ --> Microsoft_Outlook23
```
