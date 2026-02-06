def chatbot():
    print("Hello! I am ChatPy. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("ChatPy: Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("ChatPy: Hello there! How can I help you today?")
        elif "how are you" in user_input:
            print("ChatPy: I'm a bot, but I'm doing great! How about you?")
        elif "your name" in user_input or "who are you" in user_input:
            print("ChatPy: My name is ChatPy. Nice to meet you!")
        elif "weather" in user_input:
            print("ChatPy: I hope it’s sunny where you are!")
        elif "time" in user_input:
            print("ChatPy: I don't have a clock, but it's always a good time to code!")
        elif "color" in user_input:
            print("ChatPy: I like all colors, but I think blue is calm!")
        elif "help" in user_input:
            print("ChatPy: I can chat with you, tell jokes, or answer basic questions.")
        else:
            print("ChatPy: I don't understand. Can you ask something else?")

chatbot()