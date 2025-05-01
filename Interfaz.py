import tkinter

# Ventana tk
ventana = tkinter.Tk()
ventana.geometry("650x400")

# Creación de título como label
etiqueta_titulo = tkinter.Label(ventana, 
                                text = "MENÚ GESTOR DE TAREAS",
                                bg = "light grey",
                                height = 2,
                                font = ("Arial", 20, "bold"))
etiqueta_titulo.pack(fill = tkinter.X)

# Creación de Botones para funciones principales
boton_agregar = tkinter.Button(ventana, text = "Agregar")
boton_agregar.pack()
boton_estado = tkinter.Button(ventana, text = "Cambiar Estado")
boton_estado.pack()
boton_eliminar = tkinter.Button(ventana, text = "Eliminar")
boton_eliminar.pack()
boton_vista = tkinter.Button(ventana, text = "Ver tareas")
boton_vista.pack()


ventana.mainloop()