```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Gmail_Trigger(("fas:fa-envelope Gmail Trigger")):::trigger
    Microsoft_Outlook_Trigger(("fas:fa-bolt Microsoft Outlook Trigger")):::trigger
    Screenshot_HTML["fas:fa-globe Screenshot HTML"]
    Retrieve_Screenshot["fas:fa-globe Retrieve Screenshot"]
    Set_Outlook_Variables["fas:fa-cogs Set Outlook Variables"]
    Set_Gmail_Variables["fas:fa-envelope Set Gmail Variables"]
    Retrieve_Headers_of_Email["fas:fa-globe Retrieve Headers of Email"]
    Format_Headers["fas:fa-cogs Format Headers"]
    Set_Email_Variables["fas:fa-cogs Set Email Variables"]
    ChatGPT_Analysis(["fas:fa-robot ChatGPT Analysis"]):::ai
    Create_Jira_Ticket["fas:fa-cogs Create Jira Ticket"]
    Rename_Screenshot["fas:fa-cogs Rename Screenshot"]
    Upload_Screenshot_of_Email_to_Jira["fas:fa-cogs Upload Screenshot of Email to Jira"]

    Gmail_Trigger --> Set_Gmail_Variables
    Format_Headers --> Set_Outlook_Variables
    Screenshot_HTML --> Retrieve_Screenshot
    ChatGPT_Analysis --> Create_Jira_Ticket
    Rename_Screenshot --> Upload_Screenshot_of_Email_to_Jira
    Create_Jira_Ticket --> Rename_Screenshot
    Retrieve_Screenshot --> ChatGPT_Analysis
    Set_Email_Variables --> Screenshot_HTML
    Set_Gmail_Variables --> Set_Email_Variables
    Set_Outlook_Variables --> Set_Email_Variables
    Microsoft_Outlook_Trigger --> Retrieve_Headers_of_Email
    Retrieve_Headers_of_Email --> Format_Headers
```
