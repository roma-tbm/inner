from openai import OpenAI
from config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL, MOCK_MODE


client = None if MOCK_MODE else OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)


def ask(system_prompt: str, user_message: str) -> str:
    if MOCK_MODE:
        return f"[mock] Я слышу тебя. Ты написал: «{user_message}». Продолжим."
    response = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
    )
    return response.choices[0].message.content
