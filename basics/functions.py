# functions are the block of code with makes the program reusable. You can contain your code block and call them whenever
# you need them.
# function is resuable, testable, predictable and reduces complexity. Example:
def square(x):
    return x*x
print(square(5))
# why written return instead of print because print() displys but 'return' gives data back.
# returned valued can travel through systems.

# Parameters and argument
def greet(name):
    print("Hello", name)
greet("Harshit")
# Here above, 'name' is parameter and 'Harshit' is an argument

# Scope in functions
# If you keep your toothbrush inside bathroom: bathroom can access it, kitchen cannot directly access it. Variables work similarly.
# variables created "outside" of function are GLOBAL variables
def test():
    age = 18
    print(age)
test()
# now here the age is "inside" the function so it is called LOCAL scope
# same variable example, and they both will not collide.
x = 100
def test():
    x = 50
    print(x)
test()
print(x)    # prints the output as 50, 100

# Question: Write a function: creates local variable movie, returns movie name, store returned value in another variable, 
# print that variable outside
def m():
    movie = "Harry potter"
    return movie
print(m())

# LAMBDA function: Suppose you want a tiny function, normal way would be:
def square(x):
    return x*x
# works perfectly. But sometimes, functions are very small and used one time, and to solve that we have a shortcut syntax lambda
# A lambda is a small anonymous function, anonymous means function without a normal name definition.
# Example: 1) Normal function
def add(a, b):
    return a+b
# Lambda version
lambda a,b: a+b  # means "lambda parameters: expression" like lambda x: x*2 means takes x and return x*2
# How do we use it;
square = lambda x: x*x
print(square(5))
# lambda is bad for readability so for bigger functions, always prioritize normal def, and for one liner, use lambda
# In a lambda, the result of the expression is returned automatically. You should never write the word return.
# Question: write a function using lambda to compare and return the smaller value
compare = lambda a, b: a if a<b else b
print(compare(2, 4))

# RECURSION:
# Simple definition, a function calling itself, but this can create infinite recursion as it can call itself forever
# So recursion needs: 1) stopping condition and 2) repeated smaller works. These 2 are the core ideas
# Basic recursion example:
def countdown(n):
    if n == 0:   # this is the base case, very important and act as a stopping condition
        return
    print(n)
    countdown(n-1)  # recursive case, function calling itself
countdown(5)
# In this above example, it works by seeing the input value, then it checks the if condition, if it not satisfy it prints the n,
# then it goes to same function to get next number in this case, n-1 then again check if condition till n == 0 is satisfied,
# once satisfied, nothing to return and then program stopped!
# QuestionL Write recursive function. Print number from 1 to n using show(5)
def show(n):
    if n == 0:
        return
    show(n - 1)
    print(n)
show(3)
# Explanation:
# STEP 1Start: show(3) Inside this call: n = 3 Check: if n == 0, No.
# Now Python sees: show(n - 1) which becomes: show(2)
# IMPORTANT: print(3) has NOT run yet.
# Python pauses current function here.
# Visual: show(3), WAITING to print 3. 
# STEP 2: Now new function starts: show(2), Inside: n = 2. Again: show(1) called.
# Now: show(3) waiting print(3), show(2) waiting print(2)
# STEP 3: Now: show(1) Again calls: show(0)
# Now stack:
# show(3) waiting print(3)
# show(2) waiting print(2)
# show(1) waiting print(1)
# STEP 4 — BASE CASE
# Now: show(0), Condition true: return. Function ends immediately.
# NOW THE MAGIC: Python goes BACK to previous waiting function. Which was: show(1)
# Remember: it was paused at: show(n - 1) That line is now finished.
# So Python moves to NEXT line: print(n). For THIS function: n = 1
# So prints: 1. THEN ? show(1) ends. 
# Python returns to previous waiting function: show(2). Now: print(n). Here: n = 2, Prints: 2
# Then: back to show(3), print(3)
# Final output:
# 1
# 2
# 3
# THE KEY THING YOU MISSED, You thought: “n becomes 4 then becomes 3”, But actually: NO.
# There are MULTIPLE DIFFERENT n's. Like:
# show(5) has its own n = 5
# show(4) has its own n = 4
# show(3) has its own n = 3
# Each recursive call creates NEW local scope.
# Recursion heavily depends on:
# local variables
# function memory
# call stack
# Visualize Like Waiting Rooms:
# show(5) waiting
#     show(4) waiting
#         show(3) waiting
#             show(2) waiting
#                 show(1) waiting
#                     show(0) ends

#                 print(1)
#             print(2)
#         print(3)
#     print(4)
# print(5)
# THAT is recursion.
def test(n):
    if n == 0:
        return
    print(n)
    test(n - 1)
    print(n)
test(3)
# In this above program, the function will give output as: 3 2 1 1 2 3 and the reason behind it, is first it will make a countdown
# from 3 2 1 and then the paused values in print() after test(n-1) will come out and print as 1 2 3.
def test(n):
    if n == 0:
        return
    print("Down", n)
    test(n - 1)
    print("Up", n)
test(2)
# Now gonna write popular factorial program in recursion
# We want: factorial(5) to become:
# 5 × factorial(4)
# Then:
# 5 × 4 × factorial(3)
# and so on.
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
print(factorial(5))