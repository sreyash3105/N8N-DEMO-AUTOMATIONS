```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    OpenAI_Chat_Model(["fas:fa-robot OpenAI Chat Model"]):::ai
    OpenAI_Chat_Model1(["fas:fa-robot OpenAI Chat Model1"]):::ai
    OpenAI_Chat_Model3(["fas:fa-robot OpenAI Chat Model3"]):::ai
    OpenAI_Chat_Model4(["fas:fa-robot OpenAI Chat Model4"]):::ai
    Schedule_Trigger(("fas:fa-bolt Schedule Trigger")):::trigger
    Get_Issue_Comments["fas:fa-cogs Get Issue Comments"]
    Close_Issue["fas:fa-cogs Close Issue"]
    Send_Reminder["fas:fa-cogs Send Reminder"]
    Join_Comments["fas:fa-cogs Join Comments"]
    Add_Autoclose_Message["fas:fa-cogs Add Autoclose Message"]
    Ask_For_Feedback_Message["fas:fa-cogs Ask For Feedback Message"]
    Simplify_Thread_For_AI["fas:fa-cogs Simplify Thread For AI"]
    Solution_Found_{"fas:fa-code-branch Solution Found?"}:::logic
    Reply_to_Issue["fas:fa-cogs Reply to Issue"]
    Last_Message_is_Not_Bot{"fas:fa-code-branch Last Message is Not Bot"}:::logic
    Structured_Output_Parser["fas:fa-robot Structured Output Parser"]
    Get_Issue_Metadata["fas:fa-cogs Get Issue Metadata"]
    Notify_Slack_Channel["fab:fa-slack Notify Slack Channel"]
    Close_Issue2["fas:fa-cogs Close Issue2"]
    Get_List_of_Unresolved_Long_Lived_Issues["fas:fa-cogs Get List of Unresolved Long Lived Issues"]
    Execute_Workflow["fas:fa-cogs Execute Workflow"]
    Execute_Workflow_Trigger(("fas:fa-bolt Execute Workflow Trigger")):::trigger
    Customer_Satisfaction_Agent["fas:fa-robot Customer Satisfaction Agent"]
    KnowledgeBase_Agent["fas:fa-robot KnowledgeBase Agent"]:::ai
    Issue_Reminder_Agent(["fas:fa-robot Issue Reminder Agent"]):::ai
    Find_Simlar_Issues["fas:fa-cogs Find Simlar Issues"]
    Query_KnowledgeBase["fas:fa-cogs Query KnowledgeBase"]
    Report_Unhappy_Resolution["fab:fa-slack Report Unhappy Resolution"]
    Classify_Current_Issue_State{"fas:fa-robot Classify Current Issue State"}:::logic

    Join_Comments --> Simplify_Thread_For_AI
    Reply_to_Issue --> Close_Issue2
    Solution_Found_ --> Reply_to_Issue
    Solution_Found_ --> Notify_Slack_Channel
    Schedule_Trigger --> Get_List_of_Unresolved_Long_Lived_Issues
    OpenAI_Chat_Model --> Classify_Current_Issue_State
    Find_Simlar_Issues --> KnowledgeBase_Agent
    Get_Issue_Comments --> Join_Comments
    Get_Issue_Metadata --> Get_Issue_Comments
    OpenAI_Chat_Model1 --> KnowledgeBase_Agent
    OpenAI_Chat_Model3 --> Issue_Reminder_Agent
    OpenAI_Chat_Model4 --> Customer_Satisfaction_Agent
    KnowledgeBase_Agent --> Solution_Found_
    Query_KnowledgeBase --> KnowledgeBase_Agent
    Issue_Reminder_Agent --> Send_Reminder
    Notify_Slack_Channel --> Reply_to_Issue
    Add_Autoclose_Message --> Close_Issue
    Simplify_Thread_For_AI --> Classify_Current_Issue_State
    Last_Message_is_Not_Bot --> Issue_Reminder_Agent
    Ask_For_Feedback_Message --> Close_Issue
    Execute_Workflow_Trigger --> Get_Issue_Metadata
    Structured_Output_Parser --> KnowledgeBase_Agent
    Customer_Satisfaction_Agent --> Ask_For_Feedback_Message
    Customer_Satisfaction_Agent --> Add_Autoclose_Message
    Customer_Satisfaction_Agent --> Report_Unhappy_Resolution
    Classify_Current_Issue_State --> Customer_Satisfaction_Agent
    Classify_Current_Issue_State --> Last_Message_is_Not_Bot
    Classify_Current_Issue_State --> KnowledgeBase_Agent
    Get_List_of_Unresolved_Long_Lived_Issues --> Execute_Workflow
```
