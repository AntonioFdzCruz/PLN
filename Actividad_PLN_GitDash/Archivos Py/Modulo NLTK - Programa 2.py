'''
Programas en phyton Modulo NLTK
programa 2

El ejercicio consiste en encontrar todas las "palabras" de 3 o 4 letras
- Se entiende por "palabra" CUALQUIER coosa entre espacios
'''
import nltk
import matplotlib.pyplot as plt

carpeta_nombre='D:\\Tony\\Documents\\MEGAsync\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\Actividad_PLN_GitDash\\Documentos\\'
archivo_nombre="archivo1.txt"
with open(carpeta_nombre+archivo_nombre,"r", encoding='utf-8') as archivo:
    texto=archivo.read()

print("----------------------------------------------------------------------")
tokens=nltk.word_tokenize(texto, "spanish")
tokens_conjunto=set(tokens)
palabras_totales=len(tokens)
palabras_diferentes=len(tokens_conjunto)
print(palabras_totales)
print(palabras_diferentes)
texto_nltk=nltk.Text(tokens)
distribucion=nltk.FreqDist(texto_nltk)
print("----------------------------------------------------------------------")
hapaxes=distribucion.hapaxes()
for hapax in hapaxes:
 print(hapax)
from matplotlib import rcParams
rcParams.update({"figure.autolayout": True})
distribucion.plot(cumulative=True)
distribucion.plot(40,cumulative=True)