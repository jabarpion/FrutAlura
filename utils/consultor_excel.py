import re
import unicodedata


def normalizar_texto(texto):
    """
    Convierte el texto a minúsculas y elimina acentos.
    """

    texto = str(texto).lower().strip()

    texto = unicodedata.normalize(
        "NFD",
        texto
    )

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    return texto


def buscar_en_excel(df, pregunta, max_resultados=10):
    """
    Busca registros relacionados con la pregunta
    dentro del Excel.
    """

    pregunta_normalizada = normalizar_texto(pregunta)

    palabras = re.findall(
        r"\b\w+\b",
        pregunta_normalizada
    )

    stopwords = {
        "que",
        "cual",
        "cuales",
        "como",
        "donde",
        "cuando",
        "para",
        "del",
        "las",
        "los",
        "una",
        "uno",
        "por",
        "con",
        "es",
        "el",
        "la",
        "de",
        "en",
        "un",
        "y",
        "a",
        "se",
        "me",
        "hay",
        "dime",
        "muestra",
        "mostrar",
        "quiero",
        "necesito",
        "tiene",
        "tienen"
    }

    palabras = [
        palabra
        for palabra in palabras
        if palabra not in stopwords
        and len(palabra) > 1
    ]

    if not palabras:
        return df.head(max_resultados)

    puntuaciones = []

    for _, fila in df.iterrows():

        texto_fila = " ".join(
            normalizar_texto(valor)
            for valor in fila
        )

        puntuacion = sum(
            1
            for palabra in palabras
            if palabra in texto_fila
        )

        puntuaciones.append(puntuacion)

    resultado = df.copy()

    resultado["_puntuacion"] = puntuaciones

    resultado = (
        resultado[
            resultado["_puntuacion"] > 0
        ]
        .sort_values(
            "_puntuacion",
            ascending=False
        )
        .drop(columns=["_puntuacion"])
        .head(max_resultados)
    )

    return resultado


def dataframe_a_texto(df):
    """
    Convierte los resultados del Excel
    en texto para entregarlo a Gemini.
    """

    if df.empty:
        return "No se encontraron registros en la tabla."

    return df.to_string(index=False)
