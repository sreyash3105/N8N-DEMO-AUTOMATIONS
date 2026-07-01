```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    Zip_Entries["Zip Entries"]
    Extract_Reviews["Extract Reviews"]
    Reviews_to_List["Reviews to List"]
    Default_Data_Loader["Default Data Loader"]
    Recursive_Character_Text_Splitter["Recursive Character Text Splitter"]
    Embeddings_OpenAI(["Embeddings OpenAI"]):::ai
    Set_Variables["Set Variables"]
    Get_Payload_of_Points["Get Payload of Points"]
    Clusters_To_List["Clusters To List"]
    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    Only_Clusters_With_3__points["Only Clusters With 3+ points"]
    Set_Variables1["Set Variables1"]
    Find_Reviews["Find Reviews"]
    Prep_Output_For_Export["Prep Output For Export"]
    Export_To_Sheets["Export To Sheets"]
    Clear_Existing_Reviews["Clear Existing Reviews"]
    Trigger_Insights["Trigger Insights"]
    Prep_Values_For_Trigger["Prep Values For Trigger"]
    Execute_Workflow_Trigger(("Execute Workflow Trigger")):::trigger
    Get_TrustPilot_Page["Get TrustPilot Page"]
    Qdrant_Vector_Store["Qdrant Vector Store"]
    Apply_K_means_Clustering_Algorithm["Apply K-means Clustering Algorithm"]
    Customer_Insights_Agent["Customer Insights Agent"]

    Zip_Entries --> Reviews_to_List
    Find_Reviews --> Apply_K_means_Clustering_Algorithm
    Set_Variables --> Clear_Existing_Reviews
    Set_Variables1 --> Find_Reviews
    Extract_Reviews --> Zip_Entries
    Reviews_to_List --> Qdrant_Vector_Store
    Clusters_To_List --> Only_Clusters_With_3__points
    Embeddings_OpenAI --> Qdrant_Vector_Store
    OpenAI_Chat_Model --> Customer_Insights_Agent
    Default_Data_Loader --> Qdrant_Vector_Store
    Get_TrustPilot_Page --> Extract_Reviews
    Qdrant_Vector_Store --> Prep_Values_For_Trigger
    Get_Payload_of_Points --> Customer_Insights_Agent
    Clear_Existing_Reviews --> Get_TrustPilot_Page
    Prep_Output_For_Export --> Export_To_Sheets
    Customer_Insights_Agent --> Prep_Output_For_Export
    Prep_Values_For_Trigger --> Trigger_Insights
    Execute_Workflow_Trigger --> Set_Variables1
    Only_Clusters_With_3__points --> Get_Payload_of_Points
    Recursive_Character_Text_Splitter --> Default_Data_Loader
    When_clicking__Test_workflow_ --> Set_Variables
    Apply_K_means_Clustering_Algorithm --> Clusters_To_List
```
