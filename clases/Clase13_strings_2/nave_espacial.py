import nave


# def obtener_habitacion(nombre):
#     """Busca al ocupante por nombre y retorna la ubicación de la habitación."""
#     respuesta=""
#     for piso in range(nave.num_pisos()):
#
#
#         for habitacion in range(nave.num_habitaciones(piso)):
#             if nave.nombre_ocupante(piso, habitacion) == nombre:
#                 respuesta= "Piso: "+ str(piso)+ " Habitación: "+ str(habitacion)
#                 return respuesta
#
#
#
# respuesta_funcion=obtener_habitacion("Ingrid")
# print(respuesta_funcion)


def obtener_habitacion(nombre):
    """Busca al ocupante por nombre y retorna la ubicación de la habitación."""
    respuesta = ""
    for piso in range(nave.num_pisos()):
        if respuesta != "":
            break

        for habitacion in range(nave.num_habitaciones(piso)):
            if nave.nombre_ocupante(piso, habitacion) == nombre:
                respuesta = "Piso: " + str(piso) + " Habitación: " + str(habitacion)
                print(respuesta)
                break


obtener_habitacion("Ingrid")



