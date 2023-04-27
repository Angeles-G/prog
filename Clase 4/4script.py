'''
Angeles Belen Garcia
Debemos desarrollar un algoritmo que permita computar los votos del Senado de
Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en
la sesión. Si el senador está presente, se deberá pedir el valor del voto
El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención
(validar). El valor por defecto para los senadores ausentes será Abstención.
Se deberá Informar:

o Cantidad total de senadores.
o Cantidad de senadores presentes.
o Cantidad y porcentaje de votos afirmativos.
o Cantidad y porcentaje de votos negativos.
o Cantidad y porcentaje de abstenciones.
o Generar una lista de senadores por cada tipo de voto y mostrarlas por
pantalla.
'''
contador_senadores = 0
contador_senadores_presentes = 0
contador_abstencion = 0
contador_afirmativo = 0
contador_negativo = 0
lista_senadores_abstencion = []
lista_senadores_afirmativo = []
lista_senadores_negativo = []
seguir = True

while seguir:
    nombre_senador = input("Ingrese el nombre del senador: ")
    presente = input("¿Esta presente? si/ no ")
    while presente != "si" and presente != "no":
        presente = input("Error - ¿Esta presente? si/ no ")
    if presente == "si":
        voto = input("Indique si voto: afirmativo - negativo - abstencion ")
        while voto != "afirmativo" and voto != "negativo" and voto != "abstencion":
            voto = input("Error - Indique si voto: afirmativo - negativo - abstencion")
        contador_senadores_presentes += 1
    else:
        voto = "abstencion"
    un_senador = {}
    un_senador ['Nombre'] = nombre_senador
    un_senador ['Asistencia'] = presente
    un_senador ['voto'] = voto
    match voto:
        case "abstencion":
            lista_senadores_abstencion.append(un_senador)
            contador_abstencion +=1
        case "afirmativo":
            lista_senadores_afirmativo.append(un_senador)
            contador_afirmativo +=1
        case "negativo":
            lista_senadores_negativo.append(un_senador)
            contador_negativo +=1
    contador_senadores += 1
    respuesta = input("¿Hay mas senadores? si / no ")
    if respuesta != "si":
        seguir = False

print("----------------------------------------------------------------")
print (f"La cantidad total de senadores es de {contador_senadores}")
print (f"La cantidad de senadores presentes es de {contador_senadores_presentes}")

if contador_abstencion != 0:
    porsentaje_abstencion = contador_abstencion *100 / contador_senadores
    print(f"El porcentaje de abstenciones fue de {porsentaje_abstencion} con {contador_abstencion} votos")
if contador_afirmativo != 0:
    porcentaje_afirmativo = contador_afirmativo *100 / contador_senadores
    print(f"El porcentaje de votos afirmativos fue de {porcentaje_afirmativo} con {contador_afirmativo} votos")
if contador_negativo != 0: 
    porcentaje_negativo =  contador_negativo *100 / contador_senadores
    print(f"El porcentaje de votos negativos fue de {porcentaje_negativo} con {contador_negativo} votos")
print("----------------------------------------------------------------")
print(f"Senadores de voto afirmativo: ")
for afirmativo in lista_senadores_afirmativo:
    print(f"Nombre: {afirmativo['Nombre']}\nVoto: {afirmativo['voto']}\nAsistencia: {afirmativo['Asistencia']}")
print("---------------------------------------")
print(f"Senadores de voto Negativo:")
for negativo in lista_senadores_negativo:
    print(f"Nombre: {negativo['Nombre']}\nVoto: {negativo['voto']}\nAsistencia: {negativo['Asistencia']}")
print("---------------------------------------")
print(f"Senadores de voto Abstenciones:")
for abstencion in lista_senadores_abstencion:
    print(f"Nombre: {abstencion['Nombre']}\nVoto: {abstencion['voto']}\nAsistencia: {abstencion['Asistencia']}")
