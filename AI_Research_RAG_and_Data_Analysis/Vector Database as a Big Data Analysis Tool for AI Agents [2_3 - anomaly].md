```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("When clicking ‘Test workflow’")):::trigger
    Total_Points_in_Collection["Total Points in Collection"]
    Cluster_Distance_Matrix["Cluster Distance Matrix"]
    Scipy_Sparse_Matrix["Scipy Sparse Matrix"]
    Set_medoid_id["Set medoid id"]
    Get_Medoid_Vector["Get Medoid Vector"]
    Prepare_for_Searching_Threshold["Prepare for Searching Threshold"]
    Searching_Score["Searching Score"]
    Threshold_Score["Threshold Score"]
    Set_medoid_threshold_score["Set medoid threshold score"]
    Split_Out1["Split Out1"]
    Merge["Merge"]
    Textual__visual__crop_descriptions["Textual (visual) crop descriptions"]
    Embed_text["Embed text"]
    Get_Medoid_by_Text["Get Medoid by Text"]
    Set_text_medoid_id["Set text medoid id"]
    Prepare_for_Searching_Threshold1["Prepare for Searching Threshold1"]
    Threshold_Score1["Threshold Score1"]
    Searching_Text_Medoid_Score["Searching Text Medoid Score"]
    Medoids_Variables["Medoids Variables"]
    Text_Medoids_Variables["Text Medoids Variables"]
    Qdrant_cluster_variables["Qdrant cluster variables"]
    Info_About_Crop_Clusters["Info About Crop Clusters"]
    Crop_Counts["Crop Counts"]
    Split_Out["Split Out"]
    Set_text_medoid_threshold_score["Set text medoid threshold score"]

    Merge --> Embed_text
    Split_Out --> Cluster_Distance_Matrix
    Split_Out --> Merge
    Embed_text --> Get_Medoid_by_Text
    Split_Out1 --> Merge
    Crop_Counts --> Info_About_Crop_Clusters
    Searching_Score --> Threshold_Score
    Threshold_Score --> Set_medoid_threshold_score
    Threshold_Score1 --> Set_text_medoid_threshold_score
    Get_Medoid_Vector --> Prepare_for_Searching_Threshold
    Medoids_Variables --> Total_Points_in_Collection
    Get_Medoid_by_Text --> Set_text_medoid_id
    Get_Medoid_by_Text --> Prepare_for_Searching_Threshold1
    Scipy_Sparse_Matrix --> Set_medoid_id
    Scipy_Sparse_Matrix --> Get_Medoid_Vector
    Text_Medoids_Variables --> Textual__visual__crop_descriptions
    Cluster_Distance_Matrix --> Scipy_Sparse_Matrix
    Info_About_Crop_Clusters --> Split_Out
    Qdrant_cluster_variables --> Medoids_Variables
    Qdrant_cluster_variables --> Text_Medoids_Variables
    Total_Points_in_Collection --> Crop_Counts
    Searching_Text_Medoid_Score --> Threshold_Score1
    Prepare_for_Searching_Threshold --> Searching_Score
    Prepare_for_Searching_Threshold1 --> Searching_Text_Medoid_Score
    When_clicking__Test_workflow_ --> Qdrant_cluster_variables
    Textual__visual__crop_descriptions --> Split_Out1
```
