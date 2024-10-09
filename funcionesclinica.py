pacientes = []
def menu_principal():
    print('''\n--- Menú del Sistema de Gestión de Pacientes ---"
    1. Cargar pacientes
    2. Mostrar lista de pacientes
    3. Buscar paciente por Historia Clínica
    4. Ordenar pacientes por Historia Clínica
    5. Determinar paciente con más días de internación
    6. Determinar paciente con menos días de internación
    7. Cantidad de pacientes con mas de 5 dias de internacion
    8. Promedio de dias de internacion de todos los pacientes
    9. Salir''')

def cargar_pacientes(pacientes: list) -> list:
    n = int(input("Ingrese la cantidad de pacientes que desee: "))
    for _ in range(n):
        numero_clinico = int(input("Ingrese numero de historia clinica: "))
        while numero_clinico < 0000 or numero_clinico > 9999:
            numero_clinico = input("Error, Ingrese numero de historia clinica:  ")
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        diagnostico = input("Diagnóstico: ")
        dias_internacion = int(input("Ingrese cantidad de días de internación: "))
        pacientes.append([numero_clinico, nombre, edad, diagnostico, dias_internacion])
        print(pacientes)
    return pacientes

def mostrar_lista_pacientes(pacientes: list):
    if  len(pacientes) == 0:
        print("No hay pacientes almacenados.")
    else:
        print("pacientes")
        for paciente in pacientes:
            print(paciente)

def buscar_paciente(pacientes: list, historia_clinico: int):
    for paciente in pacientes: 
        if historia_clinico == paciente[0] :
            return paciente
    return None    

def ordenar_pacientes(pacientes: list) -> list:
    if not pacientes:
        print("No hay pacientes almacenados.")
        return 
    for i in range(len(pacientes)):
        for j in range(0, len(pacientes) -i -1):
            if pacientes[j][0] > pacientes[j+1][0]:
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]
    print(f"Inventario ordenado por precio de manera ascendente: ")
    for paciente in pacientes:
        print(f"Numero historia clinica: {paciente[0]}, nombre: {paciente[1]}, edad: {paciente[2]}, diagnostico: {paciente[3]}, dias de internacion: {paciente[4]}")
    return pacientes

def paciente_mas_dias_internacion(pacientes: list):
    if not pacientes:
        print("No hay pacientes almacenados.")
        return 
    paciente_mas_dias = pacientes[0]
    for paciente in pacientes: 
        if paciente[4] > paciente_mas_dias[4]:
            paciente_mas_dias = paciente
    print(f"El paciente con mas dias de internacion es: {paciente_mas_dias}")

def paciente_menos_dias_internacion(pacientes: list):
    if not pacientes:
        print("No hay pacientes almacenados.")
        return 
    paciente_menos_dias = pacientes[0]
    for paciente in pacientes: 
        if paciente[4] < paciente_menos_dias[4]:
            paciente_menos_dias = paciente
    print(f"El paciente con menos dias de internacion es: {paciente_menos_dias}")

def internacion_mayor_a_5 (pacientes: list):
    if not pacientes:
        print("No hay pacientes almacenados.")
        return
    contador_paciente = 0
    for paciente in pacientes:
        if paciente[4] > 5:
            contador_paciente += 1
            print(f"hay {contador_paciente} pacientes con internacion mayor a 5 dias.")
        else:
            return "No hay pacientes con menos de 5 dias de internacion"

def promedio_dias_internacion(pacientes: list):
    if not pacientes:
        print("No hay pacientes almacenados.")
        return
    total_dias_internacion = 0 
    for paciente in pacientes:
        total_dias_internacion += paciente[4]
    promedio = total_dias_internacion / len(pacientes)
    print(f'El promedio de los dias de internacion es: {promedio}')
