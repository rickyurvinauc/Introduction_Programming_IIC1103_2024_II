# Un organizador de eventos en Santiago de Chile debe decidir si realizar un evento al aire libre en el Parque Bicentenario, en un salón cerrado, o cancelar el evento. La decisión depende de múltiples factores como el clima, la disponibilidad del salón, el número de asistentes confirmados, y el presupuesto disponible.
# Condiciones:
# Si el clima es soleado:
# Si hay más de 100 asistentes confirmados y el presupuesto es mayor a $2,000,000 CLP, el evento se realizará al aire libre en el Parque Bicentenario.
# Si el número de asistentes confirmados es menor o igual a 100, el evento se realizará al aire libre, pero en una sección más pequeña del parque.
# Si el presupuesto es menor a $2,000,000 CLP, se evaluará la disponibilidad del salón.
# Si el clima es nublado:
# Si el presupuesto es mayor o igual a $2,000,000 CLP y el salón está disponible, se realizará el evento en el salón cerrado.
# Si el presupuesto es menor a $2,000,000 CLP pero el salón está disponible, se realizará en el salón, pero se reducirán algunos servicios.
# Si el salón no está disponible, se considerará realizar el evento al aire libre solo si hay menos de 50 asistentes confirmados y si no llueve.
# Si llueve:
# Si el salón está disponible, se realizará el evento en el salón.
# Si el salón no está disponible, el evento se cancelará.
# Solicitar entradas al usuario
clima = input("Ingrese el clima (soleado, nublado, lluvioso): ")
asistentes_confirmados = int(input("Ingrese el número de asistentes confirmados: "))
presupuesto = int(input("Ingrese el presupuesto disponible en CLP: "))
salon_disponible = input("¿Está disponible el salón? (si/no): ") == "si"

if clima == "soleado":
    if asistentes_confirmados > 100 and presupuesto > 2000000:
        lugar_evento = "Parque Bicentenario (Sección Principal)"
    elif asistentes_confirmados <= 100:
        lugar_evento = "Parque Bicentenario (Sección Pequeña)"
    else:
        if salon_disponible:
            lugar_evento = "Salón Cerrado"
        else:
            lugar_evento = "Evento Cancelado"
elif clima == "nublado":
    if presupuesto >= 2000000:
        if salon_disponible:
            lugar_evento = "Salón Cerrado"
        else:
            lugar_evento = "Parque Bicentenario (si no llueve y menos de 50 asistentes)"
    else:
        if salon_disponible:
            lugar_evento = "Salón Cerrado con servicios reducidos"
        elif asistentes_confirmados < 50:
            lugar_evento = "Parque Bicentenario (si no llueve)"
        else:
            lugar_evento = "Evento Cancelado"
elif clima == "lluvioso":
    if salon_disponible:
        lugar_evento = "Salón Cerrado"
    else:
        lugar_evento = "Evento Cancelado"
else:
    lugar_evento = "Evento Cancelado"

print("El evento se realizará en: " + lugar_evento)
