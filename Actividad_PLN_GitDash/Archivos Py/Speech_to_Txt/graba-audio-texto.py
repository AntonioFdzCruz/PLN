
'''
python -m pip install -U pip

pip install winspeech

pip install SpeechRecognition


'''
import pyaudio
import wave
import threading
import queue
import sys
import speech_recognition as sr

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
frames = []
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Utilizamos una cola (queue) para comunicarnos entre los hilos
audio_queue = queue.Queue()

def record_audio():
    while True:
        data = stream.read(CHUNK)
        audio_queue.put(data)

def save_audio():
    frames = []
    while True:
        data = audio_queue.get()
        frames.append(data)
        if data == b'':  # Verificamos si la cola está vacía
            break

    wf = wave.open("./audio_PLN(graba-audio-texto).wav", "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    stream.stop_stream()
    stream.close()
    p.terminate()

print("Presiona ENTER para comenzar la grabación. Presiona ENTER nuevamente para detenerla.")
input("Presiona ENTER para comenzar...")

# Iniciamos los hilos para grabar y guardar el audio
record_thread = threading.Thread(target=record_audio)
save_thread = threading.Thread(target=save_audio)

record_thread.start()
save_thread.start()

input()  # Esperamos a que se presione ENTER nuevamente

audio_queue.put(b'')  # Agregamos una marca para indicar el final de la grabación

record_thread.join()
save_thread.join()

print("Grabación finalizada. El audio se ha guardado en 'grabacion.wav'.")