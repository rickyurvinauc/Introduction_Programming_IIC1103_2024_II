lista_estudiantes = [
    "URRUTIA SOTO ANDRES",
    "ESTRADA DIAZ CAMILA",
    "AGUILAR MUÑOZ JAVIER",
    "OLIVARES FERNANDEZ VALENTINA",
    "INOSTROZA RIVERA BENJAMIN",
    "HERNANDEZ ARAVENA ISABEL",
    "ANDRADE RAMIREZ MARTIN",
    "URIBE GONZALEZ CLAUDIA",
    "ESCOBAR HERNANDEZ JUAN",
    "OSORIO SANCHEZ CONSTANZA",
    "ALVAREZ LOPEZ CARLOS",
    "RODRIGUEZ IGLESIAS LORENA",
    "MUÑOZ PEREZ FRANCISCO",
    "SOTO ESCOBAR JAVIERA",
    "GONZALEZ MARTINEZ TOMAS",
    "DIAZ TORRES DANIELA",
    "PEREZ LOPEZ MATIAS",
    "FERNANDEZ ARAYA ANTONIA",
    "ORTEGA GONZALEZ PATRICIO",
    "RODRIGUEZ RAMIREZ MARIA",
    "MUÑOZ ALVAREZ SEBASTIAN",
    "SANCHEZ DIAZ JOSEFA",
    "OROZCO TORRES NICOLAS",
    "ARAYA SOTO ALEJANDRA",
    "MARTINEZ ESCOBAR GABRIEL",
    "DIAZ FERNANDEZ VALERIA",
    "PEREZ MARTINEZ IGNACIO",
    "ARAVENA GONZALEZ CAROLINA",
    "MARTINEZ RIVERA VICENTE",
    "RODRIGUEZ OVALLE PAULA",
    "IRARRAZAVAL DIAZ LUCAS",
    "SOTO HERNANDEZ CATALINA",
    "GONZALEZ PEREZ JUAN PABLO",
    "DIAZ FERNANDEZ MARTINA",
    "AGUIRRE LOPEZ AGUSTIN",
    "FERNANDEZ TORRES SOFIA",
    "MARTINEZ OLAVARRIA ANDREA",
    "OLGUIN MUÑOZ ALEJANDRO",
    "MUÑOZ DIAZ JAVIER",
    "SANCHEZ IRIBARREN AMPARO",
    "LOPEZ TORRES JOSE",
    "HERNANDEZ MARTINEZ ISIDORA",
    "MARTINEZ GONZALEZ LUCIA",
    "IRARRAZAVAL RIVERA CRISTIAN",
    "ESCUDERO TORRES DOMINIQUE",
    "FERNANDEZ LOPEZ VICTORIA",
    "MARTINEZ DIAZ PABLO",
    "OSORIO HERNANDEZ SOLEDAD",
    "MUÑOZ GONZALEZ RAUL",
    "SOTO RIVERA BENJAMIN",
    "AGUIRRE DIAZ CARLA",
    "ORTEGA TORRES PEDRO",
    "PEREZ HERNANDEZ CONSTANZA",
    "FERNANDEZ MARTINEZ EDUARDO",
    "ANDRADE LOPEZ FRANCISCA",
    "RODRIGUEZ PEREZ FELIPE",
    "MUÑOZ DIAZ MARCELA",
    "SANCHEZ FERNANDEZ ALBERTO",
    "LOPEZ SOTO NATALIA",
    "HERNANDEZ GONZALEZ TOMAS",
    "OSORIO TORRES MARIA JOSE",
    "DIAZ MUÑOZ LUIS",
    "PEREZ RAMIREZ MONICA",
    "IRARRAZAVAL DIAZ MAURICIO",
    "MARTINEZ PEREZ TERESA",
    "RODRIGUEZ LOPEZ CAMILO",
    "MUÑOZ FERNANDEZ ANDRES",
    "SOTO DIAZ PATRICIA",
    "GONZALEZ TORRES JORGE",
    "DIAZ HERNANDEZ JAVIERA",
    "PEREZ MARTINEZ ANDREA",
    "ARAYA RIVERA FERNANDO",
    "MARTINEZ DIAZ MARIANA",
    "ORTEGA TORRES CRISTINA",
    "MUÑOZ LOPEZ DANIEL",
    "SANCHEZ FERNANDEZ JAVIERA",
    "LOPEZ DIAZ RICARDO",
    "HERNANDEZ PEREZ CAROLINA",
    "MARTINEZ GONZALEZ CLAUDIO",
    "DIAZ RAMIREZ ELENA",
    "PEREZ LOPEZ VICTOR",
    "ESCUDERO TORRES PAULINA",
    "MARTINEZ DIAZ SEBASTIAN",
    "RODRIGUEZ PEREZ PATRICIA",
    "MUÑOZ FERNANDEZ JUAN",
    "SOTO LOPEZ SOFIA",
    "URRUTIA DIAZ TOMAS",
    "DIAZ SANCHEZ VERONICA",
    "PEREZ TORRES LORETO",
    "FERNANDEZ LOPEZ FRANCISCO",
    "MARTINEZ DIAZ CLAUDIA",
    "RODRIGUEZ PEREZ ALEJANDRO",
    "MUÑOZ GONZALEZ ROSA",
    "SANCHEZ HERNANDEZ JOSE",
    "LOPEZ MARTINEZ NELSON",
    "HERNANDEZ DIAZ AMALIA",
    "MARTINEZ ORELLANA MARCOS",
    "DIAZ TORRES VIVIANA",
    "PEREZ HERNANDEZ FABIOLA",
    "FERNANDEZ GONZALEZ ENRIQUE",
    "MARTINEZ PEREZ LAURA",
    "RODRIGUEZ SOTO JAVIER",
    "MUÑOZ DIAZ ALEJANDRO",
    "SANCHEZ FERNANDEZ FRANCISCA",
    "ORELLANA RAMIREZ HUGO",
    "HERNANDEZ GONZALEZ GABRIEL",
    "MARTINEZ TORRES JUANITA",
    "DIAZ LOPEZ LUCIA",
    "PEREZ MARTINEZ NICOLAS",
    "FERNANDEZ GONZALEZ MANUEL",
    "MARTINEZ DIAZ VICTORIA",
    "OLIVARES HERNANDEZ CRISTOBAL",
    "MUÑOZ RIVERA ANGELICA",
    "SOTO PEREZ ALFREDO",
    "GONZALEZ LOPEZ ESTEBAN",
    "DIAZ TORRES FRANCISCO",
    "PEREZ FERNANDEZ ALVARO",
    "IRIBARREN MARTINEZ ELISA",
    "MARTINEZ DIAZ ROBERTO",
    "RODRIGUEZ PEREZ CAMILA",
    "MUÑOZ GONZALEZ SEBASTIAN",
    "SANCHEZ LOPEZ LAURA",
    "LOPEZ DIAZ FELIPE",
    "HERNANDEZ PEREZ MARTINA",
    "MARTINEZ FERNANDEZ MIGUEL",
    "DIAZ RIVERA CATALINA",
    "PEREZ TORRES RODRIGO",
    "FERNANDEZ LOPEZ ANGELA",
    "MARTINEZ GONZALEZ HECTOR",
    "RODRIGUEZ DIAZ FABIOLA",
    "MUÑOZ LOPEZ JAIME",
    "SOTO MARTINEZ FRANCISCO",
    "URRUTIA RAMIREZ MARGARITA",
    "DIAZ HERNANDEZ PATRICIO",
    "PEREZ SOTO SOLEDAD",
    "FERNANDEZ GONZALEZ CRISTINA",
    "MARTINEZ LOPEZ PABLO"
]


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

