import itertools

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

# Función principal para Fuerza Bruta
def Optimizacion_del_Tiempo_Fuerza_Bruta():
    # Ingresar el nombre de la persona
    persona = input("Ingrese el nombre de la persona a organizarle el tiempo: ")

    # Ingresar actividades
    actividades = ingresar_actividades()

    # Ingresar el tiempo disponible
    tiempo_disponible = int(input("Ingrese el tiempo disponible en horas: "))

    # Inicializar variables para almacenar la mejor solución
    mejor_solucion = []
    mejor_prioridad = 0

    # Generar todas las combinaciones posibles de actividades
    for i in range(1, len(actividades) + 1):
        combinaciones = itertools.combinations(actividades, i)
        for combinacion in combinaciones:
            duracion_total = sum(actividad["duracion"] for actividad in combinacion)
            if duracion_total <= tiempo_disponible:
                prioridad_total = sum(actividad["prioridad"] for actividad in combinacion)
                if prioridad_total > mejor_prioridad:
                    mejor_prioridad = prioridad_total
                    mejor_solucion = combinacion

    # Mostrar la organización de tiempo con las actividades seleccionadas
    print(f"\nOrganización de tiempo para {persona}:")
    print(f"Mejor prioridad alcanzable: {mejor_prioridad}")
    print("Actividades organizadas según prioridad y tiempo disponible:")

    # Mostrar las actividades seleccionadas
    for actividad in mejor_solucion:
        print(f"{actividad['nombre']} - Duración: {actividad['duracion']} horas, Prioridad: {actividad['prioridad']}")

# Ejecutar la función principal
Optimizacion_del_Tiempo_Fuerza_Bruta()
