import tkinter as tk
import sys
import importlib
from tkinter import ttk  # Agrega esta línea para importar el módulo ttk



class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)



# # Crear la ventana principal
# ventana = tk.Tk()

# # Crear el widget de texto "consola"
# consola = tk.Text(ventana)

# # Empaquetar el widget de texto en la ventana
# consola.pack()


def main():
    ventana = tk.Tk()
    ventana.title("• Programas PLN • ")
    # Configurar el color de fondo de la ventana
    ventana.configure(bg="#FFC000")

    def limpiar_pantalla():
        consola.delete('1.0', tk.END)


    def programa1():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module1")
        module.run_module1()
        pass

    def programa2():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module2")
        module.run_module2()
        pass

    def programa3():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module3")
        module.run_module3()
        pass

    def programa4():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module4")
        module.run_module4()
        pass

    def programa5():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module5")
        module.run_module5()
        pass

    def programa6():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module6")
        module.run_module6()
        pass

    def programa7():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module7")
        module.run_module7()
        pass

    def programa8():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module8")
        module.run_module8()
        pass

    def programa9():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module9")
        module.run_module9()
        pass    

    def programa10():
        sys.stdout = StdoutRedirector(consola)
        module = importlib.import_module("module10")
        module.run_module10()
        pass      



    # # Cargar la imagen
    # imagen = tk.PhotoImage(file="LogoAffC.png",height=140, width=205)#  

    # # Mostrar la imagen en la ventana
    # label_imagen = tk.Label(ventana, image=imagen)
    # label_imagen.pack()

    

    
    


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


    # boton_limpiar = tk.Button(ventana, text="Limpiar Pantalla", command=limpiar_pantalla, bg="red")

    # Crear los botones y colocarlos en la segunda columna
    # for i in range(4, 9):
        # boton = tk.Button(contenedor, text=f"Botón {i+1}")
        # boton.grid(row=i-4, column=1, padx=10, pady=10)



    # boton1 = tk.Button(ventana, text="Programa 1", command=programa1, bg="darkgray")
    # boton1.pack(anchor="nw")

    # boton2 = tk.Button(ventana, text="Programa 2", command=programa2, bg="green")
    # boton2.pack(anchor="nw")

    # boton3 = tk.Button(ventana, text="Programa 3", command=programa3, bg="darkgray")
    # boton3.pack(anchor="nw")

    # boton4 = tk.Button(ventana, text="Programa 4", command=programa4, bg="green")
    # boton4.pack(anchor="nw")


    


    # consola = tk.Text(ventana, width=80, height=10)

    # # Crear una barra de desplazamiento vertical
    # scrollbar = tk.Scrollbar(ventana, command=consola.yview)
    # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # # Asociar la barra de desplazamiento con el widget de texto
    # consola.config(yscrollcommand=scrollbar.set)

    # consola.pack()

    # linea_divisoria = tk.ttk.Separator(ventana, orient="horizontal")
    # linea_divisoria.pack(fill="x", padx=10, pady=10)

    ventana.mainloop()
    # root.mainloop()



if __name__ == "__main__":
    main()
