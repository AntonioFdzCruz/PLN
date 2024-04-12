import nltk
from nltk.draw.dispersion import dispersion_plot

nltk.download('punkt')

import os
os.system('cls')

print('\n■■■■■■■■■■■■■■■■■■■ Funcion PLOT - Distribución de frecuencias - Programa Cap. 8 Pag.19 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n')

carpeta_nombre="D:\\Tony\\Documents\\MEGAsync\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\Actividad_PLN_GitDash\\Documentos\\"
archivo_nombre="archivo2.txt"
with open(carpeta_nombre+archivo_nombre,"r", encoding='utf-8') as archivo:
    texto=archivo.read()

print('*** NLTK - Distribución de frecuencias ***')

tokens=nltk.word_tokenize(texto,"spanish")
texto_nltk=nltk.Text(tokens)
distribucion=nltk.FreqDist(texto_nltk)
lista_frecuencias=distribucion.most_common()
print('*** Mostrar: Lista frecuencias (Pag. 19):\n')
print(lista_frecuencias)

print('\nLista frecuencias (Pag. 20):')
print('\n*** A esta altura ya tenemos la lista de tokens en "tokens".')
texto_nltk=nltk.Text(tokens)
distribucion=nltk.FreqDist(texto_nltk)
print('\n*** Mostrar: Distribucion["vivíparos"]')
print(distribucion["vivíparos"])



print('\n*** Graficar resultados 1: nltk.FreqDist.plot\n')
nltk.FreqDist.plot(distribucion)


#lista_palabras = ["vivíparos", "Columna", "Mamíferos", "Animales"]


print('\n*** Graficar resultados 2: dispersion_plot()\n')
tokens=nltk.word_tokenize(texto,"spanish")
texto_nltk=nltk.Text(tokens)
lista_palabras = ["vivíparos", "Columna", "Mamíferos", "Animales"]
texto_nltk.dispersion_plot(lista_palabras)



print('\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ FIN del Programa ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n\n')
os.system('pause')