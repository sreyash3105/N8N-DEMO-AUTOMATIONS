```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Form(("fas:fa-bolt Form")):::trigger
    Settings["fas:fa-cogs Settings"]
    Check_data_consistency{"fas:fa-code-branch Check data consistency"}:::logic
    Split_out_chapters["fas:fa-cogs Split out chapters"]
    Merge_chapters_title_and_text["fas:fa-cogs Merge chapters title and text"]
    Final_article_text["fas:fa-cogs Final article text"]
    Post_on_Wordpress["fab:fa-wordpress Post on Wordpress"]
    Upload_media["fas:fa-globe Upload media"]
    Set_image_ID_for_the_post["fas:fa-globe Set image ID for the post"]
    Respond__Success(("fas:fa-bolt Respond: Success")):::trigger
    Respond__Error(("fas:fa-bolt Respond: Error")):::trigger
    Generate_featured_image(["fas:fa-robot Generate featured image"]):::ai
    Wikipedia["fas:fa-robot Wikipedia"]
    Create_post_title_and_structure(["fas:fa-robot Create post title and structure"]):::ai
    Create_chapters_text(["fas:fa-robot Create chapters text"]):::ai

    Form --> Settings
    Settings --> Create_post_title_and_structure
    Wikipedia --> Create_post_title_and_structure
    Upload_media --> Set_image_ID_for_the_post
    Post_on_Wordpress --> Generate_featured_image
    Final_article_text --> Post_on_Wordpress
    Split_out_chapters --> Merge_chapters_title_and_text
    Split_out_chapters --> Create_chapters_text
    Create_chapters_text --> Merge_chapters_title_and_text
    Check_data_consistency --> Split_out_chapters
    Check_data_consistency --> Respond__Error
    Generate_featured_image --> Upload_media
    Set_image_ID_for_the_post --> Respond__Success
    Merge_chapters_title_and_text --> Final_article_text
    Create_post_title_and_structure --> Check_data_consistency
```
