import tkinter as tk
from tkinter import ttk

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
            "Botón de enviar mensaje:\n\n"
            "- Permite al usuario enviar el mensaje escrito al chatbot.\n\n"
            "Integración de entrada de voz:\n\n"
            "- Un botón para activar la entrada de voz y convertirla en texto.\n\n"
            "Guardar texto en archivo de texto (TXT):\n\n"
            "- Un botón para guardar el texto mostrado en el área de visualización en un archivo de texto (.txt).\n\n"
            "Guardar texto en archivo de audio:\n\n"
            "- Un botón para convertir el texto mostrado en el área de visualización en voz y guardar el archivo de audio resultante.\n\n"
            "Botón de impresión:\n\n"
            "- Un botón en la parte superior derecha de la ventana principal que permite al usuario imprimir el contenido del área de visualización.\n\n"
            "Botón especial 'Mi Trabajo':\n\n"
            "- Un botón que represente tu trabajo, con tu nombre 'Antonio Fernández Cruz'.\n\n"
            "Inclusión de asistencia con IA:\n\n"
            "- Mención de mí como 'Asistencia con IA'.\n\n"
            "Datos personales:\n\n"
            "- Universidad: Universidad de Colima\n"
            "- Campus: Coquimatlán\n"
            "- Facultad: FIME (Facultad de Ingeniería Mecánica y Eléctrica)\n"
            "- Carrera: ICI (Ingeniería en Computación Inteligente)\n"
            "- Grado: 6to\n"
            "- Grupo: B\n"
            "- Ubicación: Colima, México\n"
            "- Año: 2024\n"
            "Datos del curso:\n\n"
            "- Profesor: Dte. Carrillo Zepeda Oswaldo\n"
            "- Alumno: Antonio Fdo. Fernández Cruz\n"
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
        
        # Aquí puedes continuar con la implementación de la ventana principal

        self.root.mainloop()

# Crear la ventana "Especificaciones de Uso"
root = tk.Tk()
app = EspecificacionesVentana(root)
root.mainloop()