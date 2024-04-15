'''
Programas en phyton Modulo NLTK
programa 2

El ejercicio consiste en encontrar todas las "palabras" de 3 o 4 letras
- Se entiende por "palabra" CUALQUIER coosa entre espacios
'''
import nltk
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Descargar el corpus de español si aún no está instalado
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('cess_esp')

# URL de la página web que deseas buscar
url = "https://www.guiainfantil.com/articulos/ocio/cuentos-infantiles/10-cuentos-cortos-para-leer-con-ninos/"

# Obtener el contenido HTML de la página web
response = requests.get(url)
html = response.text

# Utilizar BeautifulSoup para extraer texto del HTML
soup = BeautifulSoup(html, "html.parser")
texto = soup.get_text()

# Tokenizar el texto en español
tokens = nltk.word_tokenize(texto, language="spanish")

# Calcular estadísticas del texto
tokens_conjunto = set(tokens)
palabras_totales = len(tokens)
palabras_diferentes = len(tokens_conjunto)
print("Palabras totales:", palabras_totales)
print("Palabras diferentes:", palabras_diferentes)

# Crear un objeto Text de NLTK
texto_nltk = nltk.Text(tokens)

# Calcular la distribución de frecuencia de las palabras
distribucion = nltk.FreqDist(texto_nltk)

# Imprimir palabras únicas (hapaxes)
hapaxes = distribucion.hapaxes()
print("Hapaxes:")
for hapax in hapaxes:
    print(hapax)

# Configurar matplotlib para ajustar automáticamente los márgenes
plt.rcParams.update({"figure.autolayout": True})

# Graficar la distribución de frecuencia de las palabras
distribucion.plot(cumulative=True)
plt.show()
