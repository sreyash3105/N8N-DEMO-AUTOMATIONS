```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Crawl_HN_Home["Crawl HN Home"]
    Extract_Meta["Extract Meta"]
    Filter_Unposted_Items["Filter Unposted Items"]
    Visit_GH_Page["Visit GH Page"]
    Convert_HTML_To_Markdown["Convert HTML To Markdown"]
    Filter_Errored["Filter Errored"]
    No_Operation__do_nothing["No Operation, do nothing"]
    Update_X_Status["Update X Status"]
    LinkedIn["LinkedIn"]
    Update_L_Status["Update L Status"]
    Search_Item["Search Item"]
    Create_Item["Create Item"]
    X["X"]
    Validate_Generate_Content["Validate Generate Content"]
    Schedule_Trigger(("Schedule Trigger")):::trigger
    Merge["Merge"]
    Generate_Content(["Generate Content"]):::ai
    Ping_Me["Ping Me"]
    Wait_for_5_mins_before_posting["Wait for 5 mins before posting"]

    X --> Update_X_Status
    Merge --> Filter_Unposted_Items
    Ping_Me --> Wait_for_5_mins_before_posting
    LinkedIn --> Update_L_Status
    Create_Item --> Ping_Me
    Search_Item --> Merge
    Extract_Meta --> Search_Item
    Extract_Meta --> Merge
    Crawl_HN_Home --> Extract_Meta
    Visit_GH_Page --> Convert_HTML_To_Markdown
    Filter_Errored --> Create_Item
    Update_L_Status --> No_Operation__do_nothing
    Update_X_Status --> No_Operation__do_nothing
    Generate_Content --> Validate_Generate_Content
    Schedule_Trigger --> Crawl_HN_Home
    Filter_Unposted_Items --> Visit_GH_Page
    Convert_HTML_To_Markdown --> Generate_Content
    Validate_Generate_Content --> Filter_Errored
    Wait_for_5_mins_before_posting --> X
    Wait_for_5_mins_before_posting --> LinkedIn
```
