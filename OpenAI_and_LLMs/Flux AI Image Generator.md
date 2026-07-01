```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Vivid_Pop_Explosion["fas:fa-cogs Vivid Pop Explosion"]
    AI_Dystopia["fas:fa-cogs AI Dystopia"]
    Post_Analog_Glitchscape["fas:fa-cogs Post-Analog Glitchscape"]
    Neon_Fauvism["fas:fa-cogs Neon Fauvism"]
    None["fas:fa-cogs None"]
    Serve_webpage(("fas:fa-bolt Serve webpage")):::trigger
    Respond_with_error(("fas:fa-bolt Respond with error")):::trigger
    Upload_image_to_S3["fas:fa-cogs Upload image to S3"]
    Hyper_Surreal_Escape["fas:fa-cogs Hyper-Surreal Escape"]
    n8n_Form_Trigger(("fas:fa-bolt n8n Form Trigger")):::trigger
    Call_hugginface_inference_api["fas:fa-globe Call hugginface inference api"]
    Route_by_style{"fas:fa-code-branch Route by style"}:::logic

    None --> Call_hugginface_inference_api
    AI_Dystopia --> Call_hugginface_inference_api
    Neon_Fauvism --> Call_hugginface_inference_api
    Route_by_style --> Hyper_Surreal_Escape
    Route_by_style --> Post_Analog_Glitchscape
    Route_by_style --> AI_Dystopia
    Route_by_style --> Neon_Fauvism
    Route_by_style --> Vivid_Pop_Explosion
    Route_by_style --> None
    n8n_Form_Trigger --> Route_by_style
    Upload_image_to_S3 --> Serve_webpage
    Upload_image_to_S3 --> Respond_with_error
    Vivid_Pop_Explosion --> Call_hugginface_inference_api
    Hyper_Surreal_Escape --> Call_hugginface_inference_api
    Post_Analog_Glitchscape --> Call_hugginface_inference_api
    Call_hugginface_inference_api --> Upload_image_to_S3
    Call_hugginface_inference_api --> Respond_with_error
```
