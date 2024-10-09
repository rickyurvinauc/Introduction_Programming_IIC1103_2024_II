# Suponga que por parte de la coordinación del curso IIC1103
# se le ha solicitado que escriba un programa para determinar
# el número de estudiantes que tienen un apellido que empiece
# por cada una de las vocales. Además, se debe ser cuántos/as
# no empiezan por vocales (empiezan por consonantes).
# Suponga que el nombre de cada estudiante esta ordenado de la
# siguiente forma “APELLIDO_PATERNO APELLIDO_MATERNO PRIMER_NOMBRE”. Todo el nombre esta en mayusuclas.
# Asimismo, entre cada apellido y el nombre existe un espacio en blanco.
# A usted se le entrega una lista con los nombres de los estudiantes.
# Al final del programa usted deberá imprimir cuántos/as estudiantes
# hay por cada vocal y por consonantes. Por ejemplo:
# En el urso IIC1103 existen 30 estudiantes que su primer apellido empieza por la vocal a.
# En el curso IIC1103 existen 45 estudiantes que su apellido empieza por la vocal e.

# Conocer variables que vamos a usar!
lista_estudiantes = ["URVINA CORDOVA RICARDO", "MEDINA PUETATE INGRID",
                      "AGUILAR VELIS BENJAMIN", "OVALLE VALDES MARIANA"]

vocales = ["A", "E", "I", "O", "U", "CONSTANTE"]

cont_primer_apellido_a = 0
cont_primer_apellido_e = 0
cont_primer_apellido_i = 0
cont_primer_apellido_o = 0
cont_primer_apellido_u = 0
cont_primer_apellido_consonante = 0

cont_segundo_apellido_a = 0
cont_segundo_apellido_e = 0
cont_segundo_apellido_i = 0
cont_segundo_apellido_o = 0
cont_segundo_apellido_u = 0
cont_segundo_apellido_consonante = 0

for nombre in lista_estudiantes:
    primera_letra_apellido = nombre[0]
    if primera_letra_apellido == vocales[0]:
        cont_primer_apellido_a += 1
    elif primera_letra_apellido == vocales[1]:
        cont_primer_apellido_e += 1
    elif primera_letra_apellido == vocales[2]:
        cont_primer_apellido_i += 1
    elif primera_letra_apellido == vocales[3]:
        cont_primer_apellido_o += 1
    elif primera_letra_apellido == vocales[4]:
        cont_primer_apellido_u += 1
    else:
        cont_primer_apellido_consonante += 1

    posicion_espacio_blanco = 0
    for letra in nombre:
        if letra == " ":
            primera_letra_segundo_apellido = nombre[posicion_espacio_blanco+1]
            if primera_letra_segundo_apellido == "A":
                cont_segundo_apellido_a += 1
                break
            elif primera_letra_segundo_apellido == "E":
                cont_segundo_apellido_e += 1
                break
            elif primera_letra_segundo_apellido == "I":
                cont_segundo_apellido_i += 1
                break
            elif primera_letra_segundo_apellido == "O":
                cont_segundo_apellido_o += 1
                break
            elif primera_letra_segundo_apellido == "U":
                cont_segundo_apellido_u += 1
                break
            else:
                cont_segundo_apellido_consonante += 1
                break
        posicion_espacio_blanco += 1

resp_primer_apellido = [cont_primer_apellido_a,
                        cont_primer_apellido_e,
                        cont_primer_apellido_i,
                        cont_primer_apellido_o,
                        cont_primer_apellido_u,
                        cont_primer_apellido_consonante
                        ]

cont = 0
for i in resp_primer_apellido:
    print("En el curso IIC1103 existen", i,
          "estudiantes que su primer apellido empieza por", vocales[cont])
    cont += 1

resp_segundo_apellido = [cont_segundo_apellido_a,
                         cont_segundo_apellido_e,
                         cont_segundo_apellido_i,
                         cont_segundo_apellido_o,
                         cont_segundo_apellido_u,
                         cont_segundo_apellido_consonante
                         ]
print("\n --------------------------------------------- \n")

cont = 0
for i in resp_segundo_apellido:
    print("En el curso IIC1103 existen", i,
          "estudiantes que su segundo apellido empieza por", vocales[cont])
    cont+=1