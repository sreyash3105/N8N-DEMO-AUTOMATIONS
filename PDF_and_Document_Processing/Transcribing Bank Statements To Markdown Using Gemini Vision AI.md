```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    Google_Gemini_Chat_Model["Google Gemini Chat Model"]
    Sort_Pages["Sort Pages"]
    Get_Bank_Statement["Get Bank Statement"]
    Split_PDF_into_Images["Split PDF into Images"]
    Extract_Zip_File["Extract Zip File"]
    Images_To_List["Images To List"]
    Resize_Images_For_AI["Resize Images For AI"]
    Google_Gemini_Chat_Model1["Google Gemini Chat Model1"]
    Combine_All_Pages["Combine All Pages"]
    Extract_All_Deposit_Table_Rows["Extract All Deposit Table Rows"]
    Transcribe_to_Markdown(["Transcribe to Markdown"]):::ai

    Sort_Pages --> Resize_Images_For_AI
    Images_To_List --> Sort_Pages
    Extract_Zip_File --> Images_To_List
    Combine_All_Pages --> Extract_All_Deposit_Table_Rows
    Get_Bank_Statement --> Split_PDF_into_Images
    Resize_Images_For_AI --> Transcribe_to_Markdown
    Split_PDF_into_Images --> Extract_Zip_File
    Transcribe_to_Markdown --> Combine_All_Pages
    Google_Gemini_Chat_Model --> Transcribe_to_Markdown
    Google_Gemini_Chat_Model1 --> Extract_All_Deposit_Table_Rows
    When_clicking__Test_workflow_ --> Get_Bank_Statement
```
