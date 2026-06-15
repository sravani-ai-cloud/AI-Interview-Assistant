from app.services.gemini_service import ask_gemini

response = ask_gemini(
    "Give me 3 Python interview questions."
)

print(response)