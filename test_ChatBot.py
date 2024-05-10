from chatterbot import ChatBot

# Create a chatbot instance
chatbot = ChatBot("My Chatbot")

# Define conversation starter
conversation = [
    ("Hi", "Hello!"),
    ("How are you?", "I'm doing great, thanks for asking! How can I help you today?"),
]

# Train the chatbot
chatbot.train(conversation)

# Interact with the chatbot
while True:
  user_input = input("You: ")
  if user_input.lower() == "quit":
    break
  bot_response = chatbot.get_response(user_input)
  print("Chatbot:", bot_response)
