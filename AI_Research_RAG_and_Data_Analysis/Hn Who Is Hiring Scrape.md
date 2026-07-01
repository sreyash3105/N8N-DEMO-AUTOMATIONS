```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Split_Out["fas:fa-cogs Split Out"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    Structured_Output_Parser["fas:fa-robot Structured Output Parser"]
    Search_for_Who_is_hiring_posts["fas:fa-globe Search for Who is hiring posts"]
    Get_relevant_data["fas:fa-cogs Get relevant data"]
    Get_latest_post["fas:fa-cogs Get latest post"]
    Split_out_children__jobs_["fas:fa-cogs Split out children (jobs)"]
    Trun_into_structured_data(["fas:fa-robot Trun into structured data"]):::ai
    Extract_text["fas:fa-cogs Extract text"]
    Clean_text["fas:fa-cogs Clean text"]
    Limit_for_testing__optional_["fas:fa-cogs Limit for testing (optional)"]
    Write_results_to_airtable["fas:fa-robot Write results to airtable"]
    HI_API__Get_the_individual_job_post["fas:fa-globe HI API: Get the individual job post"]
    HN_API__Get_Main_Post["fas:fa-globe HN API: Get Main Post"]

    Split_Out --> Get_relevant_data
    Clean_text --> Limit_for_testing__optional_
    Extract_text --> Clean_text
    Get_latest_post --> HN_API__Get_Main_Post
    Get_relevant_data --> Get_latest_post
    OpenAI_Chat_Model --> Trun_into_structured_data
    HN_API__Get_Main_Post --> Split_out_children__jobs_
    Structured_Output_Parser --> Trun_into_structured_data
    Split_out_children__jobs_ --> HI_API__Get_the_individual_job_post
    Trun_into_structured_data --> Write_results_to_airtable
    Limit_for_testing__optional_ --> Trun_into_structured_data
    Search_for_Who_is_hiring_posts --> Split_Out
    When_clicking__Test_workflow_ --> Search_for_Who_is_hiring_posts
    HI_API__Get_the_individual_job_post --> Extract_text
```
