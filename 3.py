def chatbot_response(user_input):
    
    responses = {
        "hello": "Hello! How can I help you?",
        "Hello": "Hello! How can I help you?",
        "Hi": "Hi there! How can I assist you?",
        "hi": "Hi there! How can I assist you?",
        "how are you": "I'm just a bot, but I'm here to help! How can I assist you?",
        "How are you": "I'm just a bot, but I'm here to help! How can I assist you?",
        "what is your name": "I am a simple chatbot created to assist you.",
        "What is your name": "I am a simple chatbot created to assist you.",
        "Help": "Sure, I'm here to help! What do you need assistance with?",
        "help": "Sure, I'm here to help! What do you need assistance with?",
        "Bye": "Goodbye! Have a great day!",
        "bye": "Goodbye! Have a great day!",
        "Thank you": "You're welcome! If you have any other questions, feel free to ask.",
        "thank you": "You're welcome! If you have any other questions, feel free to ask.",
        "Thanks": "You're welcome! I'm here to help.",
        "thanks": "You're welcome! I'm here to help."
    }

   
    user_input = user_input.lower()

    
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]

        return "Iam sorry, I don't understand that. Can you please rephrase?"


def chat():
    print("Chatbot: Hello! I am your friendly chatbot. Type 'bye/Bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()
