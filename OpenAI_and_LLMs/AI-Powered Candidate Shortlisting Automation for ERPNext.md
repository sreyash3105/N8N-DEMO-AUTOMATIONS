```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Code["Code"]
    ApplicantData["ApplicantData"]
    ERPNext___Reject_if_Resume_not_Attached["ERPNext - Reject if Resume not Attached"]
    Applied_Against_Job{"Applied Against Job"}:::logic
    ERPNext___Hold_Applicant["ERPNext - Hold Applicant"]
    Get_Job_Opening["Get Job Opening"]
    Google_Gemini_Chat_Model["Google Gemini Chat Model"]
    Convert_to_Fields["Convert to Fields"]
    If_score_less_than_80{"If score less than 80"}:::logic
    Reject_Applicant["Reject Applicant"]
    Update_Applicant_Data["Update Applicant Data"]
    Reume_Attachment_Link["Reume Attachment Link"]
    Resume_Link_Provided{"Resume Link Provided"}:::logic
    Accept_Applicant["Accept Applicant"]
    Webhook(("Webhook")):::trigger
    File_Type{"File Type"}:::logic
    Download_PDF_Resume["Download PDF Resume"]
    PDF_to_Text["PDF to Text"]
    Txt_File_to_Text__Example_["Txt File to Text (Example)"]
    Merge1["Merge1"]
    Recruitment_AI_Agent["Recruitment AI Agent"]:::ai
    Microsoft_Outlook["Microsoft Outlook"]
    WhatsApp_Business_Cloud["WhatsApp Business Cloud"]

    Code --> ApplicantData
    Merge1 --> Get_Job_Opening
    Webhook --> Code
    File_Type --> Download_PDF_Resume
    PDF_to_Text --> Merge1
    ApplicantData --> Resume_Link_Provided
    Get_Job_Opening --> Recruitment_AI_Agent
    Accept_Applicant --> WhatsApp_Business_Cloud
    Reject_Applicant --> Microsoft_Outlook
    Convert_to_Fields --> Update_Applicant_Data
    Applied_Against_Job --> Reume_Attachment_Link
    Applied_Against_Job --> ERPNext___Hold_Applicant
    Download_PDF_Resume --> PDF_to_Text
    Recruitment_AI_Agent --> Convert_to_Fields
    Resume_Link_Provided --> Applied_Against_Job
    Resume_Link_Provided --> ERPNext___Reject_if_Resume_not_Attached
    If_score_less_than_80 --> Reject_Applicant
    If_score_less_than_80 --> Accept_Applicant
    Reume_Attachment_Link --> File_Type
    Update_Applicant_Data --> If_score_less_than_80
    Google_Gemini_Chat_Model --> Recruitment_AI_Agent
    Txt_File_to_Text__Example_ --> Merge1
```
