```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    OpenAI_Chat_Model1(["OpenAI Chat Model1"]):::ai
    Activity_Tool["Activity Tool"]
    Set_ChatInput1["Set ChatInput1"]
    AI_Agent1["AI Agent1"]:::ai
    Set_ChatInput["Set ChatInput"]
    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    AI_Agent["AI Agent"]:::ai
    Webscraper_Tool["Webscraper Tool"]

    Activity_Tool --> AI_Agent1
    Set_ChatInput --> AI_Agent
    Set_ChatInput1 --> AI_Agent1
    Webscraper_Tool --> AI_Agent
    OpenAI_Chat_Model --> AI_Agent
    OpenAI_Chat_Model1 --> AI_Agent1
    When_clicking__Test_workflow_ --> Set_ChatInput
    When_clicking__Test_workflow_ --> Set_ChatInput1
```
