import os
import google.generativeai as genai

Gemini_Api = os.getenv("GEMINI_API")
Bot_Api = os.getenv("BOT_API")

genai.configure(api_key=Gemini_Api)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash-lite",
    system_instruction=(
        "You are Escanor from the Seven Deadly Sins. "
        "Speak proudly and confidently, but keep your answers concise "
        "and include clear factual comparisons when users ask for advice."
    )
)
    
my_id_str = os.getenv("MY_ID")
if my_id_str is None:
    raise ValueError("Environment variable MY_ID not set!")

MY_ID = int(my_id_str)