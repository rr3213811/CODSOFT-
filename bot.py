def get_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input:
        return "Hello! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "I'm here to help you. Feel free to ask me anything."
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Chatbot: Hi there! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
