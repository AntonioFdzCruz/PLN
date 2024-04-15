'''
Programas en phyton Modulo NLTK
programa 2

El ejercicio consiste en encontrar todas las "palabras" de 3 o 4 letras
- Se entiende por "palabra" CUALQUIER coosa entre espacios
'''

'''Antonio Fernando Fernández Cruz'''

import nltk
nltk.download('stopwords')
print("Antonio Fernando Fernández Cruz")


carpeta_nombre='Actividad_PLN_GitDash\\Documentos\\'
archivo_nombre="archivo1.txt"
with open(carpeta_nombre+archivo_nombre,"r", encoding='utf-8') as archivo:
    texto=archivo.read()

print("----------------------------------------------------------------------")
palabras_funcionales=nltk.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
 '''print(palabras_funcional)'''

print("----------------------------------------------------------------------")
tokens=nltk.word_tokenize(texto,"spanish")
tokens_limpios=[]
for token in tokens:
 if token not in palabras_funcionales:
    tokens_limpios.append(token)
    '''print(tokens_limpios)'''

print(len(tokens))
print(len(tokens_limpios))
texto_limpio_nltk=nltk.Text(tokens_limpios)
distribucion_limpia=nltk.FreqDist(texto_limpio_nltk)
distribucion_limpia.plot(40)