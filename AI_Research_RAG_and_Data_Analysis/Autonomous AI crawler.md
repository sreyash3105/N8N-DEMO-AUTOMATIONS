```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Text["fas:fa-robot Text"]
    URLs["fas:fa-robot URLs"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    JSON_Parser["fas:fa-robot JSON Parser"]
    Map_company_name_and_website["fas:fa-cogs Map company name and website"]
    Execute_workflow(("fas:fa-bolt Execute workflow")):::trigger
    Get_companies["fas:fa-database Get companies"]
    Select_company_name_and_website["fas:fa-cogs Select company name and website"]
    Set_social_media_array["fas:fa-cogs Set social media array"]
    Merge_all_data["fas:fa-cogs Merge all data"]
    Insert_new_row["fas:fa-database Insert new row"]
    Convert_HTML_to_Markdown["fas:fa-cogs Convert HTML to Markdown"]
    Retrieve_URLs["fas:fa-cogs Retrieve URLs"]
    Split_out_URLs["fas:fa-cogs Split out URLs"]
    Remove_duplicated["fas:fa-cogs Remove duplicated"]
    Set_domain_to_path["fas:fa-cogs Set domain to path"]
    Filter_out_invalid_URLs["fas:fa-cogs Filter out invalid URLs"]
    Aggregate_URLs["fas:fa-cogs Aggregate URLs"]
    Filter_out_empty_hrefs["fas:fa-cogs Filter out empty hrefs"]
    Set_domain__text_["fas:fa-cogs Set domain (text)"]
    Add_protocool_to_domain__text_["fas:fa-cogs Add protocool to domain (text)"]
    Get_website__text_["fas:fa-globe Get website (text)"]
    Set_response__text_["fas:fa-cogs Set response (text)"]
    Set_domain__URL_["fas:fa-cogs Set domain (URL)"]
    Get_website__URL_["fas:fa-globe Get website (URL)"]
    Set_response__URL_["fas:fa-cogs Set response (URL)"]
    Add_protocool_to_domain__URL_["fas:fa-cogs Add protocool to domain (URL)"]
    Crawl_website["fas:fa-robot Crawl website"]:::ai

    Text --> Crawl_website
    URLs --> Crawl_website
    JSON_Parser --> Crawl_website
    Crawl_website --> Set_social_media_array
    Get_companies --> Select_company_name_and_website
    Retrieve_URLs --> Split_out_URLs
    Aggregate_URLs --> Set_response__URL_
    Merge_all_data --> Insert_new_row
    Split_out_URLs --> Filter_out_empty_hrefs
    Execute_workflow --> Get_companies
    Set_domain__URL_ --> Add_protocool_to_domain__URL_
    Get_website__URL_ --> Retrieve_URLs
    OpenAI_Chat_Model --> Crawl_website
    Remove_duplicated --> Set_domain_to_path
    Set_domain__text_ --> Add_protocool_to_domain__text_
    Get_website__text_ --> Convert_HTML_to_Markdown
    Set_domain_to_path --> Filter_out_invalid_URLs
    Filter_out_empty_hrefs --> Remove_duplicated
    Set_social_media_array --> Merge_all_data
    Filter_out_invalid_URLs --> Aggregate_URLs
    Convert_HTML_to_Markdown --> Set_response__text_
    Map_company_name_and_website --> Merge_all_data
    Add_protocool_to_domain__URL_ --> Get_website__URL_
    Add_protocool_to_domain__text_ --> Get_website__text_
    Select_company_name_and_website --> Crawl_website
    Select_company_name_and_website --> Map_company_name_and_website
```
