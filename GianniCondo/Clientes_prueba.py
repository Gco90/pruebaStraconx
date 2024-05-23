
#Estructura principal que almacena los clientes
clientes = []

#Estructura que contiene el nemotecnico y descriocion de los paises
paises = {"EC": "Ecuador",
          "CO": "Colombia",
          "PE":"Peru"}

def AgregarCliente(clientes):
    print("Estoy en agregar cliente")

    #solicito los datos de nombre y cedula del cliente
    nombre = input("Ingrese el nombre del cliente:")
    cedula = input("Ingrese la cedula del cliente:")
    nemo_pais = input("Ingrese el Nemotecnico del pais:")

    #Almaceno los datos ingresados en una estructura temporal
    nuevo_cliente = {"nombre": nombre, "cedula": cedula, "nemo_pais":nemo_pais}

    #Agrego el nuevo cliente a la estructra principal de clientes
    clientes.append(nuevo_cliente)

    print(f"Cliente {nombre} agregado exitosamente" )

    

def EliminarCliente(clientes):
    #Validacion inicial de la estructura si no hay datos vuelvo al menu principal
    if not clientes:
        print("\n No hay clientes")
        return
    
    nombre_eliminar = input("Ingrese el nombre del cliente a Eliminar: ")

    #flag para controlar si encontro o no al cliente dentro de la estrcutura
    cliente_encontrado = False
    #Recorro la lista de clientes y valido si el nombre ingresado esta en la lista
    for i, cliente in enumerate(clientes):
        if cliente["nombre"] == nombre_eliminar:
            del clientes[i]
            cliente_encontrado = True
            print(f"Cliente: {nombre_eliminar} Eliminado con exito!")
            break

    if not cliente_encontrado:
        print(f"Cliente: {nombre_eliminar} No fue encontrado en la lista!")

def ListarCliente(clientes):
    if not clientes:
        print("\n No hay clientes")
        return
    
    #recorro la lista de clientes
    print("\n Listado de Clientes")
    for cliente in clientes: 
        print(f"Cliente: {cliente['nombre']} - Identificacion: {cliente['cedula']} - Nemotecnico: {cliente['nemo_pais']}")
    

def BuscarCliente(clientes):
    if not clientes:
        print("\n No hay clientes")
        return
    #Ingreso el nombre del cliente a buscar dentro de la estructura
    nombre_buscar = input("Ingrese el nombre del cliente a buscar:")
    #Flag para controlar si se econtro el cliente
    cliente_encontrado = False
    for  cliente in clientes:
        if cliente['nombre'] == nombre_buscar:           
            print(f"Cliente encontrado Identificacion: {cliente['cedula']}")
            cliente_encontrado = True
            #Si el cliente fu encontrado salgo del ciclo
            break
    
    #Si el cliente no fue encontrado presente un mensaje informativo
    if not cliente_encontrado: 
        print(f"Cliente: {nombre_buscar} No fue encontrado en la lista!")



def DeterminarPais(clientes, paises):
    if not clientes:
        print("\n No hay clientes")
        return
    
    #Ingreso la cedula a buscar del cliente
    cedula_buscar = input("Ingrese la cedula del cliente:")
    #Variabel temporal que almacena la informacion del cliente
    cliente = None
    #Recorro la lista de clientes
    for c in clientes:
        if c["cedula"] == cedula_buscar:
            cliente = c
            break
    
    if not cliente:
        print(f"Cliente con cedula:{cedula_buscar} No encontrado")
        return
    
    #Con la informacion obtenida del cliente accedo al nemotecnico ingresado
    codigo_pais = cliente['nemo_pais']

    #Obtengo la descripcion del pais en base al nemotecnico
    pais = paises.get(codigo_pais)

    if pais:
        print(f"El cliente: {cliente['nombre']} es del Pais {pais}")
    else:
        print("El codigo del pais no fue encontrado")



def menu_principal():
    #metodo de printea el menu principal de la aplicacion
    while True:
        print("\n Menu principal")
        print("1 Agregar Cliente")
        print("2 Eliminar Cliente")
        print("3 Listar Cliente")
        print("4 Buscar Cliente")
        print("5 Determinar pais de Cliente")
        print("6 Salir")

        #capturo la opcion correspondiente
        opcion = input("Ingrese la opcion deseada:")

        #Validacion de la opcion ingresada para llamar a la funcion especifica 

        if opcion == "1":
            AgregarCliente(clientes)
        elif opcion == "2" : 
            EliminarCliente(clientes)
        elif opcion == "3" : 
            ListarCliente(clientes)
        elif opcion == "4" :
            BuscarCliente(clientes)
        elif opcion == "5" :
            DeterminarPais(clientes,paises)
        elif opcion == "6" :
            print("Saliendo...")
            break
        else:
            print("Opcion invalida por favor intentelo nuevamente")



#Ejecutando el menu principal
menu_principal()










