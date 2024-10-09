# Escribe tu código aquí

def solo_dcc(lista):
    iterador=0
    for letra in lista:
        if letra!="d" and letra!="c":
            lista[iterador]="-"
        iterador+=1
    
    return lista

