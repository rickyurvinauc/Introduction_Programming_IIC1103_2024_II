# Escribe tu código aquí
from hotel import num_habitaciones, nombre_ocupante


def revisar_asignacion():
    # cuantos cuidadores tienen mas de un perro
    contador = 0

    for n_habitacion in range(num_habitaciones()):
        perro = nombre_ocupante(n_habitacion)
        for n_habitacion_2 in range(n_habitacion, num_habitaciones()):
            perro2 = nombre_ocupante(n_habitacion_2)
            if perro == perro2 and n_habitacion != n_habitacion_2:
                contador += 1
                break

    return contador

