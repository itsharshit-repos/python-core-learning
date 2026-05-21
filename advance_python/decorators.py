# DECORATORS
# Modifying behaviour of function without without changing the original function code
# so, decorator are like a wrapper around the function. So under that hood, we can call other function.
# Example -
# def decorator(func):
#     def wrapper():
#         print("Before func")
#         func()
#         print("After func")
#     return wrapper
# SO, now suppose, func replaced by greet(): print("Hello")
# now, greet = decorator(greet) | greet()
# OUTPUT: 
# Before function
# Hello
# After function

# THIS IS MASSIVE IN BACKEND SYSTEMS
# Because now frameworks can automatically add:
# authentication
# logging
# monitoring
# rate limiting
# caching
# WITHOUT rewriting your business logic.

# Python gives shortcut syntax, so instead of: greet = decorator(greet)
# we can write:
# @decorator
# def greet():
#     print("Hello")     (SAME THING INTERNALLY)

# REAL EXAMPLE -
# Traditionally without decorator:- 
import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"time: {end-start}")
    return wrapper
# Now, with decorator:-
@timer
def task():
    print("running task")
    time.sleep(1)
task()

# SIMPLE EXAMPLE - AI Access Guard
# In AI engineering, calling an LLM costs money. You want to make sure a user has enough credit before letting them use the AI.
# Instead of writing a credit-checking if statement inside every single function, you write a decorator once and apply it using @.
def check_credit(func):
    def wrapper():
        user_credit = 10
        if user_credit <= 0:
            print("Access denied! You have 0 credit left.")
        else:
            func()
    return wrapper
# applying it
@check_credit
def call_ai_model():
    print("AI is thinking... Here is your answer!")
call_ai_model()

# IMPORTANT: Decorator helps in separation of concerns
# Meaning: business logic stays clean. Extra system behavior added separately.

# *ARGS, **KWARGS
# Sometime we want to pass arguments to function, but we dont know how many. That is why we use these, also when we call that 
# function, we dont know how many keywords we going to pass, so we use them.
# Simple example: flexible version
def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")
    return wrapper
# Now any function works
# '*args' collect positional arguments
def test(*args):
    print(args)
test(1,2,3,4)
# '**kwargs' collect keyword arguments
def test(**kwargs):
    print(kwargs)
test(name="Harshit", age=18)