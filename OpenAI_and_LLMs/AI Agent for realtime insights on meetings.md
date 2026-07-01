```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    OpenAI1(["fas:fa-robot OpenAI1"]):::ai
    Insert_Transcription_Part["fas:fa-database Insert Transcription Part"]
    Create_Note["fas:fa-database Create Note"]
    Create_Recall_bot["fas:fa-globe Create Recall bot"]
    Create_OpenAI_thread["fas:fa-globe Create OpenAI thread"]
    Create_data_record["fas:fa-database Create data record"]
    Scenario_1_Start___Edit_Fields["fas:fa-cogs Scenario 1 Start - Edit Fields"]
    Scenario_2_Start___Webhook(("fas:fa-bolt Scenario 2 Start - Webhook")):::trigger
    If_Jimmy_word{"fas:fa-code-branch If Jimmy word"}:::logic

    Create_Note --> OpenAI1
    If_Jimmy_word --> OpenAI1
    Create_Recall_bot --> Create_OpenAI_thread
    Create_OpenAI_thread --> Create_data_record
    Insert_Transcription_Part --> If_Jimmy_word
    Scenario_2_Start___Webhook --> Insert_Transcription_Part
    Scenario_1_Start___Edit_Fields --> Create_Recall_bot
```
