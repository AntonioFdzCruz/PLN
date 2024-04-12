import nltk
nltk.download('punkt')
import os
os.system('cls')

print('\n\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ Funciones - Conteo - Programa Cap. 7 Pag.17 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n')

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
texto_nltk=nltk.Text(tokens)
texto_nltk.concordance("mamífero")









conteo_individual=tokens.count("vertebrados")
print("conteo_individual: ",conteo_individual)
palabras_totales=len(tokens)
porcentaje=100*conteo_individual/palabras_totales
print("Porcentaje: ",porcentaje," %")

print('\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ FIN del Programa ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n\n')