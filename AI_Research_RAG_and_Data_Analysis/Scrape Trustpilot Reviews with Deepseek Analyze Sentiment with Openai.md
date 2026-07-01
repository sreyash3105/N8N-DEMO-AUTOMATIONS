```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Split_Out["fas:fa-cogs Split Out"]
    Information_Extractor["fas:fa-robot Information Extractor"]
    If{"fas:fa-code-branch If"}:::logic
    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Limit1["fas:fa-cogs Limit1"]
    Set_Parameters["fas:fa-cogs Set Parameters"]
    Get_reviews["fas:fa-globe Get reviews"]
    Extract["fas:fa-cogs Extract"]
    Get_rows["fab:fa-google Get rows"]
    Get_Google_Sheets["fab:fa-google Get Google Sheets"]
    Get_Single_review["fas:fa-globe Get Single review"]
    Extract_review["fas:fa-cogs Extract review"]
    Update_sheet["fab:fa-google Update sheet"]
    Sentiment_Analysis["fas:fa-robot Sentiment Analysis"]
    DeepSeek_Chat_Model(["fas:fa-robot DeepSeek Chat Model"]):::ai
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai

    If --> Get_Single_review
    Limit1 --> Get_Google_Sheets
    Extract --> Split_Out
    Get_rows --> If
    Split_Out --> Limit1
    Get_reviews --> Extract
    Extract_review --> Information_Extractor
    Set_Parameters --> Get_reviews
    Get_Google_Sheets --> Get_rows
    Get_Single_review --> Extract_review
    OpenAI_Chat_Model --> Sentiment_Analysis
    Sentiment_Analysis --> Update_sheet
    Sentiment_Analysis --> Update_sheet
    Sentiment_Analysis --> Update_sheet
    DeepSeek_Chat_Model --> Information_Extractor
    Information_Extractor --> Sentiment_Analysis
    When_clicking__Test_workflow_ --> Set_Parameters
```
