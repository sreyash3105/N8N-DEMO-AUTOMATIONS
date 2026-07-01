```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Fal_Flux["fas:fa-globe Fal Flux"]
    Get_Image_Result_URL["fas:fa-globe Get Image Result URL"]
    Download_Image["fas:fa-globe Download Image"]
    Google_Drive["fab:fa-google Google Drive"]
    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Wait_3_Sec["fas:fa-robot Wait 3 Sec"]
    Check_Status["fas:fa-globe Check Status"]
    Completed_{"fas:fa-code-branch Completed?"}:::logic
    Edit_Fields["fas:fa-cogs Edit Fields"]

    Fal_Flux --> Wait_3_Sec
    Completed_ --> Get_Image_Result_URL
    Completed_ --> Wait_3_Sec
    Wait_3_Sec --> Check_Status
    Edit_Fields --> Fal_Flux
    Check_Status --> Completed_
    Download_Image --> Google_Drive
    Get_Image_Result_URL --> Download_Image
    When_clicking__Test_workflow_ --> Edit_Fields
```
