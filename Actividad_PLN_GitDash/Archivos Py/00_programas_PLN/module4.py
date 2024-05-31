def run_module4():
    print("Módulo 4 ejecutado - Tratamiento del archivo de Texto y conversión de estructura CSV")

print('Soy el archivo 4')



import pyaudio
import wave
import keyboard
import speech_recognition as sr
import pyttsx3
import os
import time
import threading

# Parámetros de configuración del audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5  # Duración de la grabación en segundos

def cuenta_regresiva():
    for i in range(RECORD_SECONDS, 0, -1):
        print('')
        print(f"Tiempo restante de grabación: {i} segundos")
        time.sleep(1)  # Espera 1 segundo

def grabar_audio():

    print('\n\n')
    print('----------------------------------------------------------')
    print("■ Presiona cualquier tecla para comenzar a grabar...")
    keyboard.read_event()  # Espera a que se presione una tecla
    
    frames = []

    # Configuración del dispositivo de audio
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # Iniciar cuenta regresiva en un hilo separado
    cuenta_regresiva_thread = threading.Thread(target=cuenta_regresiva)
    cuenta_regresiva_thread.start()

    # Obtener nombre de archivo único basado en el tiempo actual
    grabacion_filename = "\\00_programas_PLN\\archivos\\Audio_PLN_PASO_1.wav"

    # Grabación de audio
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Detener la grabación
    print(" • Fin de la grabación.\n\n")
    print(f' • Archivo de grabación guardado como: {grabacion_filename}')
    print('----------------------------------------------------------')
    stream.stop_stream()
    stream.close()
    p.terminate()
    cuenta_regresiva_thread.join()  # Esperar a que termine la cuenta regresiva

    # Guardar la grabación en un archivo WAV
    wf = wave.open(grabacion_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return grabacion_filename

def texto_a_audio(texto):
    # Obtener nombre de archivo único basado en el tiempo actual
    audio_filename = "\\00_programas_PLN\\archivos\\Audio_PLN_PASO_2.wav"

    # Inicializar el motor de texto a voz
    engine = pyttsx3.init()

    # Guardar el texto en un archivo de audio
    engine.save_to_file(texto, audio_filename)
    engine.runAndWait()

    print(f' • Archivo de audio generado a partir del texto guardado como: {audio_filename}')
    return audio_filename

def reconocer_audio(grabacion_filename):
    print("• Transcripción del audio:\n")
    r = sr.Recognizer()
    with sr.AudioFile(grabacion_filename) as source:
        try:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="es-ES")
            print(text)
            return text
        except sr.UnknownValueError:
            print("• • • Hubo un problema al transcribir el audio. Esto puede ser debido a la calidad del audio o dificultades en la detección del idioma.")
            return None

def reproducir_audio(audio_filename):
    print('\n----------------------------------------------------------')
    print("¿Deseas reproducir el audio generado a partir del texto? (s/n)")
    opcion = input()
    if opcion.lower() == 's':
        os.system(audio_filename)
    elif opcion.lower() == 'n':
        return
    else:
        print("► Por favor, ingresa 's' para reproducir el audio o 'n' para omitir ◄")

def leer_archivo():
    # print('----------------------------------------------------------')
    print("■ Leyendo archivo de texto:")
    print('')
    archivo_texto = "texto_PLN.txt"
    if os.path.exists(archivo_texto):
        try:
            with open(archivo_texto, "r", encoding="utf-8") as file:
                contenido = file.read()
                print(contenido)
                audio_filename = texto_a_audio(contenido)
                reproducir_audio(audio_filename)
        except UnicodeDecodeError:
            print("• • • El archivo de texto que se desea reproducir no está codificado con UTF-8. • • •")
    else:
        print("•► El archivo de texto no existe‼")

# Lógica principal del programa
while True:
    grabacion_filename = grabar_audio()

    texto = reconocer_audio(grabacion_filename)
    if texto is None:
        print("• • • Se produjo un error al transcribir el audio. ¿Deseas volver a grabar el audio? (s/n)")
        opcion = input()
        if opcion.lower() == 's':
            continue
        else:
            print("¡Hasta luego!")
            break

    leer_archivo()

    print('----------------------------------------------------------')
    print("• ¿Deseas grabar otro audio? (s/n)")
    opcion = input()
    if opcion.lower() != 's':
        print("¡Hasta luego!")
        break
 
