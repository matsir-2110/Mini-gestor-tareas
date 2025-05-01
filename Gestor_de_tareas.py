# Diccionario con tareas previamente escritas
tarea = {
    1: {"Tarea": "Estudiar para los parciales de la semana que viene", "Descripcion": "", "Estado": "Pendiente"},
    2: {"Tarea": "Ir al gimnasio todos los dias", "Descripcion": "", "Estado": "Pendiente"},
    3: {"Tarea": "Leer libros 3 horas por dia", "Descripcion": "", "Estado": "Pendiente"},
    4: {"Tarea": "Practicar tiros al arco de futbol", "Descripcion": "", "Estado": "Pendiente"}
}

# Imprimir las tareas escritas al inicio como referencia
i = 1
for i, datos in tarea.items():
    print("TAREA NÚMERO: ", i)
    print("Tarea: ", datos['Tarea'])
    print("Descripción: ", datos['Descripcion'])
    print("Estado: ", datos['Estado'])
    print("")

# Función para agregar tareas y descripciones 
def agregado():
    nueva_tarea = input("Escriba la tarea que desea agregar:  ")
    opcion = input("¿Desea agregar alguna descripcion? ").lower()

    if opcion == 'si':
        descripcion = input("Ingrese la descripción de la tarea:  ")
    else:
        descripcion = ""
    
    numero = 1
    while numero in tarea:
        numero += 1
    
    tarea[numero] = {"texto": nueva_tarea, "descripcion": descripcion, "Estado": "Pendiente"}
    print("Tarea agregada")

# Función para cambiar el estado de las tareas
def marcado():
    opcion = input("Desea cambiar el estado de alguna tarea? ").lower()
    if opcion == 'si':
        opcion_n = int(input("¿Que tarea desea cambiar? "))
        opcion_n2 = input("Elija COMPLETADO / PENDIENTE ")
        tarea[opcion_n]['Estado'] = opcion_n2
     
# Función para eliminar alguna de las tareas
def eliminado():
    opcion = input("¿Desea eliminar alguna tarea? ").lower()
    if opcion == 'si':
        opcion_n = int(input("¿Que tarea desea eliminar? (1/2/3/etc)"))
        tarea.pop(opcion_n)
        print("Tarea eliminada")

# Función para mostrar por pantalla la tarea, su descripción y estado
def listado():
    i = 1
    for i, datos in tarea.items():
        print("TAREA NÚMERO: ", i)
        print("Tarea: ", datos['Tarea'])
        print("Descripción: ", datos['Descripcion'])
        print("Estado: ", datos['Estado'])
        print("")

#Función que muestra el menú de opciones
def menus():
    print("\nMenu de tareas. Seleccione que desea hacer:")
    print("Agregar una tarea con descripción (AGREGAR)")
    print("Marcar una tarea como completada (MARCAR)")
    print("Eliminar una tarea (ELIMINAR)")
    print("Vista de las tareas con su estado. Completada / Pendiente (LISTADO)")
    menu = input().lower()

    if menu == 'agregar':
        agregado()
    if menu == 'marcar':
        marcado()
    if menu == 'eliminar':
        eliminado()
    if menu == 'listado':
        listado()

menus()

# Opción para volver al menú
opcion2 = input("¿Desea volver a seleccionar alguna de las opciones anteriores? ").lower()
if opcion2 == 'si':
    menus()