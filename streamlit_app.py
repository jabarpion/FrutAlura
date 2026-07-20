import streamlit as st
from pathlib import Path

from utils.lector_pdf import leer_pdf
from utils.agente import preguntar_al_pdf


st.set_page_config(
    page_title="FrutAlura IA",
    page_icon="🤖"
)


@st.cache_data
def cargar_documento():
    ruta_pdf = (
        Path(__file__).parent
        / "documentos"
        / "codigo_conducta_frutalura.pdf"
    )

    return leer_pdf(ruta_pdf)


if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("🤖 Agente Inteligente FrutAlura")

st.write(
    "Haz preguntas sobre el Código de Conducta de FrutAlura."
)


for mensaje in st.session_state.messages:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])


pregunta = st.chat_input("Escribe tu pregunta...")


if pregunta:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": pregunta,
        }
    )

    with st.chat_message("user"):
        st.markdown(pregunta)

    with st.spinner("Consultando documento..."):

        texto_pdf = cargar_documento()

        respuesta = preguntar_al_pdf(
            texto_pdf,
            pregunta,
        )

    with st.chat_message("assistant"):
        st.markdown(respuesta)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": respuesta,
        }
    )
