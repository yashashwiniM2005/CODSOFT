TASK 1:

def chatbot_response(user_input):
    # Convert input to lower case to handle case insensitivity
    user_input = user_input.lower()

    # Basic greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    # Asking for help
    elif "help" in user_input:
        return "Sure! What do you need help with?"

    # Inquiring about time
    elif "time" in user_input:
        return "I can't tell you the exact time, but it's always a good time to code!"

    # Asking for the weather
    elif "weather" in user_input:
        return "I can't check the weather, but I hope it's sunny where you are!"

    # Farewells
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    # Default response for unknown inputs
    else:
        return "I'm sorry, I don't understand that. Can you rephrase?"

# Chatbot loop for conversation
print("Chatbot: Hi! I am a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a nice day!")
        break
    else:
        response = chatbot_response(user_input)
        print("Chatbot:", response)
		
OUTPUT:

Chatbot: Hi! I am a simple chatbot. Type 'bye' to exit.
You: Hi
Chatbot: Hello! How can I help you today?
You: help
Chatbot: Sure! What do you need help with?
You: time
Chatbot: I can't tell you the exact time, but it's always a good time to code!
You: weather
Chatbot: I can't check the weather, but I hope it's sunny where you are!
You: bye
Chatbot: Goodbye! Have a nice day!

=== Code Execution Successful ===

