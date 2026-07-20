def dividir_en_chunks(texto, tamano=1200, solapamiento=200):
    """
    Divide un texto en fragmentos con solapamiento.
    """

    chunks = []

    inicio = 0

    while inicio < len(texto):

        fin = inicio + tamano

        chunks.append(texto[inicio:fin])

        inicio += tamano - solapamiento

    return chunks
