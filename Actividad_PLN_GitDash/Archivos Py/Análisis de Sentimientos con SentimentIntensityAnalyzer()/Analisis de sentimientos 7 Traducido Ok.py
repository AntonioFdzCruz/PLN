
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
import os

# Descargar recursos necesarios de NLTK
nltk.download('vader_lexicon')
nltk.download('punkt')

# Crear el analizador de sentimientos
sid = SentimentIntensityAnalyzer()

# Función para obtener el valor de una palabra
def valor_palabra(palabra):
    if palabra in sid.lexicon:
        return sid.lexicon[palabra]
    else:
        return None

# Función para analizar una frase y mostrar los valores de cada palabra
def analizar_detalle(texto):
    # Traducir el texto al inglés
    texto_traducido = GoogleTranslator(source='auto', target='en').translate(texto)
    print
    print('-'*100)
    print(f"  ■ Texto traducido: {texto_traducido} ■")
    print('-'*100)

    # Tokenizar el texto traducido
    palabras = nltk.word_tokenize(texto_traducido)
    
    # Analizar el texto completo
    sentimiento = sid.polarity_scores(texto_traducido)
    print('')
    print('Valores de la polaridad del texto completo:', sentimiento)

    # Analizar cada palabra
    for palabra in palabras:
        valor = valor_palabra(palabra.lower()) 
        if valor is not None:
            print('')
            print(f"    Palabra: '{palabra}', Valor de sentimiento: {valor}")
        else:
            print('')
            print(f"    • Palabra: '{palabra}' no se encuentra en el léxico de VADER.")

    
    # Imprimir el sentimiento basado en el valor compuesto
    compound_score = sentimiento['compound']
    if compound_score >= 0.05:
        print("\n  ■  Sentimiento ► Positivo ◄")
        print('\n')
        print('•'*150)
        print('\n')
    elif compound_score <= -0.05:
        print("\n  ■  Sentimiento ► Negativo ◄")
        print('\n')
        print('•'*150)
    else:
        print("\n  ■  Sentimiento ► Neutral ◄")
        print('\n')
        print('•'*150)
        print('\n\n')


os.system('cls')
print('\n')
print('•'*150)
print('')

# Ejemplo de uso
texto = input("Ingresa un texto para analizar su sentimiento: ")
analizar_detalle(texto)
