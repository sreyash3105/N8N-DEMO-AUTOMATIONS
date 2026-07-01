```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    If_params_correct{"fas:fa-code-branch If params correct"}:::logic
    Respond_to_Webhook(("fas:fa-bolt Respond to Webhook")):::trigger
    Webhook(("fas:fa-bolt Webhook")):::trigger
    Generate_voice["fas:fa-globe Generate voice"]
    Error(("fas:fa-bolt Error")):::trigger

    Webhook --> If_params_correct
    Generate_voice --> Respond_to_Webhook
    If_params_correct --> Generate_voice
    If_params_correct --> Error
```
