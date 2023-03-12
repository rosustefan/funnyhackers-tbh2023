import openai
from whitepaper_summarizer.config import configuration

openai.api_key = configuration.API_KEY


def write_summary(whitepaper_url):
    """
    This function receives a URL from the frontend and summarizes the input.
    It returns a string.
    """

    summary = "Please summarize the given whitepaper."

    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant meant to analyze a" +
                "cryptocurrency whitepapers and provide answers to people's" +
                " questions regarding that whitepaper."
            },
            {
                "role": "system",
                "content": "This is the whitepaper you are going to use:" 
                + whitepaper_url
            },
            {
                "role": "system",
                "content": "Answer people's questions based on this prompt:"
                + summary
            }

        ]
    )
    response = output["choices"][0]["message"]["content"].lstrip()
    print(f"\nChatGPT's response to your question is:\n {response}")
    print()

    return response
