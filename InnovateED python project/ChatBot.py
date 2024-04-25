import random

# Define responses for different types of user inputs
greetings = ["hello", "hi", "hey", "greetings", "howdy"]
responses_to_greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

farewells = ["bye", "goodbye", "see you", "farewell"]
responses_to_farewells = ["Goodbye!", "See you later!", "Take care!", "Farewell!"]

questions = ["how are you", "what's up", "how's it going", "how are you doing"]
responses_to_questions = ["I'm doing well, thank you!", "Not too bad, thanks!", "I'm great, thanks for asking!"]

# Function to handle user input and generate appropriate responses
def chat():
    print("Welcome! I'm a Python Chatbot. You can start talking to me or type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("Goodbye! Have a great day!")
            break
        elif user_input in greetings:
            print(random.choice(responses_to_greetings))
        elif user_input in farewells:
            print(random.choice(responses_to_farewells))
            break
        elif user_input in questions:
            print(random.choice(responses_to_questions))
        else:
            print("I'm sorry, I don't understand that.")

# Run the chatbot
chat()
