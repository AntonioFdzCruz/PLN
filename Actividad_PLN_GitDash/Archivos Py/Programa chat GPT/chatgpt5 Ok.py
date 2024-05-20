import openai

# Especificar la clave de API manualmente
api_key = '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'

# Establecer la clave de API globalmente
openai.api_key = api_key

# Función para enviar una solicitud de chat a ChatGPT
def enviar_solicitud_chat(mensaje):
    respuesta = openai.Completion.create(
        engine="davinci",
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
