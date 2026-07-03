from datetime import datetime

def current_time():
    now = datetime.now()
    print("Bot: Current Time is", now.strftime("%I:%M:%S %p"))


def chatbot():

    print("🤖 Welcome to Simple Chatbot")

    name = input("Enter your name: ")
    print("Hello", name + "!")

    while True:

        user = input("\nYou: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hello", name + "!")

        elif user == "how are you":
            print("Bot: I'm doing great. What about you?")

        elif user == "i am fine":
            print("Bot: Nice to hear that!")

        elif user == "your name":
            print("Bot: My name is Python ChatBot.")

        elif user == "who made you":
            print("Bot: I was created using Python.")

        elif user == "time":
            current_time()    

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye", name + "!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()