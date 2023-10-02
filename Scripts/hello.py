def respond_to_user_input(user_input):
    if user_input.lower() == "hello":
        return "Hello! How can I help you today?"
    elif user_input.lower() == "how are you?":
        return "I'm an AI language model, so I don't have feelings, but I'm here to help! What can I do for you?"
    elif user_input.lower() == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase your question or statement?"

def start_conversation():
    print("Welcome! I'm here to chat with you. Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("AI: Goodbye! Have a great day!")
            break
        else:
            response = respond_to_user_input(user_input)
            print("AI:", response)

if __name__ == "__main__":
    start_conversation()