# Creamos un diccionario vacío para almacenar los datos de los equipos de red
equipos_de_red = {}

# Función para ingresar datos de un equipo de red
def ingresar_equipo():
    nombre_datacenter = input("Ingrese el nombre del Datacenter: ")
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    tipo_equipo = input("Ingrese el tipo de equipo: ")
    modelo_equipo = input("Ingrese el modelo del equipo: ")
    sala = input("Ingrese la sala: ")
    rack = input("Ingrese el rack: ")
    numero_u_rack = input("Ingrese el número de U del rack: ")
    ip_principal = input("Ingrese la IP principal: ")
    
    cantidad_interfaces = {}
    tipos_interfaces = ['ethernet','fibra']
    for tipo in tipos_interfaces:
        cantidad = int(input(f"Ingrese la cantidad de interfaces {tipo}: "))
        cantidad_interfaces[tipo] = cantidad
    
    # Creamos un diccionario con los datos ingresados
    equipo = {
        'Nombre Datacenter': nombre_datacenter,
        'Nombre Equipo': nombre_equipo,
        'Tipo Equipo': tipo_equipo,
        'Modelo Equipo': modelo_equipo,
        'Sala': sala,
        'Rack': rack,
        'Número de U del Rack': numero_u_rack,
        'IP Principal': ip_principal,
        'Cantidad de Interfaces': cantidad_interfaces
    }
    
    # Guardamos el equipo en el diccionario general
    equipos_de_red[nombre_equipo] = equipo

# Función para buscar un equipo por su nombre
def buscar_equipo(nombre):
    if nombre in equipos_de_red:
        print("Datos del equipo:")
        for key, value in equipos_de_red[nombre].items():
            print(f"{key}: {value}")
    else:
        print("El equipo no fue encontrado.")

# Menú de opciones
while True:
    print("\n1. Ingresar datos de un equipo de red")
    print("2. Buscar equipo por nombre")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        ingresar_equipo()
    elif opcion == '2':
        nombre_equipo = input("Ingrese el nombre del equipo que desea buscar: ")
        buscar_equipo(nombre_equipo)
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")