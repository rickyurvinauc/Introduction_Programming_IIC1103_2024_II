# Pregunta
# Llaves - B
#
# Actualizar
# Plantilla de pregunta
# Llaves - B (I1 2023-2) 🌶️🌶️
# Lenguaje de programación
# Python
# Descripción
# Objetivo
#
# Deberás escribir la función son_llave que recibe 2 strings como parámetros, p y q, donde la función deberá retornar un booleano True si p y q son llave, o False si no lo son.
#
# Considera dos strings p y q de la misma longitud compuestos por vocales en mayúscula y minúscula. Decimos que p y q son "llave" si las posiciones de las mayúsculas y las minúsculas en p coinciden con las posiciones de las mayúsculas y minúsculas en q, sin importar qué vocales son.
#
# Screen-Shot-2023-06-30-at-22-09-15.png
#
# Input Format
#
# Los llamados a inputs serán manejados por nosotros, por lo que no debes preocuparte de recibir inputs. Solo deberás encargarte de definir la función son_llave.
#
# Output Format
#
# El output también es manejado por nosotros.
#
# Ejemplo
#
# Input
# 3
# print(son_llave("aaIoUaaEUei", "ueOaAeiIUae"))
# print(son_llave("AeiOu", "uOeiA"))
# print(son_llave("aaaAa", "eeeEe"))
#
# Output
# True
# False
# True
#
# Explicación: El primer input nos muestra cuántas veces se va a llamar la función son_llave. La primera llamada y la última se tienen strings que son llaves, ya que las posiciones de vocales que son mayúsculas coinciden (y lo mismo para sus minúsculas). En cuanto a la segunda llamada, los strings "AeiOu" y "uOeiA" no son llave debido a que sus primeras letras, A y u, no son del mismo tipo (ambas mayúsculas o ambas minúsculas). También ocurre con las letras en la segunda posición (e y O), penúltima posición (O e i) y la última posición (u y A).
def son_llave(p, q):
    indice=0
    for letra in p:
        if letra.islower() and q[indice].islower():
            indice+=1
        elif letra.isupper() and q[indice].isupper():
            indice+=1
        else:
            return False

    return True