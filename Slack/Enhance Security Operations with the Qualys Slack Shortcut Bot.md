```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Parse_Webhook["Parse Webhook"]
    Qualys_Create_Report["Qualys Create Report"]
    Required_Report_Variables["Required Report Variables"]
    Qualys_Start_Vulnerability_Scan["Qualys Start Vulnerability Scan"]
    Scan_Report_Task_Modal["Scan Report Task Modal"]
    Vuln_Scan_Modal["Vuln Scan Modal"]
    Route_Message{"Route Message"}:::logic
    Required_Scan_Variables["Required Scan Variables"]
    Route_Submission{"Route Submission"}:::logic
    Close_Modal_Popup(("Close Modal Popup")):::trigger
    Webhook(("Webhook")):::trigger
    Respond_to_Slack_Webhook___Vulnerability(("Respond to Slack Webhook - Vulnerability")):::trigger
    Respond_to_Slack_Webhook___Report(("Respond to Slack Webhook - Report")):::trigger

    Webhook --> Parse_Webhook
    Parse_Webhook --> Route_Message
    Route_Message --> Respond_to_Slack_Webhook___Vulnerability
    Route_Message --> Respond_to_Slack_Webhook___Report
    Route_Message --> Close_Modal_Popup
    Route_Submission --> Required_Scan_Variables
    Route_Submission --> Required_Report_Variables
    Close_Modal_Popup --> Route_Submission
    Required_Scan_Variables --> Qualys_Start_Vulnerability_Scan
    Required_Report_Variables --> Qualys_Create_Report
    Respond_to_Slack_Webhook___Report --> Scan_Report_Task_Modal
    Respond_to_Slack_Webhook___Vulnerability --> Vuln_Scan_Modal
```
