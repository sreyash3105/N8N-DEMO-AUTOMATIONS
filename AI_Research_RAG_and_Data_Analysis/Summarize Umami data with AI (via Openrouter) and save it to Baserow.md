```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    Schedule_Trigger(("Schedule Trigger")):::trigger
    Get_view_stats_from_Umami["Get view stats from Umami"]
    Parse_Umami_data["Parse Umami data"]
    Send_data_to_A_I_["Send data to A.I."]
    Get_page_data_from_Umami["Get page data from Umami"]
    Parse_Umami_data1["Parse Umami data1"]
    Get_page_view_data_from_Umami["Get page view data from Umami"]
    Parse_Umami["Parse Umami"]
    Send_data_to_A_I_1["Send data to A.I.1"]
    Save_data_to_Baserow["Save data to Baserow"]

    Parse_Umami --> Send_data_to_A_I_1
    Parse_Umami_data --> Send_data_to_A_I_
    Schedule_Trigger --> Get_view_stats_from_Umami
    Parse_Umami_data1 --> Get_page_view_data_from_Umami
    Send_data_to_A_I_ --> Get_page_data_from_Umami
    Send_data_to_A_I_1 --> Save_data_to_Baserow
    Get_page_data_from_Umami --> Parse_Umami_data1
    Get_view_stats_from_Umami --> Parse_Umami_data
    Get_page_view_data_from_Umami --> Parse_Umami
    When_clicking__Test_workflow_ --> Get_view_stats_from_Umami
```
