import tkinter

ventana_agregar = tkinter.Tk()
ventana_agregar.geometry("300x300")

#Título del apartado
titulo_agregar = tkinter.Label(ventana_agregar,
                                 text = "AGREGADO DE TAREAS",
                                 width = 20,
                                 height = 2,
                                 background = "light grey",
                                 font = ("Arial", 12, "bold"))
titulo_agregar.pack(pady = 20)

#Label de entrada de dato principal
label_ag = tkinter.Label(ventana_agregar,
                              text = "Escriba la Tarea")
label_ag.pack()

#Entry de dato principal (agregar tarea)
tarea_agregar = tkinter.Entry(ventana_agregar,
                              font = ("Arial", 13))
tarea_agregar.pack()

#Función que guarda lo que ingresa el usuario
def bot_agg():
    texto = tarea_agregar.get()
    print(texto)

#Botón que al tocarlo, guarda la info
bot_agregar = tkinter.Button(ventana_agregar,
                             text = "Guardar",
                             command = lambda: bot_agg())
bot_agregar.pack()


#Espacio entre Entrys
label_espacio = tkinter.Label()
label_espacio.pack(pady = 7)


#Descripción de la tarea
label_desc = tkinter.Label(ventana_agregar,
                              text = "Descripción de la Tarea")
label_desc.pack(pady = 5)

desc_agregar = tkinter.Entry(ventana_agregar,
                              font = ("Arial", 13))
desc_agregar.pack()

#Función que guarda lo que ingresa el usuario
def bot_agg_desc():
    texto = desc_agregar.get()
    print(texto)

#Botón que al tocarlo, guarda la info
bot_agregar_desc = tkinter.Button(ventana_agregar,
                             text = "Guardar",
                             command = lambda: bot_agg_desc())
bot_agregar_desc.pack()




ventana_agregar.mainloop()