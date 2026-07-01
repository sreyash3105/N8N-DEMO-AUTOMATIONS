```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    getHubspotMessage["fas:fa-globe getHubspotMessage"]
    OpenAi_Create_Thread["fas:fa-globe OpenAi Create Thread"]
    OpenAI_Run["fas:fa-globe OpenAI Run"]
    Get_Run["fas:fa-globe Get Run"]
    Get_Last_Message["fas:fa-globe Get Last Message"]
    HTTP_Request["fas:fa-globe HTTP Request"]
    Completed__Action_or_Inprogress{"fas:fa-code-branch Completed, Action or Inprogress"}:::logic
    Wait["fas:fa-robot Wait"]
    Wait1["fas:fa-robot Wait1"]
    Submit_Data["fas:fa-globe Submit Data"]
    Select_Function{"fas:fa-code-branch Select Function"}:::logic
    Code1["fas:fa-cogs Code1"]
    Wait2["fas:fa-robot Wait2"]
    HTTP_Request1["fas:fa-globe HTTP Request1"]
    Code["fas:fa-cogs Code"]
    Submit_Data1["fas:fa-globe Submit Data1"]
    Wait3["fas:fa-robot Wait3"]
    respondHubspotMessage1["fas:fa-globe respondHubspotMessage1"]
    IF{"fas:fa-code-branch IF"}:::logic
    Airtable["fas:fa-robot Airtable"]
    IF1{"fas:fa-code-branch IF1"}:::logic
    createThread["fas:fa-robot createThread"]
    OpenAI_Run1["fas:fa-globe OpenAI Run1"]
    IF2{"fas:fa-code-branch IF2"}:::logic
    OpenAI(["fas:fa-robot OpenAI"]):::ai
    Webhook(("fas:fa-bolt Webhook")):::trigger

    IF --> Airtable
    IF1 --> OpenAi_Create_Thread
    IF1 --> OpenAI
    IF2 --> getHubspotMessage
    Code --> Submit_Data1
    Wait --> Get_Run
    Code1 --> Submit_Data
    Wait1 --> Get_Run
    Wait2 --> Get_Run
    Wait3 --> Get_Run
    OpenAI --> OpenAI_Run1
    Get_Run --> Completed__Action_or_Inprogress
    Webhook --> IF2
    Airtable --> IF1
    OpenAI_Run --> Get_Run
    OpenAI_Run1 --> Get_Run
    Submit_Data --> Wait2
    HTTP_Request --> Code1
    Submit_Data1 --> Wait3
    createThread --> OpenAI_Run
    HTTP_Request1 --> Code
    Select_Function --> HTTP_Request
    Select_Function --> HTTP_Request1
    Get_Last_Message --> respondHubspotMessage1
    getHubspotMessage --> IF
    OpenAi_Create_Thread --> createThread
    Completed__Action_or_Inprogress --> Get_Last_Message
    Completed__Action_or_Inprogress --> Select_Function
    Completed__Action_or_Inprogress --> Wait1
    Completed__Action_or_Inprogress --> Wait
```
