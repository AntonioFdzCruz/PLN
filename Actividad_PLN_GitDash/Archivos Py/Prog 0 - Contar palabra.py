
#Prog 05

"""
D:\\Tony\\Documents\\MEGAsync\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\Programas2024\\Documentos\\archivo1.txt
"""

import os
os.system('cls')

def verificar_archivo(archivo):
    if os.path.isfile(archivo):
        print("El archivo '{}' existe.".format(archivo))
        return True
    else:
        print("Error: El archivo '{}' no existe.".format(archivo))
        return False

def buscar_palabra(archivo, palabra):
    try:
        with open("D:\\Tony\\Documents\\MEGAsync\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\Programas2024\\Documentos\\archivo1.txt", 'r', encoding='utf-8') as archivo_txt:
            contenido = archivo_txt.read()
            palabra = palabra.lower()  # Convertir la palabra a minúsculas para hacer la búsqueda insensible a mayúsculas y minúsculas
            conteo = contenido.lower().count(palabra)
            if conteo > 0:
                print("La palabra '{}' se encontró {} veces en el archivo.".format(palabra, conteo))
            else:
                print("La palabra '{}' no se encontró en el archivo.".format(palabra))
    except PermissionError:
        print("Error: No tienes permiso para acceder al archivo '{}'.".format(archivo))
    except Exception as e:
        print("Ocurrió un error:", e)


def main():
    os.system('cls')
    archivo = input("\n\n\n\n\nIngrese la ruta y nombre del archivo de texto (incluya la extensión .txt): ")
    if not verificar_archivo(archivo):
        return
    
    while True:
        os.system('cls')
        palabra = input("\n\n\nIngrese la palabra que desea buscar en el archivo: ")
        buscar_palabra(archivo, palabra)
        
        respuesta = input("\n\n¿Desea buscar otra palabra en el mismo archivo? (s/n): ")
        if respuesta.lower() != 's':
            os.system('cls')
            break

if __name__ == "__main__":
    main()