option = 1
idCuenta = 0
cuentas = []
saldo = {
    "saldo1": 1000,
    "saldo2": 2000,
    "saldo3": 3000,
    "saldo4": 4000,
    "saldo5": 5000,
    "saldo6": 6000,
    "saldo7": 7000,
    "saldo8": 8000,
    "saldo9": 9000,
    "saldo10": 10000,
}

while True:
    print("******Cuentas Cersei*******")
    print("******Opción 1. = **********Ingrese una cuenta*********")

    option = int(input("Escoga opción: "))

    if (option == 1):

        idCuenta += 1

        cuentas = {}

        cuentas["id"] = idCuenta
