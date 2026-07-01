```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Base_Image["fab:fa-google Base Image"]
    Google_Gemini_Chat_Model["fab:fa-google Google Gemini Chat Model"]
    Structured_Output_Parser["fas:fa-robot Structured Output Parser"]
    Loop_Over_Items["fas:fa-cogs Loop Over Items"]
    Wait["fas:fa-robot Wait"]
    Download_Screenshot["fas:fa-globe Download Screenshot"]
    Upload_to_Drive["fab:fa-google Upload to Drive"]
    Update_Base_Image["fab:fa-google Update Base Image"]
    Merge["fas:fa-cogs Merge"]
    Schedule_Trigger(("fas:fa-bolt Schedule Trigger")):::trigger
    Get_URLs_with_Missing_Base_Images["fab:fa-google Get URLs with Missing Base Images"]
    Run_Webpage_Screenshot["fas:fa-globe Run Webpage Screenshot"]
    Run_Webpage_Screenshot1["fas:fa-globe Run Webpage Screenshot1"]
    Has_Changes["fas:fa-cogs Has Changes"]
    Combine_Row_and_Result["fas:fa-cogs Combine Row and Result"]
    Wait1["fas:fa-robot Wait1"]
    Aggregate["fas:fa-cogs Aggregate"]
    Create_Report["fas:fa-cogs Create Report"]
    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Get_Webpages_List["fab:fa-google Get Webpages List"]
    For_Each_Webpage___["fas:fa-cogs For Each Webpage..."]
    Download_New_Screenshot["fas:fa-globe Download New Screenshot"]
    Combine_Screenshots["fas:fa-cogs Combine Screenshots"]
    Visual_Regression_Agent(["fas:fa-robot Visual Regression Agent"]):::ai

    Wait --> Loop_Over_Items
    Merge --> Download_Screenshot
    Wait1 --> For_Each_Webpage___
    Aggregate --> Create_Report
    Base_Image --> Combine_Screenshots
    Has_Changes --> Aggregate
    Loop_Over_Items --> Merge
    Loop_Over_Items --> Run_Webpage_Screenshot
    Upload_to_Drive --> Update_Base_Image
    Schedule_Trigger --> Get_Webpages_List
    Get_Webpages_List --> For_Each_Webpage___
    Combine_Screenshots --> Visual_Regression_Agent
    Download_Screenshot --> Upload_to_Drive
    For_Each_Webpage___ --> Combine_Row_and_Result
    For_Each_Webpage___ --> Base_Image
    For_Each_Webpage___ --> Run_Webpage_Screenshot1
    Combine_Row_and_Result --> Has_Changes
    Run_Webpage_Screenshot --> Wait
    Download_New_Screenshot --> Combine_Screenshots
    Run_Webpage_Screenshot1 --> Download_New_Screenshot
    Visual_Regression_Agent --> Wait1
    Google_Gemini_Chat_Model --> Visual_Regression_Agent
    Structured_Output_Parser --> Visual_Regression_Agent
    Get_URLs_with_Missing_Base_Images --> Loop_Over_Items
    Get_URLs_with_Missing_Base_Images --> Merge
    When_clicking__Test_workflow_ --> Get_URLs_with_Missing_Base_Images
```
