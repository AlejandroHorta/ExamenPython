option = 1
idCiclista = 0
ciclistas = []

while True:
    print("******Ciclistas*******")
    print("******Opción 1. = Ingrese un Ciclista*********")
    print("******Opción 2. = Mostrar todos los Ciclistas ingresados*********")
    print("******Opción 3. = Buscar ciclista por codigo*********")
    print("******Opción 4. = Editar tiempo ciclista*********")
    print("******Opción 5. = Eliminar un ciclista*******")

    option = int(input("Escoga opción: "))

    if (option == 1):

        idCiclista += 1

        ciclista = {}

        ciclista["id"] = idCiclista
        ciclista["codigo"] = int(input("Digita el codigo del ciclista:"))
        ciclista["nombre"] = input("Digita el nombre del ciclista:")
        ciclista["edad"] = int(input("Digita la edad del ciclista:"))
        ciclista["equipo"] = (input("Digite el equipo del ciclista:"))
        ciclista["tiempo"] = float(input("Digita el tiempo del ciclista:"))

        ciclistas.append(ciclista)
        print("ciclista registrado...")

    elif (option == 2):
        for ciclista in ciclistas:
            print(ciclista)
    elif (option == 3):
        ciclistaBuscar = int(input("Digite el codigo del ciclista a buscar:"))
        for ciclista in ciclistas:
            if (ciclista["codigo"] != ciclistaBuscar):
                print("No existe el ciclista")
                break
            print(f"ciclista encontrada {ciclista}")
    elif (option == 4):
        ciclistaBuscar = int(input("Ingrese el codigo del ciclista a buscar:"))
        for ciclista in ciclistas:
            if (ciclista["codigo"] != ciclistaBuscar):
                print("sin ciclistas")
                break
            print(f"el tiempo del actual ciclista es: {ciclista['tiempo']}")
            print(ciclista["tiempo"])
            ciclistaNuevo = float(input("Digita el nuevo tiempo ciclista: "))
            ciclista["tiempo"] = ciclistaNuevo
    elif (option == 5):
        codigo = int(input("Digite el codigo del ciclista a eliminar: "))
        for ciclista in ciclistas:
            if (ciclista["codigo"] == codigo):
                ciclistas.remove(ciclista)
    elif (option == 0):
        break
    else:
        print("Opción no valida")
