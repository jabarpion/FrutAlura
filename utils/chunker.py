def dividir_en_chunks(texto, tamano=1500, solapamiento=300):
    """
    Divide un texto en fragmentos con solapamiento.
    """

    chunks = []

    inicio = 0

    while inicio < len(texto):

        fin = inicio + tamano

        chunk = texto[inicio:fin]

        chunks.append(chunk)

        inicio += tamano - solapamiento

    return chunks
