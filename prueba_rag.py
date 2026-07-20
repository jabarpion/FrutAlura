from utils.lector_pdf import leer_pdf
from utils.chunker import dividir_en_chunks
from utils.buscador import buscar_chunks


texto = leer_pdf(
    "documentos/codigo_conducta_frutalura.pdf"
)

print("Caracteres PDF:", len(texto))


chunks = dividir_en_chunks(texto)

print("Cantidad de chunks:", len(chunks))


pregunta = "¿Qué es el código de conducta?"


resultados = buscar_chunks(
    pregunta,
    chunks,
    top_k=3
)


print("\n--- RESULTADOS ---")

for i, resultado in enumerate(resultados, 1):

    print("\nCHUNK", i)
    print(resultado[:500])
