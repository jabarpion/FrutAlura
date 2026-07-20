import re


def tokenizar(texto):
    """
    Convierte un texto en un conjunto de palabras.
    """

    palabras = re.findall(r"\w+", texto.lower())

    return set(palabras)


def buscar_chunks(pregunta, chunks, top_k=3):
    """
    Devuelve los chunks más relacionados con la pregunta.
    """

    palabras_pregunta = tokenizar(pregunta)

    resultados = []

    for chunk in chunks:

        palabras_chunk = tokenizar(chunk)

        puntaje = len(
            palabras_pregunta.intersection(
                palabras_chunk
            )
        )

        resultados.append(
            (
                puntaje,
                chunk
            )
        )

    resultados.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return [
        chunk
        for _, chunk in resultados[:top_k]
    ]
