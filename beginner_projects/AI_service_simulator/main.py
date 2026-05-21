import time

class AISystem:
    def __init__(self, user_id, pin, model, initial_credit=2):
        self.user_credit = initial_credit
        self.user_id = user_id
        self.pin = pin
        self.model = model

    def check_credit(self, func):
        def wrapper(*args, **kwargs):
            if self.user_credit <= 0:
                print("Access denied! You have 0 credit left.")
                return
            else:
                self.user_credit -= 1
                print(f"Remaining credits: {self.user_credit}")
                return func(*args, **kwargs)
        return wrapper

    def add_credit(self):
        print("\nADD CREDIT: Type your username and pin to add credit")
        while True:
            user = input("Enter your username ('xx' to cancel): ").strip()
            pinn = input("Enter your 4 digit pin ('xx' to cancel): ").strip()
            # adding the condition
            if user == 'xx' and pinn == 'xx':
                print("GoodBye!")
                break
            elif user == self.user_id and pinn == self.pin:
                print("Fetching data", end="")
                for _ in range(5):
                    time.sleep(0.6)
                    print(".", end="", flush=True)
                print("Success!")

                while True:
                    try:
                        cred = int(input("Enter number of credit you want to add (eg. 5, 10, etc): "))
                        break
                    except ValueError:
                        print("INVALID input. Enter a whole number!")
                print("Generating bill...")
                time.sleep(0.7)
                print(f"Your total bill for {cred} credit is: ${cred}")

                payment_successful = False
                while True:
                    payment = input("Type 'pay' for payment or 'cancel' to exit: ").strip().lower()
                    if payment == 'exit' or payment == 'cancel':
                        print("Payment cancelled!")
                        break
                    elif payment == 'pay':
                        print("Wait for a moment, checking transaction", end="")
                        for _ in range(6):
                            time.sleep(0.6)
                            print(".", end="", flush=True)
                        print("Payment success! Credit added to your account.")
                        # adding credit to account
                        self.user_credit += cred
                        print(f"Total user credit: {self.user_credit}")
                        payment_successful = True
                        break
                    else:
                        print("INVALID! Please type 'pay'.")

                if payment_successful or payment == 'cancel' or payment == 'exit':
                    break

            elif user == self.user_id and pinn != self.pin:
                print("Password is incorrect! Try again!")
            elif user != self.user_id and pinn == self.pin:
                print("Username is incorrect! Try again!")
            else:
                print("Username and password is incorrect!")


class AIModel:
    def __init__(self, model_name):
        self.model_name = model_name
    def mock_ai_stream(self, prompt):
        clean_prompt = prompt.lower().strip()
        response = {
            "hi": "Hi, good to see you! Myself DEMO, an AI build to test ai streaming engine.",
            "how are you": "I am absolutely good, thanks for asking! how are you?",
            "how are you?": "I am absolutely good, thanks for asking! how are you?",
            "who are you": "Myself DEMO, an AI build to test ai streaming engine.",
            "who are you?": "Myself DEMO, an AI build to test ai streaming engine.",
            "who is harshit": "He is my creator and created this whole system.",
            "who is harshit?": "He is my creator and created this whole system."
        }
        fallback_text = "I'm sorry, I don't understand that prompt."
        chosen_response = response.get(clean_prompt, fallback_text)
        tokens = chosen_response.split()
        for token in tokens:
            time.sleep(0.3)
            yield token + " "

print("============ WELCOME TO DEMO AI =============")
print("To continue, please login in with your username and password.")

while True:
    user_id = input("Enter your username (5 characters) or 'xx' to exit: ").strip()
    pin = input("Enter your 4 digit pin or 'xx' to exit: ").strip()

    if user_id == 'xx' and pin == 'xx':
        print("Come back soon!")
        break
    elif len(user_id) != 5 or len(pin) != 4:
        print("Please enter valid username and password within the range!")
    else:
        model = AIModel("DEMO-AI")
        system = AISystem(user_id, pin, model)
        @system.check_credit
        def call_ai_model(prompt):
            print(f"Prompt: {prompt}")
            print("Response: ", end="")
            
            token_generation = system.model.mock_ai_stream(prompt)
            for chunk in token_generation:
                print(chunk, end="", flush=True)
            print()

        print("\n==== AI CHAT SESSION STARTED ====")
        while True:
            if system.user_credit <= 0: 
                print("\nCREDIT ENDED! Type: \n1. Add (to add credit)\n2. Exit")
                action = input("Enter your choice: ").strip().lower()
                
                if action == '1' or action == 'add':
                    system.add_credit()
                elif action == '2' or action == 'exit':
                    print("Please add credit to resume service!")
                    break
                else:
                    print("Invalid Option! Please type 'add' or 'exit'")
                    continue
            user_prompt = input("\nAsk Anything! (or type 'exit' to quit): ").strip()

            if user_prompt.lower() == 'exit':
                print("GoodBye!")
                break
            elif user_prompt == "":
                continue
            else:
                call_ai_model(user_prompt)
