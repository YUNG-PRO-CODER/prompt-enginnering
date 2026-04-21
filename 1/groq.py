from openai import OpenAI
import config

GROQ_URL = "https://api.groq.com/openai/v1"
GROK_URL = "https://api.x.ai/v1"

GROQ_MODELS = getattr(config, "GROQ_MODELS", [
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
])

GROK_MODEL = getattr(config, "GROK_MODEL", "grok-4.20-multi-agent")


def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    """
    Smart LLM router:
    Priority:
    1. Grok (if API key exists)
    2. Groq (fallback)
    """

    grok_key = getattr(config, "GROK_API_KEY", None)

    if grok_key:
        try:
            client = OpenAI(api_key=grok_key, base_url=GROK_URL)

            res = client.chat.completions.create(
                model=GROK_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )

            return res.choices[0].message.content

        except Exception as e:
            print(f"[WARN] Grok failed → {type(e).__name__}: {e}")

    groq_key = getattr(config, "GROQ_API_KEY", None)

    if groq_key:
        client = OpenAI(api_key=groq_key, base_url=GROQ_URL)

        last_err = None

        for model in GROQ_MODELS:
            try:
                res = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temperature,
                    max_tokens=max_tokens,
                )

                return res.choices[0].message.content

            except Exception as e:
                last_err = e
                print(f"[WARN] Groq model {model} failed → {e}")

        return f"Groq failed for all models. Last error: {last_err}"

    return (
        "No working API key found.\n"
        "Fix:\n"
        "- Add GROK_API_KEY (for Grok)\n"
        "- OR add GROQ_API_KEY (for Groq)\n"
    )