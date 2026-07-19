import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

cliente = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def preguntar_al_pdf(texto_pdf, pregunta):

    prompt = f"""
Eres un asistente de FrutAlura.

Responde únicamente utilizando la información del documento.

Si la respuesta no está en el documento, responde exactamente:

"No encontré esa información en el documento."

DOCUMENTO:

{texto_pdf}

PREGUNTA:

{pregunta}
"""

    respuesta = cliente.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return respuesta.text
