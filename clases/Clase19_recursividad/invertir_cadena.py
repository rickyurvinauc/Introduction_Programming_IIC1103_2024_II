def invertir_cadena(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])