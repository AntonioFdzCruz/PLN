'''
python -m pip install -U pip

pip install winspeech

pip install SpeechRecognition
'''
import pyaudio
import wave
import speech_recognition as sr

def grabar_audio(nombre_archivo, duracion):
    formato = pyaudio.paInt16
    canales = 1
    tasa_muestreo = 44100
    tamano_buffer = 1024

    audio = pyaudio.PyAudio()

    stream = audio.open(format=formato, channels=canales, rate=tasa_muestreo, input=True, frames_per_buffer=tamano_buffer)

    print("Grabando audio...")

    frames = []

    for i in range(0, int(tasa_muestreo / tamano_buffer * duracion)):
        data = stream.read(tamano_buffer)
        frames.append(data)

    print("Grabación finalizada.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    archivo_salida = wave.open(nombre_archivo, 'wb')
    archivo_salida.setnchannels(canales)
    archivo_salida.setsampwidth(audio.get_sample_size(formato))
    archivo_salida.setframerate(tasa_muestreo)
    archivo_salida.writeframes(b''.join(frames))
    archivo_salida.close()

def convertir_audio_a_texto(nombre_archivo):
    reconocedor = sr.Recognizer()

    with sr.AudioFile(nombre_archivo) as fuente:
        audio = reconocedor.record(fuente)

    try:
        texto = reconocedor.recognize_google(audio, language='es-ES')
        print("Texto reconocido:")
        print(texto)
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
    except sr.RequestError as e:
        print("Error al solicitar resultados al servicio de reconocimiento de voz de Google: {0}".format(e))

# Nombre del archivo de audio
nombre_archivo = "audio_PLN.wav"

# Duración de la grabación en segundos
duracion_grabacion = 15

# Grabar audio desde el micrófono
grabar_audio(nombre_archivo, duracion_grabacion)

# Convertir audio a texto
convertir_audio_a_texto(nombre_archivo)
