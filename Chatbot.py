# Mini Project of Chatbot in AI
# Implementation of New Ideas
print("Chatbot: Hello! How can I assist you today?")

while True:
    user = input("You: ").lower()
    
    if "hello" in user or "hi" in user:
        print("Chatbot: Hello there! Nice to meet you.")
    
    elif "how are you" in user:
        print("Chatbot: I'm doing great! Thanks for asking.")
    
    elif "your name" in user:
        print("Chatbot: I am a simple chatbot created to assist you.")
    
    elif "help" in user:
        print("Chatbot: Sure! You can ask me basic questions or say ‘bye’ to exit.")
    
    elif "bye" in user:
        print("Chatbot: Goodbye! Have a great day ahead.")
        break
    
    else:
        print("Chatbot: I'm still learning. Could you please rephrase that?")
