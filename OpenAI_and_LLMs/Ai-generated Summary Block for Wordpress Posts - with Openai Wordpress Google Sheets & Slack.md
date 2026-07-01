```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Text_Classifier{"fas:fa-robot Text Classifier"}:::logic
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Loop_Over_Items["fas:fa-cogs Loop Over Items"]
    If{"fas:fa-code-branch If"}:::logic
    Webhook(("fas:fa-bolt Webhook")):::trigger
    Schedule_Trigger(("fas:fa-bolt Schedule Trigger")):::trigger
    Wordpress___Update_Post["fab:fa-wordpress Wordpress - Update Post"]
    Google_Sheets___Get_rows["fab:fa-google Google Sheets - Get rows"]
    HTML_to_Markdown["fas:fa-cogs HTML to Markdown"]
    OpenAI(["fas:fa-robot OpenAI"]):::ai
    Google_Sheets___Add_Row["fab:fa-google Google Sheets - Add Row"]
    Slack___Notify_Channel["fab:fa-slack Slack - Notify Channel"]
    Set_fields___From_Webhook_input["fas:fa-cogs Set fields - From Webhook input"]
    Date___Time___Substract["fas:fa-cogs Date & Time - Substract"]
    Set_fields___Prepare_data_for_Gsheets___Slack["fab:fa-slack Set fields - Prepare data for Gsheets & Slack"]
    WordPress___Get_Post2["fab:fa-wordpress WordPress - Get Post2"]
    No_Operation__do_nothing["fas:fa-cogs No Operation, do nothing"]
    WordPress___Get_Last_Posts["fab:fa-wordpress WordPress - Get Last Posts"]
    WordPress___Get_Post1["fab:fa-wordpress WordPress - Get Post1"]
    WordPress___Get_All_Posts["fab:fa-wordpress WordPress - Get All Posts"]

    If --> Loop_Over_Items
    If --> WordPress___Get_Post2
    OpenAI --> Wordpress___Update_Post
    Webhook --> Set_fields___From_Webhook_input
    Loop_Over_Items --> No_Operation__do_nothing
    Loop_Over_Items --> Google_Sheets___Get_rows
    Text_Classifier --> OpenAI
    Text_Classifier --> Loop_Over_Items
    HTML_to_Markdown --> Text_Classifier
    Schedule_Trigger --> Date___Time___Substract
    OpenAI_Chat_Model --> Text_Classifier
    WordPress___Get_Post2 --> HTML_to_Markdown
    Slack___Notify_Channel --> Loop_Over_Items
    Date___Time___Substract --> WordPress___Get_Last_Posts
    Google_Sheets___Add_Row --> Slack___Notify_Channel
    Wordpress___Update_Post --> Set_fields___Prepare_data_for_Gsheets___Slack
    Google_Sheets___Get_rows --> If
    WordPress___Get_All_Posts --> Loop_Over_Items
    Set_fields___From_Webhook_input --> WordPress___Get_Post1
    When_clicking__Test_workflow_ --> WordPress___Get_All_Posts
    Set_fields___Prepare_data_for_Gsheets___Slack --> Google_Sheets___Add_Row
```
