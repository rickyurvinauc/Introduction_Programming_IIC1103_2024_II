# Escribe tu código aquí

def abiertos_tour(p):
    num_cajones=1
    cajon=p[0]

    while cajon!=0:
        cajon=p[cajon]
        num_cajones+=1

    return num_cajones