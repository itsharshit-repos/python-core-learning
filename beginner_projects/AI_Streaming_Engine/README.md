# CLI Based AI Streaming Engine
## Project Overview
> This is a beginner-level CLI based **AI Streaming Engine**, a small system that simulates how modern AI platforms like ChatGPT stream responses in real time instead of waiting to generate the full answer at once. The system should behave like a tiny AI backend service where a user sends a prompt, the engine checks whether the user has enough credits to access the model, and then gradually streams the response token-by-token using Python generators. The project should feel like a lightweight inference engine - managing credits, handling access control with decorators, generating streamed responses, and separating logic into reusable modules instead of writing everything in one place. The purpose of this project is not just learning generators or decorators individually, but understanding how real AI systems combine streaming, state management, modular architecture, backend control flow, and user experience together. Conceptually, this project is a beginner simulation of how modern LLM APIs, inference servers, and AI platforms stream outputs, manage usage limits, and structure backend response pipelines internally.

## Features
#### With this system, a user can:
- Login 
- Use mock DEMO LLM
- Credit system
- Add Credit

## Concept used and what I learned
- Python fundamentals (conditional statements, loops, data structures, etc)
- OOPs
- Decorators
- Generators
- State management
    - user session
    - credits
    - authentication
    - runtime flow
- Architecture thinking
- Control flow
    - flow management
    - menus
    - retry systems
    - validation loops

## Project Structure
```text
└──AI_Streaming_Engine
        ├── main.py
        └── README.md   
```

## Future Improvements
- Version 3
    - Save users in JSON
    - Multiple accounts
    - Chat history
    - Logging
- Version 4
    - FastAPI backend
    - REST APIs
    - async streaming
- Version 5
    - Database
    - PostgreSQL
    - Auth tokens
    - Redis
    - Deployment
- Version 6
    - Real LLM API
    - Streaming responses
    - Rate limiting
    - Observability