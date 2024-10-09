#Imagina que quieres realizar un viaje en auto
# desde tu ciudad hasta una ciudad vecina.
# Necesitas calcular el costo total del viaje,
# teniendo en cuenta varios factores como la distancia
# a recorrer, el consumo de combustible del auto,
# el precio del combustible, y si habrá costos adicionales como peajes.

#Entradas
distancia = int(input("Ingrese la distancia a recorrer: "))
consumo_litros_vehiculo = float(input("Ingresa el consumo de litros de tu vehículo: "))
precio_combustible = 1500
costo_peajes = 10000

#Solución
consumo_total = distancia * consumo_litros_vehiculo
costo_combustible = consumo_total * precio_combustible
costo_total = costo_combustible + costo_peajes

#Salida
print("El costo total del viaje es: ", costo_total, "CLP")