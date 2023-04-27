#Angeles Belen Garcia - 1B - Turno mañana 
'''
Ejercicio 03
Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.
No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)
'''
respuesta = "si"
acumulador_edades_femenino = 0
contador_edades_femenino = 0
contador_masculino_nachojulieta = 0
mas_joven_edad = 0
contador_julieta = 0
contador_nacho = 0
contador_marcos = 0
total_votos = 0
porcentaje_julieta = 0
porcentaje_marcos = 0
porcentaje_nacho = 0

while respuesta == "si":
    nombre = input("Ingrese el nombre del votante: ")
    edad = int(input("Ingrese la edad del votante: "))
    while edad < 13:
        edad = int(input("Error - Ingrese la edad del votante: "))
    genero = input("Ingrese el genero del votante: masculino, femenino, otro ")
    while genero != "femenino" and genero != "masculino" and genero != "otro":
        genero = input("Error - Ingrese el genero del votante: masculino, femenino, otro ")
    nombre_participante = input("Ingrese el nombre del participante al que le dara voto positivo: (Nacho, Julieta o Marcos) ")
    while nombre_participante != "Julieta" and nombre_participante != "Nacho" and nombre_participante != "Marcos":
        nombre_participante = input("Error - Ingrese el nombre del participante al que le dara voto positivo: (Nacho, Julieta o Marcos) ")
    match genero:
        case "femenino":
            contador_edades_femenino += 1
            acumulador_edades_femenino += edad
        case "masculino":
            if edad > 25 and edad < 40:
                if nombre_participante == "Julieta" or nombre_participante == "Nacho":
                    contador_masculino_nachojulieta += 0
    match nombre_participante:
        case "Nacho":
            if (contador_nacho == 0 or edad < mas_joven_edad) and nombre_participante == "Nacho":
                mas_joven_edad = edad
                mas_joven_nombre = nombre
            contador_nacho += 1
        case "Julieta":
            contador_julieta += 1
        case "Marcos":
            contador_marcos += 1
    total_votos += 1
    respuesta = input("si desea ingresar mas datos escriba 'si'")

if contador_edades_femenino > 0 :
    promedio_edad_femenino = acumulador_edades_femenino / contador_edades_femenino
    print("El promedio de edad de votantes femeninas es de " , promedio_edad_femenino)

if contador_masculino_nachojulieta > 0:
    print("La cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta, es de: ", contador_masculino_nachojulieta)
print("El nombre del votante mas joven que voto a Nacho es ", mas_joven_nombre)
if contador_julieta > 0:
    porcentaje_julieta = contador_julieta *100 / total_votos
    print("El porcentaje de votos de julieta fue de ", porcentaje_julieta)
if contador_nacho > 0:
    porcentaje_nacho = contador_nacho *100 / total_votos
    print("El porcentaje de votos de Nacho fue de ", porcentaje_nacho)
if contador_marcos > 0:
    porcentaje_marcos = contador_marcos *100 / total_votos
    print("El porcentaje de votos de Marcos fue de ", porcentaje_marcos)

if contador_marcos > contador_julieta and contador_marcos > contador_nacho:
    print("El participante que gano fue Marcos")
elif contador_julieta > contador_nacho:
    print("El participante que gano fue Julieta")
else:
    print("El participante que gano fue Nacho")

