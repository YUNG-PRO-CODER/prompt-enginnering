import requests
from testconfig import API_KEY

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

data = {
    "model": "x-ai/grok-4.20-multi-agent",
    "messages": [
        {
            "role": "system",
            "content": "u are a gamer."
        },
        {
            "role": "user",
            "content": "who is arthur morgan? and why is he loved by many gamers?"
        }
    ],
    "temperature": 0.7,
    "max_tokens": 100
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)