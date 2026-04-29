import requests
import json
from config import API_KEY_GPT

API_KEY = API_KEY_GPT

def generate_response(prompt, temperature=0.3, max_tokens=1024):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-5.5-pro",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        result = response.json()
    except:
        return f"[ERROR] Invalid JSON response: {response.text}"

    if "error" in result:
        return f"[API ERROR] {result['error']}"

    if "choices" not in result:
        return f"[ERROR] Unexpected response: {result}"

    return result["choices"][0]["message"]["content"]