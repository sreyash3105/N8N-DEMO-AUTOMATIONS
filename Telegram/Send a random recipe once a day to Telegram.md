```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Cron["fas:fa-clock Cron"]
    Airtable2["fas:fa-robot Airtable2"]
    Set["fas:fa-cogs Set"]
    Recipe_Photo["fab:fa-telegram Recipe Photo"]
    Recipe_URL["fab:fa-telegram Recipe URL"]
    IF{"fas:fa-code-branch IF"}:::logic
    Airtable["fas:fa-robot Airtable"]
    Airtable1["fas:fa-robot Airtable1"]
    Telegram_Recipe_Image["fab:fa-telegram Telegram Recipe Image"]
    Telegram_Recipe_URL["fab:fa-telegram Telegram Recipe URL"]
    Set1["fas:fa-cogs Set1"]
    Get_recipes_from_API["fas:fa-globe Get recipes from API"]
    Get_recipes["fas:fa-globe Get recipes"]
    Telegram_Trigger___people_join_bot(("fab:fa-telegram Telegram Trigger - people join bot")):::trigger
    Telegram___Welcome_Message["fab:fa-telegram Telegram - Welcome Message"]

    IF --> Set1
    Set --> Get_recipes_from_API
    Cron --> Airtable2
    Set1 --> Airtable1
    Airtable --> IF
    Airtable2 --> Set
    Get_recipes --> Telegram_Recipe_Image
    Recipe_Photo --> Recipe_URL
    Get_recipes_from_API --> Recipe_Photo
    Telegram_Recipe_Image --> Telegram_Recipe_URL
    Telegram___Welcome_Message --> Get_recipes
    Telegram_Trigger___people_join_bot --> Airtable
    Telegram_Trigger___people_join_bot --> Telegram___Welcome_Message
```
