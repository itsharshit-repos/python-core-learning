# INHERITANCE: 
# Inheritance is where the object relationship begins
# Suppose you created some classes, all of them have name, model, etc so would repeating same code make sense?
# To solve this, so we use Inheritance
# CORE IDEA: A child class can reuse, extend, modify behaviour/data from parent class
# Inheritance example: 
class Agent:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"I am {self.name}")
# child class
class CodingAgent(Agent): 
    def code(self):
        print("writing code...")
# CodingAgent automatically gets: constructor, methods, attributes from 'Agent'
c1 = CodingAgent("CodeBot")
c1.introduce()  # even though introduce() never written inside child class
# Adding extra features in child class works too!
c1.code()

# super() - Suppose child class wants parent constructor too
class Agent:
    def __init__(self, name):
        self.name = name
class CodingAgent:
    def __init__(self, name, language):
        super().__init__(name)   # means run parent constructor first
        self.language = language
# Coding Task — 
# Create parent class: Agent
# Constructor: name
# Method: introduce()
# Output: I am ResearchBot
# Create child class: ResearchAgent
# Extra:
# field: domain
# Method: research()
# Output: Researching AI Systems
# Use: inheritance, super(), object creation, both methods
class Agent:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"I am {self.name}")
class ResearchAgent(Agent):
    def __init__(self, name, domain):
        super().__init__(name)
        self.domain = domain
    def research(self):
        print(f"Researching {self.domain}")
c1 = ResearchAgent("ResearchBot", "AI System")
c1.introduce()
c1.research()

#--------------------------------------------------------------------------------------------------------------------------------

# METHOD OVERRIDING: Child class can replace parent behaviour
class Agent:
    def work(self):
        print("Agent working")
class CodingAgent(Agent):
    def work(self):
        print("Writing code")
c1 = CodingAgent()
c1.work()
# Important because specialized behaviour, customised implementation while still sharing same interface.

#------------------------------------------------------------------------------------------------------------------------------

# POLYMORPHISM: Same method name, different behaviour
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
animals = [Dog(), Cat()]
for a in animals:
    a.sound()
# System can treat many ojects uniformly. Example: agent.respond() without caring whether -
# coding agent, research agent, vision agent. Internally each behaves differently .
# Coding Task — 
# Create parent class: Agent
# Method: task()
# prints: Agent performing task
# Create TWO child classes: 
# --- CodingAgent
# Override: task()
# Output: Writing backend code
# --- ResearchAgent -
# Override: task()
# Output: Researching AI papers
# Then: create list of objects
# loop through them
# call: task()
class Agent:
    def task(self):
        print("Agent performing task")
class CodingAgent(Agent):
    def task(self):
        print("Writing backend code")
class ResearchAgent(Agent):
    def task(self):
        print("Researching AI papers")
object = [Agent(), CodingAgent(), ResearchAgent()]
for obj in object:
    obj.task()

#-----------------------------------------------------------------------------------------------------------------------------

# ENCAPSULATION:
# hiding/protecting internal state and controlling access
# larger system needs: controlled access validation, protection so we use ENCAPSULATION
# Python does not have true private variables BUT it has conventions
# 1) _ (Single underscore) eg. self._token MEANS "Internal use only"
# 2) __ (double underscore) eg. self.__password MEANS triggers name mangling, making direct access harder 
# example:
# class User:
#     def __init__(self, password):
#         self.__password = password
# u = User("secret")
# print(u.__password)
# AND now this fails! because system should NOT allow -
# arbitary modification, unsafe access, invalid states
# GETTER & SETTER: controlled access methods
class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        self.__balance += amount if amount > 0 else print("Invalid amount")
    def get_balance(self):
        return self.__balance
# Better because instead of account.balance = -999, system forces validation through methods.
# Coding Task — Secure AI Config
# Create class: AIConfig
# Requirements: Private Variable - __api_key
# Constructor: Store - api key
# Method: show_key() prints key.
# Method: update_key(new_key)
# updates key ONLY IF: length > 5
# Otherwise print: Invalid API key
# Create Object: show key, update key, show again
class AIConfig:
    def __init__(self):
        self.__api_key = 112233
    def show_key(self):
        return self.__api_key
    def update_key(self, new_key):
        if len(str(new_key)) > 5:
            self.__api_key = new_key
        else:
            print("Invalid API key.")
k1 = AIConfig()
print(k1.show_key())
k1.update_key(102599)
print(k1.show_key())
k2 = AIConfig()
print("---Testing invalid API key---")
k2.update_key(123)
print(f"Current key remains: {k2.show_key()}")
    