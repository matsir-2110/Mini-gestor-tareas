import tkinter

# Ventana tk
ventana = tkinter.Tk()
ventana.geometry("600x500")

# Creación de título como etiqueta
etiqueta_titulo = tkinter.Label(ventana, text = "MINI GESTOR DE TAREAS", bg = "light grey")
etiqueta_titulo.pack(fill = tkinter.X)



ventana.mainloop()