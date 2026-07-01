```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    OpenAI_Chat_Model1(["fas:fa-robot OpenAI Chat Model1"]):::ai
    OpenAI_Chat_Model2(["fas:fa-robot OpenAI Chat Model2"]):::ai
    Merge["fas:fa-cogs Merge"]
    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    SET_company_name["fas:fa-cogs SET company_name"]
    Define_dictionary_of_demographic_keys["fas:fa-cogs Define dictionary of demographic keys"]
    ScrapingBee_Search_Glassdoor["fas:fa-globe ScrapingBee Search Glassdoor"]
    Extract_company_url_path["fas:fa-cogs Extract company url path"]
    ScrapingBee_GET_company_page_contents["fas:fa-globe ScrapingBee GET company page contents"]
    Extract_reviews_page_url_path["fas:fa-cogs Extract reviews page url path"]
    ScrapingBee_GET_Glassdoor_Reviews_Content["fas:fa-globe ScrapingBee GET Glassdoor Reviews Content"]
    Extract_Overall_Review_Summary["fas:fa-cogs Extract Overall Review Summary"]
    Extract_Demographics_Module["fas:fa-cogs Extract Demographics Module"]
    Extract_overall_ratings_and_distribution_percentages["fas:fa-robot Extract overall ratings and distribution percentages"]
    Extract_demographic_distributions["fas:fa-robot Extract demographic distributions"]
    Define_contributions_to_variance["fas:fa-cogs Define contributions to variance"]
    Set_variance_and_std_dev["fas:fa-cogs Set variance and std_dev"]
    Calculate_P_Scores["fas:fa-cogs Calculate P-Scores"]
    Sort_Effect_Sizes["fas:fa-cogs Sort Effect Sizes"]
    Calculate_Z_Scores_and_Effect_Sizes["fas:fa-cogs Calculate Z-Scores and Effect Sizes"]
    Format_dataset_for_scatterplot["fas:fa-cogs Format dataset for scatterplot"]
    Specify_additional_parameters_for_scatterplot["fas:fa-cogs Specify additional parameters for scatterplot"]
    Quickchart_Scatterplot["fas:fa-globe Quickchart Scatterplot"]
    QuickChart_Bar_Chart["fas:fa-cogs QuickChart Bar Chart"]
    Text_Analysis_of_Bias_Data(["fas:fa-robot Text Analysis of Bias Data"]):::ai

    Merge --> Calculate_Z_Scores_and_Effect_Sizes
    SET_company_name --> Define_dictionary_of_demographic_keys
    OpenAI_Chat_Model --> Text_Analysis_of_Bias_Data
    Sort_Effect_Sizes --> QuickChart_Bar_Chart
    Sort_Effect_Sizes --> Text_Analysis_of_Bias_Data
    Calculate_P_Scores --> Sort_Effect_Sizes
    OpenAI_Chat_Model1 --> Extract_demographic_distributions
    OpenAI_Chat_Model2 --> Extract_overall_ratings_and_distribution_percentages
    Extract_company_url_path --> ScrapingBee_GET_company_page_contents
    Set_variance_and_std_dev --> Merge
    Extract_Demographics_Module --> Extract_demographic_distributions
    ScrapingBee_Search_Glassdoor --> Extract_company_url_path
    Extract_reviews_page_url_path --> ScrapingBee_GET_Glassdoor_Reviews_Content
    Extract_Overall_Review_Summary --> Extract_overall_ratings_and_distribution_percentages
    Format_dataset_for_scatterplot --> Specify_additional_parameters_for_scatterplot
    Define_contributions_to_variance --> Set_variance_and_std_dev
    Extract_demographic_distributions --> Merge
    When_clicking__Test_workflow_ --> SET_company_name
    Calculate_Z_Scores_and_Effect_Sizes --> Calculate_P_Scores
    Calculate_Z_Scores_and_Effect_Sizes --> Format_dataset_for_scatterplot
    Define_dictionary_of_demographic_keys --> ScrapingBee_Search_Glassdoor
    ScrapingBee_GET_company_page_contents --> Extract_reviews_page_url_path
    ScrapingBee_GET_Glassdoor_Reviews_Content --> Extract_Demographics_Module
    ScrapingBee_GET_Glassdoor_Reviews_Content --> Extract_Overall_Review_Summary
    Specify_additional_parameters_for_scatterplot --> Quickchart_Scatterplot
    Extract_overall_ratings_and_distribution_percentages --> Define_contributions_to_variance
```
