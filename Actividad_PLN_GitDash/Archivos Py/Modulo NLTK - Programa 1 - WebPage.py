'''
Programas en phyton Modulo NLTK
programa 1

El ejercicio consiste en encontrar todas las "palabras" de 3 o 4 letras
- Se entiende por "palabra" CUALQUIER coosa entre espacios
'''
import re
import requests

# URL de la página web que deseas buscar
url = "https://www.guiainfantil.com/articulos/ocio/cuentos-infantiles/10-cuentos-cortos-para-leer-con-ninos/"

# Obtener el contenido HTML de la página web
response = requests.get(url)
html = response.text

# Expresión regular para encontrar palabras de 3 o 4 letras
expresion_regular = re.compile(r"\b\w{3,4}\b")

# Buscar palabras de 3 o 4 letras en el contenido HTML
resultados_busqueda = expresion_regular.finditer(html)

# Imprimir las palabras encontradas
for resultado in resultados_busqueda:
    print(resultado.group(0))
