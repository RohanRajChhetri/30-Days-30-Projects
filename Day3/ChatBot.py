from openai import OpenAI

client = OpenAI(api_key="",base_url="https://api.deepseek.com") #insert API key 

def chat_with_gpt(prompt):
    response = client.chat.completions.create (model = "deepseek-chat", messages = [{"role": "user", "content": prompt}])

    return response.choices[0].message.content

if __name__ == "__main__":
    user_input = input("You: ")
    while True:
        if user_input.lower() == ["exit", "quit"]:
            print("Exiting the chat. Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"GPT: {response}")
