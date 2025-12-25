import datetime

print("🤖 ChatBot: Hello! I am SmartBot.")
name = input("🤖 ChatBot: What's your name? ")

print(f"🤖 ChatBot: Nice to meet you, {name} 😊")
print("Type 'bye' to exit.\n")

# predefined replies
responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm doing great 😊 What about you?",
    "your name": "My name is SmartBot 🤖",
    "help": "I can chat, tell time/date, and answer basic questions."
}

while True:
    user = input(f"{name}: ").lower()

    # exit condition
    if user == "bye":
        print("🤖 ChatBot: Goodbye! Take care 👋")
        break

    # time
    elif "time" in user:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"🤖 ChatBot: Current time is {time}")

    # date
    elif "date" in user:
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"🤖 ChatBot: Today's date is {date}")

    # dictionary responses
    elif user in responses:
        print("🤖 ChatBot:", responses[user])

    # mood response
    elif "fine" in user or "good" in user:
        print("🤖 ChatBot: That's nice to hear 😊")

    elif "bad" in user or "sad" in user:
        print("🤖 ChatBot: Oh no 😔 Hope things get better soon.")