```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    If_media_status_is_finished{"If media status is finished"}:::logic
    If_media_status_is_finished1{"If media status is finished1"}:::logic
    Telegram["Telegram"]
    Telegram1["Telegram1"]
    Telegram2["Telegram2"]
    Loop_Over_Items["Loop Over Items"]
    Schedule_Trigger1(("Schedule Trigger1")):::trigger
    Telegram_Params["Telegram Params"]
    Instagram_params["Instagram params"]
    Rapid_Api_params["Rapid Api params"]
    filter_the_image_content["filter the image content"]
    get_top_trends_on_instagram__blender3d["get top trends on instagram #blender3d"]
    get_top_trends_on_instagram__isometric["get top trends on instagram #isometric"]
    merge_the_array_content["merge the array content"]
    Check_Data_on_Database_Is_Exist["Check Data on Database Is Exist"]
    If_Data_is_Exist{"If Data is Exist"}:::logic
    send_error_message_to_telegram["send error message to telegram"]
    insert_data_on_db["insert data on db"]
    Analyze_Image_and_give_the_content(["Analyze Image and give the content"]):::ai
    Analyze_Content_And_Generate_Instagram_Caption(["Analyze Content And Generate Instagram Caption"]):::ai
    Prepare_data_on_Instagram["Prepare data on Instagram"]
    Check_Status_Of_Media_Before_Uploaded["Check Status Of Media Before Uploaded"]
    Publish_Media_on_Instagram["Publish Media on Instagram"]
    Check_status_of_post_["Check status of post "]
    filter_the_image_content_2["filter the image content-2"]
    Replicate_params["Replicate params"]
    Generate_image_on_flux["Generate image on flux"]

    Loop_Over_Items --> Check_Data_on_Database_Is_Exist
    Telegram_Params --> Rapid_Api_params
    If_Data_is_Exist --> Loop_Over_Items
    If_Data_is_Exist --> insert_data_on_db
    Instagram_params --> Telegram_Params
    Rapid_Api_params --> get_top_trends_on_instagram__isometric
    Rapid_Api_params --> get_top_trends_on_instagram__blender3d
    Replicate_params --> Instagram_params
    Schedule_Trigger1 --> Replicate_params
    insert_data_on_db --> Analyze_Image_and_give_the_content
    Check_status_of_post_ --> If_media_status_is_finished1
    Generate_image_on_flux --> Prepare_data_on_Instagram
    merge_the_array_content --> Loop_Over_Items
    filter_the_image_content --> merge_the_array_content
    Prepare_data_on_Instagram --> Check_Status_Of_Media_Before_Uploaded
    Publish_Media_on_Instagram --> Check_status_of_post_
    filter_the_image_content_2 --> merge_the_array_content
    If_media_status_is_finished --> Publish_Media_on_Instagram
    If_media_status_is_finished --> Telegram
    If_media_status_is_finished1 --> Telegram1
    If_media_status_is_finished1 --> Telegram2
    Check_Data_on_Database_Is_Exist --> If_Data_is_Exist
    Check_Data_on_Database_Is_Exist --> send_error_message_to_telegram
    Analyze_Image_and_give_the_content --> Analyze_Content_And_Generate_Instagram_Caption
    Check_Status_Of_Media_Before_Uploaded --> If_media_status_is_finished
    get_top_trends_on_instagram__isometric --> filter_the_image_content
    get_top_trends_on_instagram__blender3d --> filter_the_image_content_2
    Analyze_Content_And_Generate_Instagram_Caption --> Generate_image_on_flux
```
