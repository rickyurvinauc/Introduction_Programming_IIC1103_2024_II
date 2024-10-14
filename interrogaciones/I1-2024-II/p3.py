# Escribe tu código aquí
import hotel

def obtener_habitacion(nombre):
    for n_habitacion in range(hotel.num_habitaciones()):
        if nombre==(hotel.nombre_ocupante(n_habitacion)):
            return n_habitacion
    return -1
