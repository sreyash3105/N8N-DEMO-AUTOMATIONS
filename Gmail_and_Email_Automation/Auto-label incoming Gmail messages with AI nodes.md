```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Gmail_trigger(("fas:fa-envelope Gmail trigger")):::trigger
    Get_message_content["fas:fa-envelope Get message content"]
    Set_label_values["fas:fa-cogs Set label values"]
    Get_all_labels["fas:fa-envelope Get all labels"]
    Split_out_assigned_labels["fas:fa-cogs Split out assigned labels"]
    Merge_corresponding_labels["fas:fa-cogs Merge corresponding labels"]
    Aggregate_label_IDs["fas:fa-cogs Aggregate label IDs"]
    Add_labels_to_message["fas:fa-envelope Add labels to message"]
    Assign_labels_for_message(["fas:fa-robot Assign labels for message"]):::ai
    JSON_Parser["fas:fa-robot JSON Parser"]
    OpenAI_Chat(["fas:fa-robot OpenAI Chat"]):::ai

    JSON_Parser --> Assign_labels_for_message
    OpenAI_Chat --> Assign_labels_for_message
    Gmail_trigger --> Get_message_content
    Get_all_labels --> Merge_corresponding_labels
    Set_label_values --> Get_all_labels
    Set_label_values --> Split_out_assigned_labels
    Aggregate_label_IDs --> Add_labels_to_message
    Get_message_content --> Assign_labels_for_message
    Assign_labels_for_message --> Set_label_values
    Split_out_assigned_labels --> Merge_corresponding_labels
    Merge_corresponding_labels --> Aggregate_label_IDs
```
