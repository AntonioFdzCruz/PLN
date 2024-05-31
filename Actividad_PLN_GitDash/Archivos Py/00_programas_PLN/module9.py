def run_module9():
    print("Módulo 9 ejecutado - Tratamiento del archivo de Texto y conversión de estructura CSV")

print('Soy el archivo 9')



import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize

# Definir la gramática para el chunking
grammar = r"""
    Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}
"""

# Ejemplo de texto
texto = "El perro come comida deliciosa"

# Tokenizar el texto
tokens = word_tokenize(texto)

# Etiquetar las palabras
etiquetado = nltk.pos_tag(tokens)

# Crear el parser de chunking
chunkParser = RegexpParser(grammar)

# Realizar el chunking
chunked = chunkParser.parse(etiquetado)

# Mostrar el resultado
print(chunked)
