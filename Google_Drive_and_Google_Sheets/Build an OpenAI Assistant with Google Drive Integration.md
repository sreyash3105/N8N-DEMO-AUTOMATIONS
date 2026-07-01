```mermaid
graph TD
    classDef trigger fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef ai fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef logic fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    When_clicking__Test_workflow_(("fas:fa-bolt When clicking ‘Test workflow’")):::trigger
    Google_Drive["fab:fa-google Google Drive"]
    When_chat_message_received(("fas:fa-robot When chat message received")):::trigger
    Window_Buffer_Memory[("fas:fa-robot Window Buffer Memory")]
    OpenAI(["fas:fa-robot OpenAI"]):::ai
    OpenAI2(["fas:fa-robot OpenAI2"]):::ai
    OpenAI1(["fas:fa-robot OpenAI1"]):::ai
    OpenAI_Assistent(["fas:fa-robot OpenAI Assistent"]):::ai

    OpenAI2 --> OpenAI1
    Google_Drive --> OpenAI2
    Window_Buffer_Memory --> OpenAI_Assistent
    When_chat_message_received --> OpenAI_Assistent
    When_clicking__Test_workflow_ --> OpenAI
    When_clicking__Test_workflow_ --> Google_Drive
```
