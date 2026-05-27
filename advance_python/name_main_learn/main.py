# In this we will learn about very common line we see in production code files at the last line, and that is -
# if __name__ == "__main__":
#     main()
# See, in production grade files, files are not static, they are being used by other files too, and not only one file is running,
# multiple files at the same time running, so we cannot everytime in terminal, trying to run files one-by-one, that is why, we 
# create a main file, and then other files, and try to connect them by importing and all. Now when we import file in another file, 
# the problem without "__main__" is suppose you created a file named "test_1.py" and you wrote some some code, and then you created
# another file, "test_2.py" now what happens is when you import test_1.py in test_2.py, using 'from test_1 import {whatever function}'
# test_1 all code will execute and then test_2 all code will execute! AND you sure you dont want this, you want just some particular 
# things run, AND test_1 only run, when I run that file individually, that is why, we use __name__ == "__main__"

# The solution -
# Python gives every file a hidden variable:  __name__
# This variable changes depending on how the file is used.
#-----------------------------------------------------------------
# Case 1: File is run directly:  python ai_tools.py
# Then:
# __name__ == "__main__"
#-----------------------------------------------------------------
# Case 2: File is imported:  import ai_tools
# Then:  __name__ == "ai_tools"
# So we can write:
# if __name__ == "__main__":
#     print("Run this only when file is executed directly")
#-----------------------------------------------------------------
# Correct version -
# ai_tools.py
# def add_credit(credit: int, amount: int) -> int:
#     return credit + amount
# if __name__ == "__main__":
#     print("AI tools loaded")
#-----------------------------------------------------------------
# Now if you run directly:
# python ai_tools.py
# Output: AI tools loaded
# But if another file imports it: main.py
# import ai_tools
# result = ai_tools.add_credit(5, 10)
# print(result)
# Output: 15
# No unwanted print. That is the point.

# AND NOW one more important thing, you cannot write whole program under __name__ == "__main__", so you can create a function above
# that will be the main function, which have all the thing to execute when file alone is going to be executed. Take this as -
# Suppose you create a folder structure:
# ai_streaming_engine/
# ├── main.py
# ├── model.py
# ├── credit_system.py
# Now in this, you can write seperate code for model.py and credit_system.py and then in main.py, create a def main(): function
# and in this file only import all the necessary functions from other 2 files, and then in main() function, put and execute it, 
# and then you only have to execute one main file, and program connected to every file, will be executed. 
# Lets take a example -

# model.py: It should nto start the whole app when imported
class AIModel:
    def generate(self, prompt: str) -> str:
        return f"Response to: {prompt}"
    
# credit_system.py: It should not ask login immediately when imported
class CreditSystem:
    def __init__(self, credit: int):
        self.credit = credit

# main.py: Only this main file should start the application
from model import AIModel
from credit_system import CreditSystem
def main():
    model = AIModel()
    credit_system = CreditSystem(credit=3)
    prompt = input("Enter prompt: ")
    response = model.generate(prompt)
    print(response)
if __name__ == "__main__":
    main()
# Now This is the real mental shift: Files should define reusable building blocks. Only the entry file should start the program.

# LEARN this simple rule: 
# 1) Use this pattern for every serious Python file that can be run directly
def main():
    # your integrated main code
    pass
if __name__ == "__main__":
    main()
# 2) Do not put random execution code at top level. Top level should mostly contain:
#    imports, constants, classes, functions
# 3) Execution should go inside main()
# 4) And be protected by: if __name__ == "__main__":

class AIModel:
        def generate(self, prompt):
            return f"AI response for: {prompt}"
def main():
    model = AIModel()
    prompt = input("Enter prompt: ")
    print(model.generate(prompt))
if __name__ == "__main__":
    main()