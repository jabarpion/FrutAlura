from utils.lector_pdf import leer_pdf
from utils.chunker import dividir_en_chunks
from utils.buscador import buscar_chunks

# Leer el documento
texto = leer_pdf("documentos/codigo_conducta_frutalura.pdf")

# Dividir en chunks
chunks = dividir_en_chunks(texto)

print(f"Cantidad de chunks: {len(chunks)}")

# Pregunta de prueba
pregunta = "¿Qué es el código de conducta?"

# Buscar los 3 mejores chunks
mejores = buscar_chunks(
    pregunta,
    chunks,
    top_k=3
)

print("\n========== RESULTADOS ==========\n")

for i, chunk in enumerate(mejores, start=1):

    print(f"\n===== CHUNK {i} =====\n")

    print(chunk[:800])

    print("\n")
