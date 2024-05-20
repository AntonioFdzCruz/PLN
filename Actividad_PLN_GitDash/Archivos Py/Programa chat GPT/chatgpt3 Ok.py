import openai_chat

# Especificar la clave de API manualmente
api_key = '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'

# Crear una instancia del cliente ChatGPT con la clave API especificada
chatgpt = openai_chat.ChatCompletion(api_key=api_key)

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

        respuesta = chatgpt.complete_message(mensaje)
        print("ChatGPT: " + respuesta)
        print("-----------------------------------------")

# Ejecutar la función de interacción
interactuar()
