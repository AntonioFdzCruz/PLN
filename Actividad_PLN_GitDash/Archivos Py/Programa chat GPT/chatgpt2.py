import openai

# Configuración de la API de OpenAI
openai.api_key = ''

# Función para enviar una solicitud de chat a ChatGPT
def enviar_solicitud_chat(mensaje):
    respuesta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=mensaje,
        max_tokens=50,
        temperature=0.7
    )
    return respuesta.choices[0].text.strip()
# Función para interactuar con el usuario
def interactuar():
    print("¡Bienvenido al ChatGPT!")
    print("Puedes comenzar a escribir tus mensajes. Escribe 'salir' para terminar la conversación.")
    print("-----------------------------------------")

    # Loop de interacción
    while True:
        mensaje = input("Usuario: ")
        
        if mensaje.lower() == 'salir':
            break

        respuesta = enviar_solicitud_chat(mensaje)
        print("ChatGPT: " + respuesta)
        print("-----------------------------------------")

# Ejecutar la función de interacción
interactuar()
