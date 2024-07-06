def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ['hi', 'hello', 'hey']:
            print("Chatbot: Hello! How can I assist you?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected! How about you?")
        elif 'your name' in user_input:
            print("Chatbot: I'm a simple chatbot created by OpenAI's ChatGPT.")
        elif 'what can you do' in user_input:
            print("Chatbot: I can respond to basic greetings and questions. Try asking me something!")
        elif 'bye' in user_input or 'exit' in user_input or 'quit' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Could you rephrase?")

# Run the chatbot
chatbot()
