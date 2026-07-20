from utils.chunker import dividir_en_chunks
from utils.buscador import buscar_chunks

import os
from dotenv import load_dotenv
from google import genai


load_dotenv()


cliente = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def preguntar_al_pdf(texto_pdf, pregunta):

    # Crear fragmentos del documento
    chunks = dividir_en_chunks(texto_pdf)

    # Buscar fragmentos relacionados
    mejores_chunks = buscar_chunks(
        pregunta,
        chunks,
        top_k=3
    )

    if not mejores_chunks:
        return "No encontré esa información en el documento."

    print("Chunks totales:", len(chunks))
    print("Chunks recuperados:", len(mejores_chunks))


    contexto = "\n\n".join(mejores_chunks)

    print("\n--- CONTEXTO ENVIADO ---")
    print(contexto[:1000])


    if not contexto.strip() or len(contexto) < 50:

        return "No encontré esa información en el documento."


    prompt = f"""
Eres un asistente inteligente de FrutAlura.

Tu tarea es responder preguntas utilizando únicamente el contexto entregado.

Reglas:
- No inventes información.
- No uses conocimiento externo.
- Si el contexto no contiene la respuesta, responde:
"No encontré esa información en el documento."

CONTEXTO:

{contexto}


PREGUNTA:

{pregunta}


RESPUESTA:
"""


    try:

        respuesta = cliente.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )


        return respuesta.text


    except Exception as e:

        return (
          "⚠️ El servicio de inteligencia artificial no está disponible en este momento. "
          "Intenta nuevamente en unos minutos.\n\n"
          f"Detalle técnico: {e}"
        )
