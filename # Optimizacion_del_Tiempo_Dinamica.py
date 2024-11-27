# Función para ingresar las actividades
def ingresar_actividades():
    actividades = []
    while True:
        nombre_actividad = input("Ingrese el nombre de la actividad (o 'fin' para terminar): ")
        if nombre_actividad.lower() == 'fin':
            break
        duracion = int(input(f"Ingrese la duración de la actividad '{nombre_actividad}' en horas: "))
        prioridad = int(input(f"Ingrese la prioridad de la actividad '{nombre_actividad}' (valor numérico): "))
        actividades.append({"nombre": nombre_actividad, "duracion": duracion, "prioridad": prioridad})
    return actividades

# Función principal para Programación Dinámica
def Optimizacion_del_Tiempo_Dinamica():
    # Ingresar el nombre de la persona
    persona = input("Ingrese el nombre de la persona a organizarle el tiempo: ")

    # Ingresar actividades
    actividades = ingresar_actividades()

    # Ingresar el tiempo disponible
    tiempo_disponible = int(input("Ingrese el tiempo disponible en horas: "))

    # Inicializar el arreglo pd[] donde pd[i] representa la máxima prioridad alcanzable con i tiempo disponible
    pd = [0] * (tiempo_disponible + 1)

    # Llenar el arreglo pd usando programación dinámica
    for actividad in actividades:
        for tiempo in range(tiempo_disponible, actividad["duracion"] - 1, -1):
            pd[tiempo] = max(pd[tiempo], pd[tiempo - actividad["duracion"]] + actividad["prioridad"])

    # Mostrar la organización de tiempo con las actividades seleccionadas
    print(f"\nOrganización de tiempo para {persona}:")
    print(f"Máxima prioridad alcanzable: {pd[tiempo_disponible]}")
    print("Actividades organizadas según prioridad y tiempo disponible:")

    # Mostrar las actividades que se seleccionaron (con la máxima prioridad alcanzable)
    tiempo_restante = tiempo_disponible
    for actividad in reversed(actividades):
        if tiempo_restante - actividad["duracion"] >= 0 and pd[tiempo_restante] == pd[tiempo_restante - actividad["duracion"]] + actividad["prioridad"]:
            print(f"{actividad['nombre']} - Duración: {actividad['duracion']} horas, Prioridad: {actividad['prioridad']}")
            tiempo_restante -= actividad["duracion"]

# Ejecutar la función principal
Optimizacion_del_Tiempo_Dinamica()