habitaciones_nave = [
    ["Ricardo", "Ingrid", None],       # Piso 0
    [None, "Menthor", "Mayra"],   # Piso 1
    ["Liliana", None, "Pedro"],       # Piso 2
]

def num_pisos():
    """Retorna el número de pisos de la nave."""
    return len(habitaciones_nave)

def num_habitaciones(piso):
    """Retorna el número de habitaciones en un piso específico."""
    if 0 <= piso < num_pisos():
        return len(habitaciones_nave[piso])
    else:
        return 0  # Si el piso no es válido

def nombre_ocupante(piso, habitacion):
    """Retorna el nombre del ocupante en una habitación específica."""
    if 0 <= piso < num_pisos() and 0 <= habitacion < num_habitaciones(piso):
        ocupante = habitaciones_nave[piso][habitacion]
        return ocupante if ocupante is not None else "Vacío"
    else:
        return "Vacío"  # Si la habitación o piso no existen
