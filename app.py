from ollama import chat
from ollama import ChatResponse

# Initialize chat history
messages = []
max_tokens = 50  # Set maximum response length (adjust as needed)

print("Ollama Chatbot (type 'exit' to stop)")
while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    # Add user message to conversation history
    messages.append({'role': 'user', 'content': user_input})

    # Get response from Ollama
    response: ChatResponse = chat(model='llama3.2', messages=messages)

    # Extract and print chatbot's response
    bot_response = response.message.content
    print("Chatbot:", bot_response)

    # Add chatbot response to conversation history
    messages.append({'role': 'assistant', 'content': bot_response})
