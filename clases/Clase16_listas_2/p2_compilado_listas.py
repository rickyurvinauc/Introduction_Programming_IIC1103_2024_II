def dcc_banco(saldo_i, transaciones):
    print("Saldo inicial", saldo_i)
    pendientes = []

    for operacion in transaciones:
        if operacion > 0:
            saldo_i += operacion
            print("Deposito", operacion, "- Saldo", saldo_i)

        else:
            operacion = operacion * -1
            if operacion > saldo_i:
                print("Retiro fallido", operacion, "- Saldo", saldo_i)
                pendientes.append(operacion * -1)
                continue
            saldo_i -= operacion
            print("Retiro", operacion, "- Saldo", saldo_i)

    while sum(pendientes) < 0:
        transaciones = pendientes.copy()
        for operacion in transaciones:
            operacion = operacion * -1
            if operacion > saldo_i:
                print("Retiro fallido", operacion * -1, "- Saldo", saldo_i)
            else:
                saldo_i -= operacion
                pendientes.pop(0)
                print("Retiro", operacion, "- Saldo", saldo_i)



