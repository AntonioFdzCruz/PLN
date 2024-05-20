
import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import ne_chunk, pos_tag

# Descargar los recursos necesarios
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


text1 = "Cuento de caperucita; Había una vez una adorable niña que era querida por todo aquél que la conociera, pero sobre todo por su abuelita, y no quedaba nada que no le hubiera dado a la niña. Una vez le regaló una pequeña caperuza o gorrito de un color rojo, que le quedaba tan bien que ella nunca quería usar otra cosa, así que la empezaron a llamar Caperucita Roja. Un día su madre le dijo: Ven, Caperucita Roja, aquí tengo un pastel y una botella de vino, llévaselas en esta canasta a tu abuelita que esta enfermita y débil y esto le ayudará. Vete ahora temprano, antes de que caliente el día, y en el camino, camina tranquila y con cuidado, no te apartes de la ruta, no vayas a caerte y se quiebre la botella y no quede nada para tu abuelita. Y cuando entres a su dormitorio no olvides decirle, Buenos días, ah, y no andes curioseando por todo el aposento."



words1 = word_tokenize(text1)
tagged1 = pos_tag(words1)
grammar = "NP: {<DT>?<JJ>*<NN>}"
parser = RegexpParser(grammar)
result1 = parser.parse(tagged1)
print("Resultado del chunking para frases nominales:")
print(result1)
print()
print('- -'*25)

# Ejemplo 2: Reconocimiento de entidades nombradas
text2 = "Barack Obama was born in Hawaii."
tokens2 = word_tokenize(text2)
pos_tags2 = pos_tag(tokens2)
ner_chunks2 = ne_chunk(pos_tags2)
print("Resultado del reconocimiento de entidades nombradas:")
print(ner_chunks2)
