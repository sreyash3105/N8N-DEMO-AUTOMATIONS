```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    Printify___Get_Shops["Printify - Get Shops"]
    Printify___Get_Products["Printify - Get Products"]
    Split_Out["Split Out"]
    Loop_Over_Items["Loop Over Items"]
    Split___id__title__desc["Split - id, title, desc"]
    Calculator["Calculator"]
    Wikipedia["Wikipedia"]
    Printify___Update_Product["Printify - Update Product"]
    Brand_Guidelines___Custom_Instructions["Brand Guidelines + Custom Instructions"]
    Google_Sheets_Trigger(("Google Sheets Trigger")):::trigger
    Printify___Get_Shops1["Printify - Get Shops1"]
    GS___Add_Product_Option["GS - Add Product Option"]
    Update_Product_Option["Update Product Option"]
    If1{"If1"}:::logic
    Number_of_Options["Number of Options"]
    Calculate_Options["Calculate Options"]
    Remember_Options["Remember Options"]
    Generate_Title_and_Desc(["Generate Title and Desc"]):::ai
    If{"If"}:::logic

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
