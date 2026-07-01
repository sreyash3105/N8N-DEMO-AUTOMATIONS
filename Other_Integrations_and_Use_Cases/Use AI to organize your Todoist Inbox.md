```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Update_priority_in_todoist["fas:fa-cogs Update priority in todoist"]
    Schedule_Trigger(("fas:fa-bolt Schedule Trigger")):::trigger
    Get_inbox_tasks["fas:fa-cogs Get inbox tasks"]
    Your_Projects["fas:fa-cogs Your Projects"]
    Categorize(["fas:fa-robot Categorize"]):::ai
    If_task_is_not_a_subtask["fas:fa-cogs If task is not a subtask"]
    If_other_or_ai_hallucinates["fas:fa-cogs If other or ai hallucinates"]

    Categorize --> If_other_or_ai_hallucinates
    Your_Projects --> Get_inbox_tasks
    Get_inbox_tasks --> If_task_is_not_a_subtask
    Schedule_Trigger --> Your_Projects
    If_task_is_not_a_subtask --> Categorize
    If_other_or_ai_hallucinates --> Update_priority_in_todoist
```
