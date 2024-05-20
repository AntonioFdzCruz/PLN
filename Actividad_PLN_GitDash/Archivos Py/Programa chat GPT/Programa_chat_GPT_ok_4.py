import tkinter as tk
from tkinter import ttk
import pyttsx3  # Para la conversión de texto a voz
from tkinter import filedialog
from datetime import datetime

class EspecificacionesVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Especificaciones de Uso")

        # Frame para las especificaciones
        self.frame_especificaciones = tk.Frame(self.root)
        self.frame_especificaciones.pack(pady=20)

        # Texto de las especificaciones con scrollbar
        self.scrollbar = tk.Scrollbar(self.frame_especificaciones, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        self.especificaciones_texto = (
            "Interfaz gráfica con Tkinter:\n\n"
            "- Una ventana principal con un área de texto para ingresar mensajes.\n"
            "- Un área de visualización para mostrar respuestas del chatbot.\n"
            "- Un logotipo en el centro superior de la ventana.\n\n"
            "- Botón de enviar mensaje:\n"
            "  Permite al usuario enviar el mensaje escrito al chatbot.\n\n"
            "- Integración de entrada de voz:\n"
            "  Un botón para activar la entrada de voz y convertirla en texto.\n\n"
            "- Guardar texto en archivo de texto (TXT):\n"
            "  Un botón para guardar el texto mostrado en el área de visualización en un archivo de texto (.txt).\n\n"
            "- Guardar texto en archivo de audio:\n"
            "  Un botón para convertir el texto mostrado en el área de visualización en voz y guardar el archivo de audio resultante.\n\n"
            "- Botón de impresión:\n"
            "  Un botón en la parte superior derecha de la ventana principal que permite al usuario imprimir el contenido del área de visualización.\n\n"
            "- Botón especial 'Mi Trabajo':\n"
            "  Un botón que represente tu trabajo, con tu nombre 'Antonio Fernández Cruz'.\n\n"
            "- Inclusión de asistencia con IA:\n"
            "  Mención de mí como 'Asistencia con IA'.\n\n"
            "Datos personales:\n\n"
            "- Universidad: Universidad de Colima\n"
            "- Campus: Coquimatlán\n"
            "- Facultad: FIME (Facultad de Ingeniería Mecánica y Eléctrica)\n"
            "- Carrera: ICI (Ingeniería en Computación Inteligente)\n"
            "- Grado: 6to\n"
            "- Grupo: B\n"
            "- Ubicación: Colima, México\n"
            "- Año: 2024\n"
            "- Datos del curso:\n"
            "  - Profesor: Dte. Carrillo Zepeda Oswaldo\n"
            "  - Alumno: Antonio Fdo. Fernández Cruz\n"
            "- Curso: PLN (Procesamiento de Lenguaje Natural)\n"
            "  - Profesor: Dte. Carrillo Zepeda Oswaldo\n"
            "  - Alumno: Antonio Fdo. Fernández Cruz\n"
        )

        self.text_especificaciones = tk.Text(self.frame_especificaciones, wrap="word", yscrollcommand=self.scrollbar.set)
        self.text_especificaciones.insert(tk.END, self.especificaciones_texto)
        self.text_especificaciones.pack(side="left", fill="both", expand=True)

        self.scrollbar.config(command=self.text_especificaciones.yview)

         # Botón para comenzar
        self.boton_comenzar = tk.Button(self.root, text="Comenzar con MiChatcitoGPT", command=self.abrir_ventana_principal)
        self.boton_comenzar.pack(pady=10)

    def abrir_ventana_principal(self):
        # Cerrar la ventana actual y abrir la ventana principal
        self.root.destroy()
        VentanaPrincipal()

class VentanaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MiChatcitoGPT")

        # Interfaz gráfica con Tkinter
        self.crear_interfaz()

        self.root.mainloop()

    def crear_interfaz(self):
        # Frame para el encabezado
        self.frame_encabezado = tk.Frame(self.root)
        self.frame_encabezado.pack(fill="x")

        # Logotipo
        self.logo = tk.Label(self.frame_encabezado, text="MiChatcitoGPT", font=("Arial", 18))
        self.logo.pack(pady=10)

        # Área de texto para ingresar mensajes
        self.texto_ingreso = tk.Text(self.root, height=10, width=50)
        self.texto_ingreso.pack(pady=10)

        # Botón de enviar mensaje
        self.boton_enviar = tk.Button(self.root, text="Enviar", command=self.enviar_mensaje)
        self.boton_enviar.pack(pady=5)

        # Área de visualización para respuestas del chatbot
        self.area_respuesta = tk.Text(self.root, height=10, width=50)
        self.area_respuesta.pack(pady=10)

        # Botones para guardar texto en archivo de texto (TXT) y guardar texto en archivo de audio
        self.boton_guardar_txt = tk.Button(self.root, text="Guardar TXT", command=self.guardar_txt)
        self.boton_guardar_txt.pack(side="left", padx=5)

        self.boton_guardar_audio = tk.Button(self.root, text="Guardar Audio", command=self.guardar_audio)
        self.boton_guardar_audio.pack(side="left", padx=5)

    def enviar_mensaje(self):
        # Función para enviar el mensaje escrito al chatbot
        pass

    def guardar_txt(self):
        # Función para guardar el texto en un archivo de texto (.txt)
        texto = self.area_respuesta.get("1.0", tk.END)
        nombre_archivo = f"conversacion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        ruta = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=nombre_archivo)
        if ruta:
            with open(ruta, "w") as archivo:
                archivo.write(texto)

    def guardar_audio(self):
        # Función para guardar el texto en un archivo de audio
        texto = self.area_respuesta.get("1.0", tk.END)
        engine = pyttsx3.init()
        engine.save_to_file(texto, "conversacion_audio.mp3")
        engine.runAndWait()

# Crear la ventana "Especificaciones de Uso"
root = tk.Tk()
app = EspecificacionesVentana(root)
root.mainloop()