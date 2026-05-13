# EXCEPTION - abnormal runtime event that interrupts execution
# For example: divide by zero, invalid input, missing file, JSON parse failure, nwtwork timeout, etc

# Try and Except -
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")
# Instead of ZeroDivisionError, it beautifully prints "Cannot divide by zero"
# 'try' means attempt risky operation. If exception occurs, python jumps to 'except' block.

# Catching multiple exceptions
try:
    num = int(input("Enter: "))
    print(10/num)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Generic Exception:
except Exception as e:
    print(e)
# captures actual error, useful for loggin/debugging but overusing generic exception handling can hide bugs

# 'finally' Block: Runs always
# use for cleanup: close connections, release resources, logging
try:
    print("run")
except:
    print("error")
finally:
    print("always runs")

# QUESTION: Write program: 
# ask user for number
# divide 100 by that number
# handle: invalid input, divide by zero
# use: specific exceptions, f-string, finally block
try:
    num = int(input("Enter number: "))
    print(f"Result: {100/num}")
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("run")

# CUSTOM EXCEPTIONS: Python let us create exceptions
# example: raise ValueError("Invalid age"). 'raise' manually trigger exception
# Example:- 
age = -5
if age<0:
    raise ValueError("Age cannot be negative")
# why useful: rules, constraints, validations

# Creating custom Exception class:
# class InvalidAgeError(Exception):
#     pass
# now custom exception exist
# Example:
class InvalidAgeError(Exception):
    pass
age = -2
if age < 0:
    raise InvalidAgeError("Negative age not allowed")
# Why this matters: Large system need -
#  - categorized failures
#  - domain specific debugging
#  - clean architecture
# custom exception help structure systems

# QUESTION: 
# Create custom exception: InvalidMarksError
# Program: ask user marks, if marks < 0: raise custom exception, otherwise print marks safely
# handle exception using try-except
# use f-string somewhere
class InvalidMarksError(Exception):
    pass
try:
    marks = int(input("Enter your marks: "))
    if marks < 0:
        raise InvalidMarksError("Negative marks are not allowed.")
    print(f"Success! Your marks are safely recorded as: {marks}")
except ValueError:
    print("Invalid input.")
except InvalidMarksError as e:
    print(f"Custom Error Triggered: {e}")
