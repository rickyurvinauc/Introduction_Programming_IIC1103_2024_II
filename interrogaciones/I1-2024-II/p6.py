# Escribe tu código aquí
from diccionario import valida


def corregir(palabra, posicion):
    vocales = "aeiou"

    for vocal in vocales:
        cont = 0
        nueva_palabra = ""
        for caracter in palabra:
            if cont == posicion:
                nueva_palabra += vocal
                cont += 1
                continue
            nueva_palabra += caracter
            cont += 1

        if valida(nueva_palabra):
            return nueva_palabra

    return palabra
