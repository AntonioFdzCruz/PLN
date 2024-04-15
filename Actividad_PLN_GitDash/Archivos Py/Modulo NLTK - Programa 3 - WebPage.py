import nltk
import requests
from bs4 import BeautifulSoup

def obtener_texto_desde_url(url):
    # Obtener el contenido HTML de la página web
    response = requests.get(url)
    html = response.text

    # Utilizar BeautifulSoup para extraer texto del HTML
    soup = BeautifulSoup(html, "html.parser")
    texto = soup.get_text()

    return texto

# URL de la página web que deseas buscar
url = "https://www.guiainfantil.com/articulos/ocio/cuentos-infantiles/10-cuentos-cortos-para-leer-con-ninos/"
texto = obtener_texto_desde_url(url)
print(texto)

print("Antonio Fernando Fernández Cruz")

carpeta_nombre = 'Actividad_PLN_GitDash\\Documentos\\'
archivo_nombre = "archivo1.txt"

# Función para cargar texto desde un archivo
def cargar_texto_desde_archivo(carpeta_nombre, archivo_nombre):
    with open(carpeta_nombre + archivo_nombre, "r", encoding='utf-8') as archivo:
        texto = archivo.read()
    return texto

# Cargar texto desde el archivo
texto = cargar_texto_desde_archivo(carpeta_nombre, archivo_nombre)
print("----------------------------------------------------------------------")
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
    print(palabras_funcional)

print("----------------------------------------------------------------------")
tokens = nltk.word_tokenize(texto, "spanish")
tokens_limpios = []
for token in tokens:
    if token not in palabras_funcionales:
        tokens_limpios.append(token)
        print(tokens_limpios)

print(len(tokens))
print(len(tokens_limpios))
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)
distribucion_limpia.plot(40)
