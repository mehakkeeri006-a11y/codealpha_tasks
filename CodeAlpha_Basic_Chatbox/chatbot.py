def chatbot():
    print("Chatbot: Hi! I'm a simple bot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you?":
            print("Chatbot: I'm doing great, thank you!")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that yet.")

chatbot()