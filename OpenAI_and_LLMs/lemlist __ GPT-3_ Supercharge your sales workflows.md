```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Lemlist___Unsubscribe["Lemlist - Unsubscribe"]
    follow_up_task["follow up task"]
    Switch{"Switch"}:::logic
    Merge["Merge"]
    lemlist___Mark_as_interested["lemlist - Mark as interested"]
    HubSpot___Create_Deal["HubSpot - Create Deal"]
    HubSpot___Get_contact_ID["HubSpot - Get contact ID"]
    Slack["Slack"]
    HubSpot___Get_contact_ID1["HubSpot - Get contact ID1"]
    Slack1["Slack1"]
    Lemlist___Lead_Replied(("Lemlist - Lead Replied")):::trigger
    OpenAI(["OpenAI"]):::ai

    Merge --> Switch
    OpenAI --> Merge
    Switch --> Lemlist___Unsubscribe
    Switch --> lemlist___Mark_as_interested
    Switch --> HubSpot___Get_contact_ID
    Switch --> HubSpot___Get_contact_ID1
    Switch --> Slack1
    HubSpot___Create_Deal --> Slack
    Lemlist___Lead_Replied --> OpenAI
    Lemlist___Lead_Replied --> Merge
    HubSpot___Get_contact_ID --> HubSpot___Create_Deal
    HubSpot___Get_contact_ID1 --> follow_up_task
```
