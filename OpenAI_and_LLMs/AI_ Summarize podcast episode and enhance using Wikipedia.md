```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Execute_Workflow_(("When clicking 'Execute Workflow'")):::trigger
    Podcast_Episode_Transcript["Podcast Episode Transcript"]
    Workflow_Input_to_JSON_Document["Workflow Input to JSON Document"]
    Recursive_Character_Text_Splitter["Recursive Character Text Splitter"]
    Topics["Topics"]
    Summarize_Transcript["Summarize Transcript"]
    GPT_4___Extract(["GPT 4 - Extract"]):::ai
    Wikipedia1["Wikipedia1"]
    Send_Digest["Send Digest"]
    Format_topic_text___title["Format topic text & title"]
    Structured_Output_Parser["Structured Output Parser"]
    Extract_Topics___Questions(["Extract Topics & Questions"]):::ai
    GPT3_5___Research(["GPT3.5 - Research"]):::ai
    GPT3_5___Summarize(["GPT3.5 - Summarize"]):::ai
    Research___Explain_Topics["Research & Explain Topics"]:::ai

    Topics --> Research___Explain_Topics
    Wikipedia1 --> Research___Explain_Topics
    GPT_4___Extract --> Extract_Topics___Questions
    GPT3_5___Research --> Research___Explain_Topics
    GPT3_5___Summarize --> Summarize_Transcript
    Summarize_Transcript --> Extract_Topics___Questions
    Structured_Output_Parser --> Extract_Topics___Questions
    Format_topic_text___title --> Send_Digest
    Research___Explain_Topics --> Format_topic_text___title
    Extract_Topics___Questions --> Topics
    Podcast_Episode_Transcript --> Summarize_Transcript
    Workflow_Input_to_JSON_Document --> Summarize_Transcript
    When_clicking__Execute_Workflow_ --> Podcast_Episode_Transcript
    Recursive_Character_Text_Splitter --> Workflow_Input_to_JSON_Document
```
