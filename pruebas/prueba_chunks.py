from utils.lector_pdf import leer_pdf
from utils.chunker import dividir_en_chunks

texto = leer_pdf("documentos/codigo_conducta_frutalura.pdf")

chunks = dividir_en_chunks(texto)

print(f"Cantidad de chunks: {len(chunks)}")

print("\nPrimer chunk:\n")
print(chunks[0])

print("\nLongitud del primer chunk:")
print(len(chunks[0]))
