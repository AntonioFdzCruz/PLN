"""
Realizar un programa en phyton que analice en donde identifique las entidades nombradas del documento de 
texto(txt), PDF o Word, tendrán que aplicar la siguiente función 

ne_chunk(etiquetas_pos): Identifica entidades nombradas en un texto.
from nltk import ne_chunk, pos_tag, word_tokenize
text = "Barack Obama was born in Hawaii."
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
ner_chunks = ne_chunk(pos_tags)
print(ner_chunks)

o si consideran otra función para la identificación de entidades nombradas
"""

# pip install nltk


import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Texto de ejemplo
texto = "Barack Obama nació en Hawái."

# Tokenización y etiquetado POS
tokens = word_tokenize(texto)
pos_tags = pos_tag(tokens)

# Identificación de entidades nombradas
ner_chunks = ne_chunk(pos_tags)

# Imprimir las entidades nombradas
print(ner_chunks)
