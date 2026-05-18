# Basic AI Agent Management System
> This is a beginner backend-oriented Python project, a simple AI Agent Management System. Imagine a small control center where different AI agents exist, like a Research Agent and a Coding Agent. Each agent has its own identity - for example name, model, role, and current task. The system should let a user create new agents, view all existing agents, give them tasks, and save their information so that even after closing the program, the agents still “exist” when the system starts again. For example, you might create a ResearchBot using GPT-4, assign it the task “Analyze AI papers,” and later reopen the program and still see that agent and its task. The goal of this project is not just writing Python syntax. It is learning how real software systems manage entities, store state, organize behavior using OOP, and structure programs cleanly. This project is basically a tiny beginner version of how real AI systems and backend platforms manage agents, tools, users, or services internally.

#### I built this to practise OOPs, JSON persistance, and Python and Backend fundamentals. While building it, I faced many challenges as a beginner, but ultimately solving every problem, here is my final version of this system. 

## Features
#### With by system, a user can:
- Create Agent
- Store Agent
- View Agent

## Concepts used
#### I used python fundamentals like:
- Object Oriented Programming (OOPs)
- Functions
- Data Structures
- Loops
- JSON
- File Handling
- Exception Handling

## Project Structure
```text
└──AIAgent_management_system
        ├── main.py
        ├── agent_info.json
        └── README.md   
```

## Future Improvements
- Add delete/update agent
- Add database storage
- Add authentication
- Convert to FastAPI backend
- Add logging system