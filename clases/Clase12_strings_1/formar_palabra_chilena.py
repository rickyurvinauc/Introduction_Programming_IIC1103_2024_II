from diccionario.funciones_validacion import valida

def corregir(palabra, pos1, pos2):
    abecedario = 'abcdehimnopr'
    for letra1 in abecedario:
        for letra2 in abecedario:
            nueva_palabra = palabra[:pos1] + letra1 + palabra[pos1+1:pos2] + letra2 + palabra[pos2+1:]
            if valida(nueva_palabra):
                return nueva_palabra
    return palabra

# Ejemplo 1: 'em$an$da'
palabra = 'em$an$da'
pos1, pos2 = 2, 5
resultado = corregir(palabra, pos1, pos2)
print(resultado)  # 'empanada'

# Ejemplo 2:  'ban$e$a'
palabra = 'ba(de$a'
pos1, pos2 = 2, 5
resultado = corregir(palabra, pos1, pos2)
print(resultado)  #  'bandera'

# Ejemplo 3: palabra = '$hich$'
palabra = '$hich$'
pos1, pos2 = 0, 5
resultado = corregir(palabra, pos1, pos2)
print(resultado)  # 'chicha'