espacio_blanco=" "


for nombre in lista_estudiantes: # recorro cada nombre en la lista de estudiantes
    pos_espacio_blanco=0 # inicio una variable para saber la posicion de cada caracter en el nombre
    pos_primer_espacio_blanco=0
    
    for caracter in nombre: # recorro cada caracter del nombre
        if ((caracter==espacio_blanco) and (pos_primer_espacio_blanco==0)): # si el caracter encontrado en el nombre es el espacio en blanco
            #para que entre en este if primero valido que el caracter sea espacio en blanco, y ademas verifico que sea el primer espacio en blanco que encuentra
            # como se la posicion del primer espacio en blanco, entonces la ultima letra del primer apellido es esa posicion menos 1
            ultima_letra_apellido_1=nombre[pos_espacio_blanco-1] 
            # aumento el contador dependiendo que vocal es, o si es una consonante
            pos_primer_espacio_blanco=pos_espacio_blanco
            if ultima_letra_apellido_1 == vocales[0]:
                cont_primer_apellido_a += 1
                continue
            elif ultima_letra_apellido_1 == vocales[1]:
                cont_primer_apellido_e += 1
                continue
            elif ultima_letra_apellido_1 == vocales[2]:
                cont_primer_apellido_i += 1
                continue
            elif ultima_letra_apellido_1 == vocales[3]:
                cont_primer_apellido_o += 1
                continue
            elif ultima_letra_apellido_1 == vocales[4]:
                cont_primer_apellido_u += 1
                continue
            else:
                cont_primer_apellido_consonante += 1
            
        pos_espacio_blanco+=1 # sumo en uno la posicion, esta posicion es la que me permite saber donde se encuentra cada caracter del nombre
        
        ### Hasta aqui he encontrado y contado cuantas veces aparece cada vocal en la ultima letra del primer apellido
        ### Necesito ahora encontrar el segundo espacio en blanco
        if caracter==espacio_blanco: # Encuentro el seegundo espacio en blanco
            ultima_letra_segundo_apellido = nombre[pos_espacio_blanco-1]
            if ultima_letra_segundo_apellido == "A":
                cont_segundo_apellido_a += 1
                break # Termino porque ya no existe la necesidad de seeguir recorriendo los caracteres de cada nombre
            elif ultima_letra_segundo_apellido == "E":
                cont_segundo_apellido_e += 1
                break
            elif ultima_letra_segundo_apellido == "I":
                cont_segundo_apellido_i += 1
                break
            elif ultima_letra_segundo_apellido == "O":
                cont_segundo_apellido_o += 1
                break
            elif ultima_letra_segundo_apellido == "U":
                cont_segundo_apellido_u += 1
                break
            else:
                cont_segundo_apellido_consonante += 1
                break
            

resp_primer_apellido = [cont_primer_apellido_a,
                        cont_primer_apellido_e,
                        cont_primer_apellido_i,
                        cont_primer_apellido_o,
                        cont_primer_apellido_u,
                        cont_primer_apellido_consonante
                        ]# Formo una lista con los resultados del primer apellido

cont = 0
for i in resp_primer_apellido: # recorro los resultados del primer apellido e imprimo
    print("En el curso IIC1103 existen", i,
          "estudiantes que su primer apellido termina por", vocales[cont])
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
          "estudiantes que su segundo apellido termina por", vocales[cont])
    cont+=1