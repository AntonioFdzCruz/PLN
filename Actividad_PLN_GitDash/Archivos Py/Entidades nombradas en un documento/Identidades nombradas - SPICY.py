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

"""
■ ■ ■ ► En este ejemplo, doc.ents contiene las entidades nombradas identificadas
por spaCy junto con sus etiquetas (por ejemplo, “PERSON” para personas, “LOC” para lugares, etc.).

Ambas bibliotecas (NLTK y spaCy) son excelentes opciones para el procesamiento de lenguaje natural.
"""


# pip install spacy
# python -m spacy download es_core_news_sm

import spacy

# Cargar el modelo en español
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo
texto = "Barack Obama nació en Hawái."

# Procesar el texto
doc = nlp(texto)

# Identificar entidades nombradas
for entidad in doc.ents:
    print(entidad.text, entidad.label_)
