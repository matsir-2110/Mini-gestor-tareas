# ---LA INTERFAZ ESTA EN PROCESO---
import tkinter

# Ventana tk
ventana = tkinter.Tk()
ventana.geometry("650x425")

# Título en forma de label
etiqueta_titulo = tkinter.Label(ventana, 
                                text = "MENÚ GESTOR DE TAREAS",
                                bg = "SlateGray4",
                                height = 2,
                                font = ("Arial", 20, "bold"))
etiqueta_titulo.pack(fill = tkinter.X, pady = 10)

# Creación de Botones para funciones principales
#Botón para agregar tareas
boton_agregar = tkinter.Button(ventana,
                               text = "Agregar",
                               font = ("Arial", 12, "bold"),
                               width = 20,
                               height = 2,
                               background = "DarkSeaGreen3",
                               activebackground = "DarkSeaGreen4")
boton_agregar.pack(pady = 15)

#Botón para cambiar estado de tareas
boton_estado = tkinter.Button(ventana,
                              text = "Cambiar Estado",
                              font = ("Arial", 12, "bold"),
                              width = 20,
                              height = 2,
                              background = "DarkSeaGreen3",
                              activebackground = "DarkSeaGreen4")
boton_estado.pack(pady = 15)

#Botón para eliminar tareas
boton_eliminar = tkinter.Button(ventana,
                                text = "Eliminar",
                                font = ("Arial", 12, "bold"),
                                width = 20,
                                height = 2,
                                background = "DarkSeaGreen3",
                                activebackground = "DarkSeaGreen4")
boton_eliminar.pack(pady = 15)

#Botón para ver todas las tareas
boton_vista = tkinter.Button(ventana,
                             text = "Ver tareas",
                             font = ("Arial", 12, "bold"),
                             width = 20,
                             height = 2,
                             background = "DarkSeaGreen3",
                             activebackground = "DarkSeaGreen4")
boton_vista.pack(pady = 15)


ventana.mainloop()