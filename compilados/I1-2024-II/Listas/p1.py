# Escribe tu código aquí

def contabilizar(lista):
    depositado=0
    retirado=0

    for operacion in lista:
        if operacion>0:
            depositado+=operacion
        else:
            retirado+=operacion

    return [depositado, retirado]
