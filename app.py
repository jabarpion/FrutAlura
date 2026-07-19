from utils.lector_pdf import leer_pdf
from utils.agente import preguntar_al_pdf

ruta = "documentos/codigo_conducta_frutalura.pdf"

texto = leer_pdf(ruta)

print("\n====================================")
print(" Agente Inteligente FrutAlura")
print("====================================\n")

pregunta = input("Escribe tu pregunta: ")

respuesta = preguntar_al_pdf(texto, pregunta)

print("\nRespuesta:\n")

print(respuesta)
