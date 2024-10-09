from funcionesclinica import *

pacientes = []
salir = ''
while salir != 'salir':
    menu_principal()
    opcion = input("Elija una opcion (1,2,3,4,5,6,7,8,9): ")

    if opcion == '1': 
        cargar_pacientes(pacientes)
    elif opcion == '2':
        mostrar_lista_pacientes(pacientes)
    elif opcion == '3':
        historia_clinico = int(input("Ingrese el numero de historia clinica del paciente: "))
        paciente = buscar_paciente(pacientes, historia_clinico)
        if paciente:
            print(paciente)
        else: 
            print("paciente no encontrado")
    elif opcion == '4':
        ordenar_pacientes(pacientes)
    elif opcion == '5':
        paciente_mas_dias_internacion(pacientes)
    elif opcion == '6':
        paciente_menos_dias_internacion(pacientes)
    elif opcion == '7':
        internacion_mayor_a_5(pacientes)
    elif opcion == '8':
        promedio_dias_internacion(pacientes)
    elif opcion == '9':
        salir = 'salir'
    else: 
        print("Opcion invalida, por favor ingrese (1,2,3,4,5,6,7,8,9): ")