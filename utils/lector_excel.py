import pandas as pd


def leer_excel(ruta_excel):
    """
    Lee el archivo Excel de FrutAlura.

    En EMBALAJES ETIQUETAS KIWI.xlsx:
    - Las dos primeras filas corresponden al encabezado/título.
    - La tercera fila contiene los nombres de las columnas.
    """

    df = pd.read_excel(
        ruta_excel,
        sheet_name="Hoja1",
        header=2
    )

    # Eliminar columnas completamente vacías
    df = df.dropna(axis=1, how="all")

    # Limpiar nombres de columnas
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.upper()
    )

    # Reemplazar valores vacíos
    df = df.fillna("")

    return df
