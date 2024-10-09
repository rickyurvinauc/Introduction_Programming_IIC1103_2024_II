#Escriba un programa que pida los coeficientes de una ecuación de segundo grado 
# (a x² + b x + c = 0) y escriba la solución.
#Se recuerda que una ecuación de segundo grado puede no tener solución, 
# tener una solución única, tener dos soluciones o que todos los números sean solución. 
# Si todos los factores son cero, todos los numeros son solucion, 
# por otra parte, si a y b son cero no tiene solucion
# si a es cero hay una unica solucion
# si el discriminante es mayor de cero tiene dos soluciones
# si el discriminante es cero tiene una solucion, si no se cumple ninguna condicion no tiene solucion
# el discriminante se calcula b**2 - 4*a*c
import math

a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))
c = float(input("Escriba el valor del coeficiente c: "))

discriminante = b**2 - 4*a*c

if a == 0 and b == 0 and c == 0:
    print("Todos los números son solución")
elif a == 0 and b == 0:
    print("Sin solución")
elif a == 0:
    solucion_unica = -c / b
    print("Una solución:", solucion_unica)
elif discriminante > 0:
    solucion1 = (-b + math.sqrt(discriminante)) / (2*a)
    solucion2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("La ecuación tiene dos soluciones:", solucion1, " y ", solucion2)
elif discriminante == 0:
    solucion_unica = -b / (2*a)
    print("Una solución:", solucion_unica)
else:
    print("Sin solución real")