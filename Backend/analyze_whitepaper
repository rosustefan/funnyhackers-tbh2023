import requests

class analyze_whitepaper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.openai.com/v1/engines/davinci-codex/completions"

    def generate_text(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "prompt": f"{prompt}",
            "max_tokens": 1024,
            "temperature": 0.5,
            "n": 1,
            "stop": ["\n\n"]
        }

        response = requests.post(self.api_url, headers=headers, json=data)

        if response.status_code != 200:
            raise ValueError(f"Failed to generate text: {response.text}")

        output = response.json()["choices"][0]["text"]
     