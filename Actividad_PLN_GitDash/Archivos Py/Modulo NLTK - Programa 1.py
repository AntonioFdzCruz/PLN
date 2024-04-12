'''
Programas en phyton Modulo NLTK
programa 1

El ejercicio consiste en encontrar todas las "palabras" de 3 o 4 letras
- Se entiende por "palabra" CUALQUIER coosa entre espacios
'''
import re

carpeta_nombre='D:\\Tony\\Documents\\MEGAsync\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\Programas2024\\Documentos\\'
archivo_nombre="archivo1.txt"
with open(carpeta_nombre+archivo_nombre,"r", encoding='utf-8') as archivo:
    texto=archivo.read()

expresion_regular=re.compile(r"...? ")

resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))