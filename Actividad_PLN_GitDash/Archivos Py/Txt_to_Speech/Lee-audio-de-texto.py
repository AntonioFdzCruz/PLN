import pyttsx3

def texto_a_audio(texto):
    engine = pyttsx3.init()
    engine.save_to_file(texto, 'output_audio.wav')
    engine.runAndWait()

if __name__ == "__main__":
    texto = input("Ingrese el texto que desea convertir a audio: ")
    #texto = "D:\\Tony\\Documents\\MEGAsync\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\PLN\\texto_extraido.txt"
    texto_a_audio(texto)
    print("Texto convertido a audio y guardado como 'output_audio.wav'")
