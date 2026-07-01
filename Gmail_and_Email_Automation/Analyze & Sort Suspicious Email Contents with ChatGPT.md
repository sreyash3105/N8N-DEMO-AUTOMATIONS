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
    Analyze_Email_with_ChatGPT(["fas:fa-robot Analyze Email with ChatGPT"]):::ai
    Create_Potentially_Malicious_Ticket["fas:fa-cogs Create Potentially Malicious Ticket"]
    Create_Potentially_Benign_Ticket["fas:fa-cogs Create Potentially Benign Ticket"]
    Rename_Screenshot["fas:fa-cogs Rename Screenshot"]
    Set_Jira_ID["fas:fa-cogs Set Jira ID"]
    Upload_Screenshot_of_Email_to_Jira["fas:fa-cogs Upload Screenshot of Email to Jira"]
    Upload_Email_Body_to_Jira["fas:fa-cogs Upload Email Body to Jira"]
    Convert_Email_Body_to_File["fas:fa-cogs Convert Email Body to File"]
    Set_Email_Variables["fas:fa-cogs Set Email Variables"]
    Rename_Email_Body_Screenshot["fas:fa-cogs Rename Email Body Screenshot"]
    Check_if_Malicious{"fas:fa-code-branch Check if Malicious"}:::logic

    Set_Jira_ID --> Rename_Screenshot
    Gmail_Trigger --> Set_Gmail_Variables
    Format_Headers --> Set_Outlook_Variables
    Screenshot_HTML --> Retrieve_Screenshot
    Rename_Screenshot --> Upload_Screenshot_of_Email_to_Jira
    Check_if_Malicious --> Create_Potentially_Malicious_Ticket
    Check_if_Malicious --> Create_Potentially_Benign_Ticket
    Retrieve_Screenshot --> Analyze_Email_with_ChatGPT
    Set_Email_Variables --> Convert_Email_Body_to_File
    Set_Gmail_Variables --> Set_Email_Variables
    Set_Outlook_Variables --> Set_Email_Variables
    Microsoft_Outlook_Trigger --> Retrieve_Headers_of_Email
    Retrieve_Headers_of_Email --> Format_Headers
    Analyze_Email_with_ChatGPT --> Check_if_Malicious
    Convert_Email_Body_to_File --> Screenshot_HTML
    Rename_Email_Body_Screenshot --> Upload_Email_Body_to_Jira
    Create_Potentially_Benign_Ticket --> Set_Jira_ID
    Upload_Screenshot_of_Email_to_Jira --> Rename_Email_Body_Screenshot
    Create_Potentially_Malicious_Ticket --> Set_Jira_ID
```
