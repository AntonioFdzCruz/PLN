import os
import pyttsx3
import pygame

def leer_archivo():
    print("■ Leyendo archivo de texto:")
    print('')
    archivo_texto = "./texto_PLN.txt"
    if os.path.exists(archivo_texto):
        try:
            with open(archivo_texto, "r", encoding="utf-8") as file:
                contenido = file.read()
                print(contenido)
                texto_a_audio(contenido)
        except UnicodeDecodeError:
            print("• • • El archivo de texto que se desea reproducir no está codificado con UTF-8. • • •")
    else:
        print("•► El archivo de texto no existe‼")

def texto_a_audio(texto):
    engine = pyttsx3.init()
    engine.save_to_file(texto, 'Audio_PLN_ttsX3.wav')  # Guarda el audio en un archivo
    engine.runAndWait()
    reproducir_audio('Audio_PLN_ttsX3.wav')

def reproducir_audio(nombre_archivo):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(nombre_archivo)
    pygame.mixer.music.play()

    # Esperar a que se termine de reproducir
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Lógica principal del programa
os.system('cls')
os.system('pause')
print('\n\n')
print('----------------------------------------------------------')
print("¿Deseas leer el archivo de texto? (s/n)")
opcion = input()
if opcion.lower() == 's':
    leer_archivo()
else:
    print('----------------------------------------------------------\n\n\n')
    print("¡Hasta luego!")
    print('\n\n\n')

os.system('pause')
