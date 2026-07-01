```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Printify___Get_Shops["fas:fa-globe Printify - Get Shops"]
    Printify___Get_Products["fas:fa-globe Printify - Get Products"]
    Split_Out["fas:fa-cogs Split Out"]
    Loop_Over_Items["fas:fa-cogs Loop Over Items"]
    Split___id__title__desc["fas:fa-cogs Split - id, title, desc"]
    Calculator["fas:fa-robot Calculator"]
    Wikipedia["fas:fa-robot Wikipedia"]
    Printify___Update_Product["fas:fa-globe Printify - Update Product"]
    Brand_Guidelines___Custom_Instructions["fas:fa-cogs Brand Guidelines + Custom Instructions"]
    Google_Sheets_Trigger(("fab:fa-google Google Sheets Trigger")):::trigger
    Printify___Get_Shops1["fas:fa-globe Printify - Get Shops1"]
    GS___Add_Product_Option["fab:fa-google GS - Add Product Option"]
    Update_Product_Option["fab:fa-google Update Product Option"]
    If1{"fas:fa-code-branch If1"}:::logic
    Number_of_Options["fas:fa-cogs Number of Options"]
    Calculate_Options["fas:fa-cogs Calculate Options"]
    Remember_Options["fas:fa-cogs Remember Options"]
    Generate_Title_and_Desc(["fas:fa-robot Generate Title and Desc"]):::ai
    If{"fas:fa-code-branch If"}:::logic

    If --> Printify___Get_Shops1
    If1 --> Loop_Over_Items
    If1 --> GS___Add_Product_Option
    Split_Out --> Loop_Over_Items
    Wikipedia --> Generate_Title_and_Desc
    Calculator --> Generate_Title_and_Desc
    Loop_Over_Items --> Split___id__title__desc
    Remember_Options --> Calculate_Options
    Calculate_Options --> If1
    Number_of_Options --> Calculate_Options
    Printify___Get_Shops --> Printify___Get_Products
    Google_Sheets_Trigger --> If
    Printify___Get_Shops1 --> Printify___Update_Product
    Update_Product_Option --> Remember_Options
    GS___Add_Product_Option --> Generate_Title_and_Desc
    Generate_Title_and_Desc --> Update_Product_Option
    Printify___Get_Products --> Split_Out
    Split___id__title__desc --> Number_of_Options
    When_clicking__Test_workflow_ --> Brand_Guidelines___Custom_Instructions
    Brand_Guidelines___Custom_Instructions --> Printify___Get_Shops
```
