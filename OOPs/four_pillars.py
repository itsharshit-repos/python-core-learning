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

#---------------------------------------------------------------------------------------------------------------------------------

# ABSTRACTION
# Show only necessary behaviour, hide implementation details
# Think like in a system of payment, using this, user can only pay with card, or upi but whats going inside, then function they 
# dont know.
# Rules of Abstraction in Code:
# 1) You create a "blueprint" class that defines what functions must exist, but it doesn't write the code for them.
# 2) You cannot create an object directly from this blueprint class.
# 3) Any real class that inherits from this blueprint must write the actual code for those functions, or Python will throw an error
# Example:
class AIModel:
    def generate_response(self):
        pass
class GPTModel(AIModel):
    def generate_response(self):
        print("GPT generating response...")
class ClaudeModel(AIModel):
    def generate_response(self):
        print("Claude generating response...")
gpt = GPTModel()
cld = ClaudeModel()
gpt.generate_response()
cld.generate_response()
# Above is okay, but the professional version is:
from abc import ABC, abstractmethod
class AIModel(ABC):
    @abstractmethod
    def generate_response(self):
        pass
class GPTModel(AIModel):
    def generate_response(self):
        print("GPT generating response...")
class ClaudeModel(AIModel):
    def generate_response(self):
        print("Claude generating response...")
gpt = GPTModel()
cld = ClaudeModel()
gpt.generate_response()
cld.generate_response()
# Now: you CANNOT directly create AIModel()
#   > child classes MUST implement generate_response()
#   > This enforces architecture rules.
# VERY important in enterprise systems.

# A real life project example:--------------------------------------------------------------------------
from abc import ABC, abstractmethod  # important to import 
import time
# =====================================================================
# 1. THE ABSTRACT CONTRACT (The Blueprint)
# =====================================================================
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """
        Every single payment method MUST have this exact function.
        We don't write the code here, we just enforce the rule.
        """
        pass
# =====================================================================
# 2. REAL IMPLEMENTATIONS (The Complex Gears Hidden Under the Hood)
# =====================================================================
class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        # Specific complex logic for Credit Cards
        print("\n[Credit Card Engine] Connecting to bank networks...")
        time.sleep(0.5)
        print(f"Securely charged ${amount} to your Card.")
        return True
class PayPalPayment(PaymentGateway):
    def process_payment(self, amount):
        # Totally different complex logic for PayPal
        print("\n[PayPal Engine] Redirecting user to paypal.com login...")
        time.sleep(0.5)
        print(f"Verification successful! PayPal sent ${amount}.")
        return True
# =====================================================================
# 3. THE REUSABLE SYSTEM (Your AI Project Core)
# =====================================================================
class AISystem:
    def __init__(self):
        self.user_credits = 0
    def add_credit_workflow(self, gateway_object, amount_to_add):
        """
        Look at this function! It knows absolutely NOTHING about Credit Cards 
        or PayPal. It only knows that whatever 'gateway_object' is passed in, 
        it guarantees a '.process_payment()' button exists because of abstraction.
        """
        # Call the abstract method contract
        success = gateway_object.process_payment(amount_to_add)
        if success:
            self.user_credits += amount_to_add
            print(f"[System] Credits updated. Current Balance: {self.user_credits}")
# =====================================================================
# --- RUNNING THE CODE ---
# =====================================================================
app = AISystem()
# The user chooses Credit Card
card_engine = CreditCardPayment()
app.add_credit_workflow(card_engine, 5)
# Next time, the user chooses PayPal
paypal_engine = PayPalPayment()
app.add_credit_workflow(paypal_engine, 10)

# CODING TASK: 
# Create: class PaymentSystem
# using: ABC, abstractmethod
# Then create: UPI, CreditCard classes.
# Both should implement: pay(amount)
# Then: upi.pay(500), card.pay(1000)
# Print different payment messages.
from abc import ABC, abstractmethod
import time
@abstractmethod
class PaymentSystem(ABC):
    def pay(self, amount):
        pass
class UPI(PaymentSystem):
    def pay(self, amount):
        print("[UPI engine] verifying user and making transaction...")
        time.sleep(1.0)
        print(f"Verification successful! Payment done of amount: Rs.{amount}")
        return True
class CreditCard(PaymentSystem):
    def pay(self, amount):
        print("[Credit Card engine] Connecting to bank networks...")
        time.sleep(1.0)
        print(f"Securely charged ${amount} to your Card.")
        return True
upi = UPI()
upi.pay(500)
card = CreditCard()
card.pay(1000)