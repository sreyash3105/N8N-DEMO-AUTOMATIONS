```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    On_clicking__execute_(("fas:fa-bolt On clicking 'execute'")):::trigger
    Fetch_new_followers["fas:fa-globe Fetch new followers"]
    Item_Lists["fas:fa-cogs Item Lists"]
    Function["fas:fa-cogs Function"]
    Merge["fas:fa-cogs Merge"]
    Fetching_images["fas:fa-globe Fetching images"]
    Fetch_bg["fas:fa-globe Fetch bg"]
    Resize["fas:fa-cogs Resize"]
    Crop["fas:fa-cogs Crop"]
    Edit_Image["fas:fa-cogs Edit Image"]
    Resize1["fas:fa-cogs Resize1"]
    HTTP_Request["fas:fa-globe HTTP Request"]

    Crop --> Resize1
    Merge --> Edit_Image
    Resize --> Crop
    Resize1 --> Function
    Fetch_bg --> Merge
    Function --> Merge
    Edit_Image --> HTTP_Request
    Item_Lists --> Fetching_images
    Fetching_images --> Resize
    Fetch_new_followers --> Item_Lists
    On_clicking__execute_ --> Fetch_new_followers
```
