import json
import os

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
        try:
            name = input("Enter name for your agent: ")
            model = input("Enter your preferred model: ")
            domain = input("Enter your agent domain: ")
            task = input("Enter the task done by your agent: ")
            class Agent:
                def __init__(self, name, model, domain, task):
                    self.name = name
                    self.model = model
                    self.domain = domain
                    self.task = task
                def create_agent(self):
                    print(f"Your created Agent:\nName: {self.name}\nModel: {self.model}\nDomain: {self.domain}\nTask: {self.task}")
            a = Agent(name, model, domain, task)
            a.create_agent()
            # Now storing the data into json format
            data = {
                "Name": a.name,
                "Model": a.model,
                "Domain": a.domain,
                "Task": a.task
            }
            if os.path.exists("agent_info.json"):
                with open("agent_info.json", "r") as f:
                    existing_agents = json.load(f)
            else:
                existing_agents = []
            existing_agents.append(data)
            with open("agent_info.json", "w") as f:
                json.dump(existing_agents, f, indent=4)
            print("Agent has been successfully created!")
        except ValueError:
            print("Server not responding. Sorry for the interruption, we will get back to you soon. Thank you for the patience.")
    elif choice == '2':
        def view_agent():
            with open("agent_info.json", "r") as f:
                data = json.load(f)
            print(data)
        print("Here is your list of Agents:")
        view_agent()
    else:
        print("Enter a valid option number from above.")