import openai
from Configuration import API_KEY


openai.api_key = API_KEY

while True:
    question = input("Please type your question:\n")

    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )
    
    response = output["choices"][0]["message"]["content"].lstrip()

    print(f"\nChatGPT's response to your question is:\n {response}")
    print()
