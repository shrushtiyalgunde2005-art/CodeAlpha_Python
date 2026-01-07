# Basic Chatbot
# CodeAlpha Python Programming Internship - Task 3


print("🤖 Hello! I am a simple chatbot.")
print("Type 'by' to end the conversation.")

while True:
    user_msg = input("You: ").lower()

    if user_msg == "hi" or user_msg == "hello":
        print("Bot: Hello! How can I help you?")

    elif user_msg == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_msg == "what is your name":
        print("Bot: I am a simple Python chatbot created by Shrushti !")

    elif user_msg == "what can you do":
        print("Bot: I can answer simple questions and chat with you.")

    elif user_msg == "help":
        print("Bot: Try asking things like 'hi', 'how are you', or 'what is your name'.")

    elif user_msg == "who created you":
        print("Bot: I was created by a Python programmer during an internship.")

    elif user_msg == "good morning":
        print("Bot: Good morning! Have a great day ☀️")
    
    elif user_msg == "good night":
        print("Bot: Good night! Sweet dreams 🌙")
    
    elif user_msg == "bye":
        print("Bot: Goodbye! Have a nice day 😊")
        break

    else:
        print("Bot: Sorry, I didn't understand that.")

    