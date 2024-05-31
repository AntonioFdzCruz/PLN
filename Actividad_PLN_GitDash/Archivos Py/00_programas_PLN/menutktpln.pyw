import tkinter as tk
import sys
import importlib
from tkinter import ttk  # Agrega esta línea para importar el módulo ttk


#utilizare:
import os
import pyttsx3
import pygame
import pyaudio
import wave
import keyboard
import speech_recognition as sr
import time
import threading
import requests
import re
import nltk
from nltk.corpus import stopwords




#D:\\00_programas_PLN\\archivos\\
#ruta:  D:\\Tony\\Documents\\MEGAsync\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\PLN\\Actividad_PLN_GitDash\\Archivos Py\\Programas_PLN\\archivos\\


class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)


def main():
    ventana = tk.Tk()
    ventana.title("• Programas PLN • ")
    # Configurar el color de fondo de la ventana
    ventana.configure(bg="#FFC000")

    def limpiar_pantalla():
        consola.delete('1.0', tk.END)


    def programa1():
        # sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module1")
        module.run_module1()
        pass

    def programa2():
        # sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module2")
        # module.run_module2()
        pass

    def programa3():
        # sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module3")
        # module.run_module3()
        pass

    def programa4():
        # sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module4")
        # module.run_module4()
        pass

    def programa5():
        # sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module5")
        # module.run_module5()
        pass

    def programa6():
        # sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module6")
        # module.run_module6()
        pass

    def programa7():
        # sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module7")
        # module.run_module7()
        pass

    def programa8():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module8")
        module.run_module8()
        pass

    def programa9():
        # sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module9")
        # module.run_module9()
        pass    

    def programa10():
        # sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module10")
        # module.run_module10()
        pass      

    # Crear un contenedor para las dos columnas
    contenedor = tk.Frame(ventana)
   
    imagen = tk.PhotoImage(file="LogoAffCbanner.png")
    porcentaje = 1  # Porcentaje de cambio de tamaño (ejemplo: 50% para reducir a la mitad)

    # Calcular las nuevas dimensiones de la imagen
    nuevo_ancho = int(imagen.width() * porcentaje / 20)
    nuevo_alto = int(imagen.height() * porcentaje / 20)

    # Redimensionar la imagen proporcionalmente
    imagen = imagen.subsample(porcentaje)

    # Mostrar la imagen a la izquierda del título
    label_imagen = tk.Label(ventana, image=imagen, borderwidth=0)
    # label_imagen.pack(side=tk.LEFT)
    label_imagen.pack(anchor="n")

    linea_divisoria = tk.ttk.Separator(ventana, orient="horizontal")
    linea_divisoria.pack(fill="x", padx=10, pady=10)
    

    consola = tk.Text(ventana, width=100, height=20)

    # Crear una barra de desplazamiento vertical
    scrollbar = tk.Scrollbar(ventana, command=consola.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Asociar la barra de desplazamiento con el widget de texto
    consola.config(yscrollcommand=scrollbar.set)

    consola.pack()

    linea_divisoria = tk.ttk.Separator(ventana, orient="horizontal")
    linea_divisoria.pack(fill="x", padx=10, pady=10)


    contenedor.pack()
 
    # Crear los botones y colocarlos en la primera columna
    # for i in range(4):
    boton = tk.Button(contenedor, command=programa1, bg="darkgray",text="Programa 1")
    boton.grid(row=0, column=0, padx=10, pady=5)
    boton = tk.Button(contenedor, command=programa2, bg="darkgray",text="Programa 2")
    boton.grid(row=1, column=0, padx=10, pady=5)
    boton = tk.Button(contenedor, command=programa3, bg="darkgray",text="Programa 3")
    boton.grid(row=2, column=0, padx=10, pady=5)
    boton = tk.Button(contenedor, command=programa4, bg="darkgray",text="Programa 4")
    boton.grid(row=3, column=0, padx=10, pady=5)
    boton = tk.Button(contenedor, command=programa5, bg="darkgray",text="Programa 5")
    boton.grid(row=4, column=0, padx=10, pady=5)

    # Crear las etiquetas y colocarlas en la segunda columna
    etiqueta = tk.Label(contenedor, text="*.py → *.exe")
    etiqueta.grid(row=0, column=1, padx=10, pady=5)
    etiqueta = tk.Label(contenedor, text="RecSnd→TxT & Print TxT ←RecSnd")
    etiqueta.grid(row=1, column=1, padx=10, pady=5)
    etiqueta = tk.Label(contenedor, text="TxT→Snd & PlaySnd")
    etiqueta.grid(row=2, column=1, padx=10, pady=5)
    etiqueta = tk.Label(contenedor, text="Snd→TxT & TxT→Snd")
    etiqueta.grid(row=3, column=1, padx=10, pady=5)
    etiqueta = tk.Label(contenedor, text="TxT|Docx→Snd & Play")
    etiqueta.grid(row=4, column=1, padx=10, pady=5)

    boton = tk.Button(contenedor, command=programa6, bg="red",text="Programa 6")
    boton.grid(row=0, column=3, padx=10, pady=5)
    boton = tk.Button(contenedor, command=programa7, bg="darkgray",text="Programa 7")
    boton.grid(row=1, column=3, padx=10, pady=5)
    boton = tk.Button(contenedor, command=programa8, bg="darkgray",text="Programa 8")
    boton.grid(row=2, column=3, padx=10, pady=5)
    boton = tk.Button(contenedor, command=programa9, bg="darkgray",text="Programa 9")
    boton.grid(row=3, column=3, padx=10, pady=5)
    boton = tk.Button(contenedor, command=programa10, bg="darkgray",text="Programa 10")
    boton.grid(row=4, column=3, padx=10, pady=5)
    
        # Crear las etiquetas y colocarlas en la segunda columna
    etiqueta = tk.Label(contenedor, text="Chat GPT")
    etiqueta.grid(row=0, column=4, padx=10, pady=5)
    etiqueta = tk.Label(contenedor, text="Análisis de Sentimientos")
    etiqueta.grid(row=1, column=4, padx=10, pady=5)
    etiqueta = tk.Label(contenedor, text="Chunking: parser")
    etiqueta.grid(row=2, column=4, padx=10, pady=5)
    etiqueta = tk.Label(contenedor, text="Chunking ne_chunk")
    etiqueta.grid(row=3, column=4, padx=10, pady=5)
    etiqueta = tk.Label(contenedor, text="Análisis PLN en página web")
    etiqueta.grid(row=4, column=4, padx=10, pady=5)

    boton = tk.Button(contenedor, command=limpiar_pantalla, bg="#4169E1",text="Limpiar Pantalla", height=3)#
    boton.grid(row=2, column=5, padx=30, pady=0)


    ventana.mainloop()
 


if __name__ == "__main__":
    main()
