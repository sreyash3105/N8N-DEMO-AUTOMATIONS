```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    n8n_Form_Trigger(("fas:fa-bolt n8n Form Trigger")):::trigger
    Form_End["fas:fa-cogs Form End"]
    Enter_Date___Time["fas:fa-cogs Enter Date & Time"]
    Get_Form_Values["fas:fa-cogs Get Form Values"]
    Terms___Conditions["fas:fa-cogs Terms & Conditions"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Has_Accepted_{"fas:fa-code-branch Has Accepted?"}:::logic
    Send_Receipt["fas:fa-envelope Send Receipt"]
    Wait_for_Approval["fas:fa-envelope Wait for Approval"]
    Has_Approval_{"fas:fa-code-branch Has Approval?"}:::logic
    OpenAI_Chat_Model1(["fas:fa-robot OpenAI Chat Model1"]):::ai
    Create_Appointment["fab:fa-google Create Appointment"]
    Send_Rejection["fas:fa-envelope Send Rejection"]
    Decline["fas:fa-cogs Decline"]
    Decline1["fas:fa-cogs Decline1"]
    Trigger_Approval_Process["fas:fa-cogs Trigger Approval Process"]
    Execute_Workflow_Trigger(("fas:fa-bolt Execute Workflow Trigger")):::trigger
    Summarise_Enquiry(["fas:fa-robot Summarise Enquiry"]):::ai
    Enquiry_Classifier{"fas:fa-robot Enquiry Classifier"}:::logic

    Send_Receipt --> Form_End
    Has_Accepted_ --> Enter_Date___Time
    Has_Accepted_ --> Decline1
    Has_Approval_ --> Create_Appointment
    Has_Approval_ --> Send_Rejection
    Get_Form_Values --> Trigger_Approval_Process
    n8n_Form_Trigger --> Enquiry_Classifier
    Enter_Date___Time --> Get_Form_Values
    OpenAI_Chat_Model --> Enquiry_Classifier
    Summarise_Enquiry --> Wait_for_Approval
    Wait_for_Approval --> Has_Approval_
    Enquiry_Classifier --> Terms___Conditions
    Enquiry_Classifier --> Decline
    OpenAI_Chat_Model1 --> Summarise_Enquiry
    Terms___Conditions --> Has_Accepted_
    Execute_Workflow_Trigger --> Summarise_Enquiry
    Trigger_Approval_Process --> Send_Receipt
```
