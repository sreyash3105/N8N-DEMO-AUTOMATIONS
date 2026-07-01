```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Webhook(("fas:fa-bolt Webhook")):::trigger
    Code["fas:fa-cogs Code"]
    Split_Out1["fas:fa-cogs Split Out1"]
    OpenAI_Chat_Model1(["fas:fa-robot OpenAI Chat Model1"]):::ai
    Get_Changes1["fas:fa-globe Get Changes1"]
    Skip_File_Change1{"fas:fa-code-branch Skip File Change1"}:::logic
    Parse_Last_Diff_Line1["fas:fa-cogs Parse Last Diff Line1"]
    Post_Discussions1["fas:fa-globe Post Discussions1"]
    Need_Review1{"fas:fa-code-branch Need Review1"}:::logic
    Basic_LLM_Chain1(["fas:fa-robot Basic LLM Chain1"]):::ai

    Code --> Basic_LLM_Chain1
    Webhook --> Need_Review1
    Split_Out1 --> Skip_File_Change1
    Get_Changes1 --> Split_Out1
    Need_Review1 --> Get_Changes1
    Basic_LLM_Chain1 --> Post_Discussions1
    Skip_File_Change1 --> Parse_Last_Diff_Line1
    OpenAI_Chat_Model1 --> Basic_LLM_Chain1
    Parse_Last_Diff_Line1 --> Code
```
