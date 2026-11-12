from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # reads GEMINI_API_KEY from .env

client = genai.Client(http_options=types.HttpOptions(timeout=15000))  # 15 s max wait

MODELS = ["gemini-3.5-flash-lite", "gemini-3.1-flash-lite"]  # tried in order

SYSTEM_PROMPT = (
    "You are Jarvis, a voice assistant. Answer in 1-3 short sentences. "
    "Plain text only, no markdown, no lists."
)


def ask_ai(command):
    for model in MODELS:
        try:
            resp = client.models.generate_content(
                model=model,
                contents=command,
                config={"system_instruction": SYSTEM_PROMPT},
            )
            if resp.text:
                return resp.text
        except Exception as e:
            print(f"{model} failed: {str(e)[:100]}")
    return "Sorry, I couldn't reach the AI right now."


if __name__ == "__main__":
    print(ask_ai("what is coding?"))