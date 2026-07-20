from pypdf import PdfReader


def leer_pdf(ruta_pdf):
    """
    Lee un archivo PDF y devuelve todo su texto.
    """

    lector = PdfReader(str(ruta_pdf))

    texto = ""

    for pagina in lector.pages:
        contenido = pagina.extract_text()

        if contenido:
            texto += contenido + "\n"

    return texto
