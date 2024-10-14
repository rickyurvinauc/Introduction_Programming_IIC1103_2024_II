# Descripción
# Objetivo
#
# Considera dos strings p y q donde p tiene una longitud mayor o igual a la de q y ambos están compuestos por vocales en mayúscula y minúscula. Decimos que p y q son "casi-llave" si existe un trozo de string p2, dentro de p, donde p2 y q son llave. Por ejemplo, si p es "aeiou", entonces p2 (un trozo de p) puede ser "aei", "io", "u", "eio", etc. Ojo; en este caso p2 no puede ser “aiu” (no se pueden saltar ni reordenar letras).
#
# Screen-Shot-2023-06-30-at-07-39-46.png
#
# Deberás escribir la función casi_llave que recibe como parámetros dos strings, p y q, y retorna un booleano indicando si es que p y q son casi-llave.
#
# Si lo consideras necesario, puedes importar el módulo llaves y usar la función son_llave(a,b) que retorna un bool indicando si a y b son llave o no.
#
# Recordatorio: Decimos que p y q son "llave" si las posiciones de las mayúsculas y las minúsculas en p coinciden con las posiciones de las mayúsculas y minúsculas en q, sin importar qué vocales son.
#
# Input Format
#
# Los llamados a inputs serán manejados por nosotros, por lo que no debes preocuparte de recibirlos. Solo deberás encargarte de definir la función casi_llave.
#
# Output Format
#
# Los output también serán manejados por nosotros.
#
# Ejemplo
#
# Input
# 2
# print(casi_llave("aoIoUaeEUe", "OaAeiI"))
# print(casi_llave("AeiOu", "OeO"))
#
# Output
# True
# False
#
# Explicación
# El primer int nos dice que habrá dos llamadas a la función casi_llave. Los primeros strings son casi-llave ya que un trozo del primer string puede ser "IoUaeE", el cual tiene mayúsculas y minúsculas en las mismas posiciones que el segundo string "OaEeiI". Para los siguientes 2 strings, estos no son casi-llave debido a que no existe un trozo de string de "AeiOu" que pueda ser llave con "OeO".

from llaves import son_llave

def casi_llave(p, q):
    lon_q=len(q)
    indice=0
    while True:
        if indice>=len(p):
            return False
        p2=p[indice:lon_q+indice]
        indice+=1
        if son_llave(p2, q):
            return True