# Escribe tu código aquí
import hotel

n_buses_inicial = hotel.cantidad_buses()


def se_puede_excursion(n_buses_inicial):
    n_buses = n_buses_inicial
    capacidad_max = 5
    num_hab = hotel.num_habitaciones()
    perros_timidos = 0
    perros_extrovertidos = 0

    for h in range(num_hab):
        perro = hotel.nombre_ocupante(h)
        caracter = hotel.obtener_caracter(perro)
        if caracter == "timido":
            perros_timidos += 1
        else:
            perros_extrovertidos += 1

    bus_lleno = 0
    while perros_timidos != 0 and n_buses > 0:
        perros_timidos -= 1
        capacidad_max -= 1
        if capacidad_max == 0 or perros_timidos == 0:
            n_buses -= 1
            capacidad_max = 5
            bus_lleno += 1

    while perros_extrovertidos != 0 and n_buses > 0:
        perros_extrovertidos -= 1
        capacidad_max -= 1
        if capacidad_max == 0 or perros_extrovertidos == 0:
            n_buses -= 1
            capacidad_max = 5
            bus_lleno += 1

    if perros_extrovertidos > 0 or perros_timidos > 0:
        capacidad_max = 5
        while perros_timidos != 0:
            perros_timidos -= 1
            capacidad_max -= 1
            if capacidad_max == 0 or perros_timidos == 0:
                capacidad_max = 5
                bus_lleno += 1
        capacidad_max = 5
        while perros_extrovertidos != 0:
            perros_extrovertidos -= 1
            capacidad_max -= 1
            if capacidad_max == 0 or perros_extrovertidos == 0:
                capacidad_max = 5
                bus_lleno += 1

        print("Insuficientes: se tienen " + str(n_buses_inicial) + " y se necesitan " + str(bus_lleno))
    else:
        print("Suficientes: se tienen " + str(n_buses_inicial) + " y se necesitan " + str(bus_lleno))

