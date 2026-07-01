```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Execute_Workflow_(("fas:fa-bolt When clicking 'Execute Workflow'")):::trigger
    Reddit["fas:fa-cogs Reddit"]
    Set["fas:fa-cogs Set"]
    IF{"fas:fa-code-branch IF"}:::logic
    IF1{"fas:fa-code-branch IF1"}:::logic
    Merge["fas:fa-cogs Merge"]
    Merge1["fas:fa-cogs Merge1"]
    SetFinal["fas:fa-cogs SetFinal"]
    OpenAI_Summary(["fas:fa-robot OpenAI Summary"]):::ai
    OpenAI_Classify(["fas:fa-robot OpenAI Classify"]):::ai
    OpenAI_Summary_Backup(["fas:fa-robot OpenAI Summary Backup"]):::ai

    IF --> Set
    IF1 --> OpenAI_Summary_Backup
    IF1 --> Merge1
    Set --> OpenAI_Classify
    Set --> Merge
    Merge --> IF1
    Merge1 --> SetFinal
    Reddit --> IF
    OpenAI_Classify --> Merge
    OpenAI_Summary_Backup --> Merge1
    When_clicking__Execute_Workflow_ --> Reddit
```
