import json
import os

class Agent:
    def __init__(self, name, model, domain, task):
        self.name = name
        self.model = model
        self.domain = domain
        self.task = task
    def show_info(self):
        print(f"Your created Agent:\nName: {self.name}\nModel: {self.model}\nDomain: {self.domain}\nTask: {self.task}")

def view_agent():
            with open("agent_info.json", "r") as f:
                data = json.load(f)
            return data

class FileNotCreated(Exception):
     pass

while True:
    print("----Welcome to AGENT MANAGEMENT SYSTEM----")
    print("Hi User, Please select the option below: ")
    print("1. Create Agent\n2. View all created agent")
    print("3. Exit")
    choice = input("Enter the option number to proceed: ").strip().lower()

    if choice == 'exit' or choice == '3':
        print("Goodbye!")
        break

    elif choice == '1':
        name = input("Enter name for your agent: ")
        model = input("Enter your preferred model: ")
        domain = input("Enter your agent domain: ")
        task = input("Enter the task done by your agent: ")
        a = Agent(name, model, domain, task)
        a.show_info()
        # Now storing the data into json format
        data = {
            "Name": a.name,
            "Model": a.model,
            "Domain": a.domain,
            "Task": a.task
        }
        try:
            if os.path.exists("agent_info.json"):
                with open("agent_info.json", "r") as f:
                    existing_agents = json.load(f)
            else:
                existing_agents = []
            existing_agents.append(data)
            with open("agent_info.json", "w") as f:
                json.dump(existing_agents, f, indent=4)
            print("Agent has been successfully created!")
        except FileNotCreated as e:
             print(f"File cannot be created: {e}")

    elif choice == '2':
        try:
            print("Here is your list of Agents:\n")
            agent_list = view_agent()
            for agent in agent_list:
                 print(f"Name: {agent['Name']}")
                 print(f"Model: {agent['Model']}")
                 print(f"Domain: {agent['Domain']}")
                 print(f"Task: {agent['Task']}")
                 print("-"*60)
        except FileNotFoundError:
             print("Error: File 'agent_info.json' does not exist!")
        except json.JSONDecodeError:
             print("Error: The storage file is corrupted or empty and cannot be read.")

    else:
        print("Enter a valid option number from above.")