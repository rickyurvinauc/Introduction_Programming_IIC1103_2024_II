#Escriba un programa para que un estudiante decida cómo ir desde su 
# casa en Ñuñoa hasta la Universidad de Chile en el centro. Tiene tres 
# opciones: ir en Metro, en bicicleta o en micro (bus).
#Condiciones:
#Si está lloviendo, el estudiante preferirá ir en Metro.
#Si no está lloviendo y hay congestión vehicular en la Avenida Grecia,
# preferirá ir en bicicleta para evitar el tráfico.
#Si no está lloviendo y no hay congestión vehicular, pero la calidad 
#del aire es regular o mala, preferirá ir en Metro.
#Si ninguna de las condiciones anteriores se cumple, tomará la micro.

lluvia = True
congestion_vehicular = False
calidad_aire= input("Ingrese la calidad del aire (piede ser buena, regular o mala)")

if lluvia:
    transporte = "Metro"
elif not lluvia and congestion_vehicular:
    transporte = "Bicicleta"
elif not lluvia and not congestion_vehicular and (calidad_aire == "regular" or calidad_aire == "mala"):
    transporte = "Metro"
else:
    transporte = "Micro"

print("El estudiante decide ir en", transporte)
