import json

FILE_NAME = "agent_info.json"
class Agent:
    def __init__(self, name, model, domain, task):
        self.name = name
        self.model = model
        self.domain = domain
        self.task = task
    def show_info(self):
        print(f"Your created Agent:\nName: {self.name}\nModel: {self.model}\nDomain: {self.domain}\nTask: {self.task}")
    def to_dict(self):
         return {
              "Name": self.name,
              "Model": self.model,
              "Domain": self.domain,
              "Task": self.task
         }

def view_agent():
    with open(FILE_NAME, "r") as f:
        data = json.load(f)
    return data

while True:
    print("----Welcome to AGENT MANAGEMENT SYSTEM----")
    print("Hi User, Please select the option below: ")
    print("1. Create Agent\n2. View all created agent")
    print("3. Exit")
    choice = input("Enter the option number to proceed: ").strip().lower()

    if choice == 'exit' or choice == '3':
        print("Thanks for using. Have a nice day!")
        break

    elif choice == '1':
        name = input("Enter name for your agent: ")
        model = input("Enter your preferred model: ")
        domain = input("Enter your agent domain: ")
        task = input("Enter the task done by your agent: ")
        a = Agent(name, model, domain, task)
        a.show_info()

        # Now storing the data into json format
        data = a.to_dict()
        try:
            with open(FILE_NAME, "r") as f:
                existing_agents = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_agents = []
        # append new agent data
        existing_agents.append(data)
        try:
            with open(FILE_NAME, "w") as f:
                json.dump(existing_agents, f, indent=4)
            print("Agent has been successfully created!")
        except PermissionError:
             print("System error: Do not have permission to write to 'agent_info.json'.")
        except Exception as e:
             print(f"An unexpected system error occured while saving: {e}")

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