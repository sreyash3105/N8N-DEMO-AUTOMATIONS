```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Execute_Workflow_(("When clicking 'Execute Workflow'")):::trigger
    Fetch_essay_list["Fetch essay list"]
    Extract_essay_names["Extract essay names"]
    Fetch_essay_texts["Fetch essay texts"]
    Extract_title["Extract title"]
    Clean_up["Clean up"]
    Split_out_into_items["Split out into items"]
    Limit_to_first_3["Limit to first 3"]
    Default_Data_Loader["Default Data Loader"]
    Recursive_Character_Text_Splitter["Recursive Character Text Splitter"]
    OpenAI_Chat_Model1(["OpenAI Chat Model1"]):::ai
    Merge["Merge"]
    Summarization_Chain["Summarization Chain"]

    Merge --> Clean_up
    Extract_title --> Merge
    Fetch_essay_list --> Extract_essay_names
    Limit_to_first_3 --> Fetch_essay_texts
    Fetch_essay_texts --> Extract_title
    Fetch_essay_texts --> Summarization_Chain
    OpenAI_Chat_Model1 --> Summarization_Chain
    Default_Data_Loader --> Summarization_Chain
    Extract_essay_names --> Split_out_into_items
    Summarization_Chain --> Merge
    Split_out_into_items --> Limit_to_first_3
    When_clicking__Execute_Workflow_ --> Fetch_essay_list
    Recursive_Character_Text_Splitter --> Default_Data_Loader
```
