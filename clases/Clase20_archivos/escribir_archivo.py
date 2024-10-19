# Usando el método write() para escribir en un archivo
archivo = open('ejemplo.txt', 'w')
archivo.write('Hola, mundo!')
archivo.close()

# Usando writelines() para escribir en un archivo
archivo = open('ejemplo.txt', 'w')
lineas = ['Primera línea\n', 'Segunda línea\n', 'Tercera línea\n']
archivo.writelines(lineas)
archivo.close()

# Usando print() para escribir en un archivo
archivo = open('ejemplo.txt', 'a')
print('Hola, mundo!', file=archivo)
archivo.close()