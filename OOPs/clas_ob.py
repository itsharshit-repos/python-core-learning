# CLASS: it is the blueprint. Define structure, expected data, behaviour.
# OBJECT: instance created from class, actual memory entity, with its own state/data. (eg. User, Agent, etc)
# METHOD: behaviour or action (eg. save(), response(), etc)

# First Class -
class Student:
    pass
# Creating Object -
s1 = Student()  # now s1 is object (instance)
# Adding Attributes -
s1.name = "Harshit"  # 'name' is Data attached to object
s1.skill = "python"
print(s1.name)

# Better way! CONSTRUCTOR (__init__). Instead of manually assigning attributes everytime, __init__ runs automatically everytime,
# when object created.
# Constructor solves: repetitive setup, initialization consistency, object safety
# EXAMPLE -
class Student:
    def __init__(self, name, skill):
        self.name = name 
        self.skill = skill
# creating object
s1 = Student("Harshit","Python")
# accessing data
print(s1.name)
print(s1.skill)

# What is 'Self'?
# self means current object itself. Example: s1 = Student("Harshit","Python")
# inside constructor: self   refers to: s1
# self.name = name MEANS store data inside this object
# Why needed? Because many object can exist. Each object stores separate data. 'Self' identifies which object.

# ADDING METHODS: Object also have behaviour
class Student:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, {self.name}")
s1 = Student("Harshit")
s1.greet()

# Coding Task — Mini Real System
# Create class: AIAgent
# Requirements: Constructor
# Store: name, model, 
# Method: introduce()
# Output: Agent Researcher uses GPT-4
# Create TWO objects, Examples:
# Researcher
# CodingAgent
# Call introduce() for both
class AIAgent:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def introduce(self):  # method
        print(f"Agent {self.name} uses {self.model}")
research_agent = AIAgent("Researcher", "GPT-4")  # object
coding_agent = AIAgent("CodingAgent", "Claude")  # object
research_agent.introduce()
coding_agent.introduce()

# --- INSTANCE VARIABLE v/s CLASS VARIABLE ---
# important because many system need: shared data, object specific data, etc

# INSTANCE VARIABLE: Data unique to each object (belongs to individual object)
# example: self.name, self.model, EACH object stores seperate values
# EXAMPLE -
a1 = AIAgent("Research", "GPT-4")
a2 = AIAgent("Code", "Claude")
# Different data per object

# CLASS VARIABLE: Shared across all objects. Defined directly inside class
# example: 
class Software:
    company = "Google"
# NOW all object can access; a1.company, a2.company

# EXAMPLE PROGRAM :
class Robot:
    type = "AI"
    def __init__(self, name):
        self.name = name
r1 = Robot("Jarvis")
print(r1.type)
print(r1.name)
# Coding Task
# Create class: AIModel
# Requirements: Class Variable, category = "LLM", Constructor
# Store: name, company
# Method: show()
# Output example: GPT-4 by OpenAI belongs to LLM
# Create TWO objects: GPT-4, Claude
# Call: show() for both.
class AIModel:
    category = "LLM"
    def __init__(self, name, company):
        self.name = name
        self.company = company
    def show(self):
        print(f"{self.name} by {self.company} belongs to {self.category}")
gpt = AIModel("GPT-4","OpenAI")
claude = AIModel("Claude", "Anthropic")
gpt.show()
claude.show()