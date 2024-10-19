nombre_archivo = input('Ingrese el nombre del archivo: ')
manejador_archivo = open(nombre_archivo, 'r')
lista = manejador_archivo.readlines()
print(len(lista))