import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

cliente = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

respuesta = cliente.models.generate_content(
    model="gemini-2.5-flash",
    contents="Responde únicamente con la palabra: Hola"
)

print(respuesta.text)
