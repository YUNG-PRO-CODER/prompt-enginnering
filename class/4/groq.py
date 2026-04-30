import requests
from config import API_KEY_GQ

def generate_response(prompt, temperature=0.7, max_tokens=400):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY_GQ}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "x-ai/grok-4.20-multi-agent",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"