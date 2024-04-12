import nltk
nltk.download('punkt')
import os
os.system('cls')

print('\n\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Funciones - Programa Cap. 7 Pag.17 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n\n')

def riqueza_lexica(tokens):
    tokens_conjunto=set(tokens)
    palabras_totales=len(tokens)
    palabras_diferentes=len(tokens_conjunto)
    riqueza_lexica=palabras_diferentes/palabras_totales
    return riqueza_lexica

carpeta_nombre="D:\\Tony\\Documents\\MEGAsync\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\Actividad_PLN_GitDash\\Documentos\\"
archivo_nombre="archivo2.txt"

with open(carpeta_nombre+archivo_nombre,"r", encoding='utf-8') as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")
riqueza_lexica=riqueza_lexica(tokens)
print(riqueza_lexica)

print('\n\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ FIN del Programa ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n\n\n')
