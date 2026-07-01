```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Stop_Interview_{"fas:fa-code-branch Stop Interview?"}:::logic
    Generate_Row["fas:fa-cogs Generate Row"]
    Generate_Row1["fas:fa-cogs Generate Row1"]
    Clear_For_Next_Interview[("fas:fa-robot Clear For Next Interview")]
    Send_Reply_To_Agent["fas:fa-robot Send Reply To Agent"]
    Start_Interview(("fas:fa-bolt Start Interview")):::trigger
    Get_Answer["fas:fa-cogs Get Answer"]
    Set_Interview_Topic["fas:fa-cogs Set Interview Topic"]
    UUID["fas:fa-cogs UUID"]
    Generate_Row2["fas:fa-cogs Generate Row2"]
    Create_Session["fas:fa-cogs Create Session"]
    Update_Session["fas:fa-cogs Update Session"]
    Update_Session1["fas:fa-cogs Update Session1"]
    Update_Session2["fas:fa-cogs Update Session2"]
    Valid_Session_{"fas:fa-code-branch Valid Session?"}:::logic
    Respond_to_Webhook(("fas:fa-bolt Respond to Webhook")):::trigger
    Window_Buffer_Memory2[("fas:fa-robot Window Buffer Memory2")]
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    Redirect_to_Completion_Screen["fas:fa-cogs Redirect to Completion Screen"]
    Webhook(("fas:fa-bolt Webhook")):::trigger
    n_404_Not_Found["fas:fa-cogs 404 Not Found"]
    AI_Researcher["fas:fa-robot AI Researcher"]:::ai
    Parse_Response["fas:fa-cogs Parse Response"]
    Groq_Chat_Model["fas:fa-robot Groq Chat Model"]
    Show_Transcript["fas:fa-cogs Show Transcript"]
    Save_to_Google_Sheet["fab:fa-google Save to Google Sheet"]
    Session_to_List["fas:fa-cogs Session to List"]
    Messages_To_JSON["fas:fa-cogs Messages To JSON"]
    Query_By_Session["fas:fa-cogs Query By Session"]
    Get_Session["fas:fa-cogs Get Session"]

    UUID --> Create_Session
    Webhook --> Query_By_Session
    Get_Answer --> Generate_Row
    Get_Session --> Session_to_List
    Generate_Row --> Update_Session1
    n_404_Not_Found --> Respond_to_Webhook
    AI_Researcher --> Parse_Response
    Generate_Row1 --> Update_Session2
    Generate_Row2 --> Update_Session
    Create_Session --> Generate_Row2
    Parse_Response --> Stop_Interview_
    Update_Session --> Set_Interview_Topic
    Valid_Session_ --> Show_Transcript
    Valid_Session_ --> n_404_Not_Found
    Groq_Chat_Model --> AI_Researcher
    Session_to_List --> Messages_To_JSON
    Show_Transcript --> Respond_to_Webhook
    Start_Interview --> UUID
    Stop_Interview_ --> Generate_Row1
    Stop_Interview_ --> Get_Answer
    Update_Session1 --> Send_Reply_To_Agent
    Update_Session2 --> Clear_For_Next_Interview
    Messages_To_JSON --> Save_to_Google_Sheet
    Query_By_Session --> Valid_Session_
    Send_Reply_To_Agent --> AI_Researcher
    Set_Interview_Topic --> AI_Researcher
    Window_Buffer_Memory --> Clear_For_Next_Interview
    Window_Buffer_Memory2 --> AI_Researcher
    Clear_For_Next_Interview --> Redirect_to_Completion_Screen
    Redirect_to_Completion_Screen --> Get_Session
```
