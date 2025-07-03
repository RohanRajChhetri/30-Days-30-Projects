from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Andswer the following question.

here is the conversation history: {context}

question: {question}

Answer:
"""

model = OllamaLLM(model="mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

def handle_conversation():
    context = ""
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting the conversation.")
            break

        result = chain.invoke({"context": context, "question": user_input})

        print(f"Bot: {result}")
        context += f"\nUser: {user_input}\nBot: {result}"

if __name__ == "__main__":
    handle_conversation()
    