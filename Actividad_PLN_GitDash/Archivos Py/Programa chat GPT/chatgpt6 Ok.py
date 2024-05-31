import openai

# Establecer la clave de la API
openai.api_key = ""

# Listar modelos
models = openai.Model.list()

# Imprimir el ID del primer modelo
print(models.data[0].id)

# Crear una conversación de chat
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

# Imprimir la respuesta de la conversación de chat
print(chat_completion.choices[0].message.content)
