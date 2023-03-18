idCuenta = 0
cuentas = []
idCuenta = 0
i = 0

while i <= 10:
    if (i != 10):
        idCuenta += 1
        saldo = {}

        saldo["idCuenta"] = idCuenta
        saldo["numeroCuenta"] = int(
            input(f"Digita el numero de la cuenta para {saldo['idCuenta']}: "))
        saldo["saldos"] = float(
            input(f"Digita el saldo de la cuenta {saldo['numeroCuenta']}: "))
        
        cuentas.append(saldo)

        print(f"cuenta {saldo['idCuenta']} registrada ")

        i += 1

    elif(i >= 10 and len(cuentas) == 10):
        for cuenta in reversed(cuentas):
            print(f"IdCuenta: {cuenta['idCuenta']}")
            print(f"Numero cuenta: {cuenta['numeroCuenta']}")
            print(f"Saldo: {cuenta['saldos']}")
            print("*****")
        break
