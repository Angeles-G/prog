from os import system
from data_stark import lista_personajes

def buscar_nombres():
    #B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    for nombre in lista_personajes:
        print(nombre['nombre'], nombre['peso'])

def buscar_mas_alto():
    #Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    flag_primero = True

    for altura in lista_personajes:
        if flag_primero == True or float(altura['altura']) > mas_alto:
            mas_alto = float(altura['altura'])
            flag_primero = False

    print(f"La altura maxima es {mas_alto}: ")
    
    for altura in lista_personajes:
        if float(altura['altura']) == mas_alto:
            mas_alto = altura['nombre']
            print(mas_alto)

def buscar_mas_bajo():
    #Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    flag_primero = True

    for altura in lista_personajes:
        if flag_primero == True or float(altura['altura']) < mas_bajo:
            mas_bajo = float(altura['altura'])
            flag_primero = False

    print(f"La menor altura es de {mas_bajo}: ")

    for altura in lista_personajes:
        if float(altura['altura']) == mas_bajo:
            mas_bajo = altura['nombre']
            print(mas_bajo)

def buscar_promedio_altura():
    #Recorrer la lista y determinar la altura promedio de los superhéroes
    acumulador_alturas = 0
    contador_personajes = 0

    for altura in lista_personajes:
        acumulador_alturas += float(altura['altura'])
        contador_personajes += 1

    promedio_altura = acumulador_alturas / contador_personajes

    print(f"La altura promedio de los personajes es de {promedio_altura}")

def mostrar_mas_pesado():
    #Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores
    #Calcular e informar cual es el superhéroe más y menos pesado.
    # mas pesado:
    flag_primero = True

    for peso in lista_personajes:
        if flag_primero == True or float(peso['peso']) > mas_pesado:
            mas_pesado = float(peso['peso'])
            flag_primero = False

    print(f"El maximo peso es {mas_pesado}: ")

    for peso in lista_personajes:
        if float(peso['peso']) == mas_pesado:
            mas_pesado = peso['nombre']
            print(mas_pesado)

def mostrar_menos_pesado():
    #menos pesado:
    flag_primero = True

    for peso in lista_personajes:
        if flag_primero == True or float(peso['peso']) < menos_pesado:
            menos_pesado = float(peso['peso'])
            flag_primero = False

    print(f"El menor peso es de {menos_pesado}: ")

    for peso in lista_personajes:
        if float(peso['peso']) == menos_pesado:
            menos_pesado = peso['nombre']
            print(menos_pesado)


lista_opciones = ["1. Mostrar nombres de los superheroes",
                "2. Mostrar el mas alto",
                "3. Mostrar el mmas bajo",
                "4. Mostrar promedio de altura",
                "5. Mostrar mas pesado",
                "6. Mostrar menos pesado",
                "7. salir ",]

def mostrar_opciones():
    for opcion in lista_opciones:
        print(opcion)

system("cls")
#Ordenar el código implementando una función para cada uno de los valores informados.
#Construir un menú que permita elegir qué dato obtener
while True:
    print(".................................")
    mostrar_opciones()
    respuesta = int(input("Elija una opcion: "))
    match respuesta:
        case 1:
            print(".................................")
            buscar_nombres()
        case 2:
            print(".................................")
            buscar_mas_alto()
        case 3:
            print(".................................")
            buscar_mas_bajo()
        case 4:
            print(".................................")
            buscar_promedio_altura()
        case 5:
            print(".................................")
            mostrar_mas_pesado()
        case 6:
            print(".................................")
            mostrar_menos_pesado()
        case 7:
            break











