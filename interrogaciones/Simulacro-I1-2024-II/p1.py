# Llaves - A
#
# Actualizar
# Plantilla de pregunta
# Llaves - A (I1 2023-2) 🌶️
# Lenguaje de programación
# Python
# Descripción
# Objetivo
#
# Escribe un programa que cuente las letras minúsculas en una palabra de vocales.
#
# Input Format
#
# Un string correspondiente a la palabra, con letras mayúsculas y minúsculas.
#
# Output Format
#
# Un int que indique la cantidad de letras minúsculas en la palabra.
#
# Ejemplo
#
# Input
# IEaiAIO
#
# Output
# 2
#
# Explicación: hay 2 vocales minúsculas, "a" e "i".
palabra=input()
contador=0
for letra in palabra:
    if letra.islower():
        contador+=1

print(contador)