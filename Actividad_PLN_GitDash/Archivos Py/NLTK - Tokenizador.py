
import nltk
#nltk.download('punkt')
import os
os.system('cls')

print('\n\n\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ INICIO del Programa ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n\n')
""" En mi Laptop """
# carpeta_nombre="D:\\Tony\\Documents\\MEGAsync\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\programaspln2024\\Documentos\\"
""" En mi PC """
carpeta_nombre="D:\\MEGA\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\programaspln2024\\Documentos\\"

archivo_nombre="archivo2.txt"
with open(carpeta_nombre+archivo_nombre,"r", encoding='utf-8') as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

print('\n\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ FIN del Programa ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n\n\n')
