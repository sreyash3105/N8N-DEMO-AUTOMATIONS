```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    OpenAI_Chat_Model(["OpenAI Chat Model"]):::ai
    MongoDBAggregate["MongoDBAggregate"]
    Window_Buffer_Memory[("Window Buffer Memory")]
    When_chat_message_received(("When chat message received")):::trigger
    insertFavorite["insertFavorite"]
    AI_Agent___Movie_Recommendation["AI Agent - Movie Recommendation"]:::ai

    insertFavorite --> AI_Agent___Movie_Recommendation
    MongoDBAggregate --> AI_Agent___Movie_Recommendation
    OpenAI_Chat_Model --> AI_Agent___Movie_Recommendation
    Window_Buffer_Memory --> AI_Agent___Movie_Recommendation
    When_chat_message_received --> AI_Agent___Movie_Recommendation
```
