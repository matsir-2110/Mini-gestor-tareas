# Integrantes Costantini M. Mortola S. Repka M.
tarea = {
    1: {"Tarea": "Estudiar para los parciales de la semana que viene", "descripcion": "", "completada": False},
    2: {"Tarea": "Ir al gimnasio todos los dias", "descripcion": "", "completada": False},
    3: {"Tarea": "Leer libros 3 horas por dia", "descripcion": "", "completada": False},
    4: {"Tarea": "Practicar tiros al arco de futbol", "descripcion": "", "completada": False}
}

def agregado():
    nueva_tarea = input("Escriba la tarea que desea agregar:  ")
    opcion = input("¿Desea agregar alguna descripcion?").lower()

    if opcion == 'si':
        descripcion = input("Ingrese la descripción de la tarea:  ")
    else:
        descripcion = ""
    
    numero = 1
    while numero in tarea:
        numero += 1
    
    tarea[numero] = {"texto": nueva_tarea, "descripcion": descripcion, "completada": False}
    print("Tarea agregada")

#def marcado():
    # Agregar prox

#def eliminado():
    # Agregar prox

#def estados():
    # Agregar prox

#def mostrar_tareas():
    # Agregar pro

def menus():
    print("\nMenu de tareas. Seleccione que desea hacer:")
    print("Agregar una tarea con descripción (AGREGAR)")
    print("Marcar una tarea como completada (MARCAR)")
    print("Eliminar una tarea (ELIMINAR)")
    print("Estado de las tareas. Completada / Pendiente (ESTADO)")
    print("Mostrar tareas (MOSTRAR)")
    menu = input().lower()

    if menu == 'agregar':
        agregado()
    if menu == 'marcar':
        marcado()
    if menu == 'eliminar':
        eliminado()
    if menu == 'estado':
        estados()
    if menu == 'mostrar':
        mostrar_tareas()
menus()

opcion2 = input("¿Desea volver a seleccionar alguna de las opciones anteriores?").lower()
if opcion2 == 'si':
    menus()