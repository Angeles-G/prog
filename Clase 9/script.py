from os import system
import re

def parser_csv(path:str)->list:
    lista = []
    archivo = open(path, "r", encoding = "utf-8")
    for line in archivo:
        lectura = re.split(r",|\n", line)
        tema = {}
        tema ["title"] = lectura[0]
        tema ["views"] = int(lectura[1])
        tema ["length"] = int(lectura[2])
        tema ["img_url"] = lectura[3]
        tema["url"] = lectura[4]
        tema["date"] = lectura[5]
        lista.append(tema)
    archivo.close()
    return lista


def mostrar_lista_tema_views(lista:list):
    for tema in lista:
        print(f"{tema['title']}, - {tema['views']}")

def calcular_maximo(lista:list, clave:str)-> int:
    '''
    Brief: calcula el maximo valor numerico en una lista, en base a una clave
    Parameters: 
        Lista: list --> lista sobre la que voy a hacer la busqueda
        Clave: str --> clave con la cual realizo la busqueda en la lista
    Return: retorna un intero que representa el maximo valor de la clave
    '''
    flag_primero = True
    if (type(lista) == list and len(lista) >0 and type(clave)== str and clave != ""):
        for tema in lista:
            if flag_primero == True or tema[clave] > maximo:
                maximo = tema[clave]
                flag_primero = False
    return maximo

def mostrar_lista_tema(lista:list, valor = None, clave = None):
    if clave is None:
        for tema in lista:
            print(f"{tema['title']}")
    else:
        for tema in lista:
            if tema[clave] == valor:
                print(f"{tema['title']}")

def buscar_tamas_mas_views(lista:list):
    maxima_view = calcular_maximo(lista, "views")
    print(f"Cantidad maxima de reproduccion: {maxima_view}")
    mostrar_lista_tema(lista, maxima_view, "views")

def buscar_temas_menos_views():
    flag_primero = True

    for tema in lista_bzrp:
        if flag_primero == True or tema['views'] < minima_views:
            minima_views = tema['views']
            flag_primero = False
    
    print(f"Cantidad minima de reproduccion: {minima_views}")

    for tema in lista_bzrp:
        if tema['views'] == minima_views:
            print(f"{tema['title']}")

def mostrar_promedio_views():
    acumulador_views = 0

    for tema in lista_bzrp:
        acumulador_views += tema['views']
    
    contador_tema = len(lista_bzrp)
    promedio_views = acumulador_views / contador_tema

    print(f"El promedio de vistas es {promedio_views}")

def mostrar_menu():
    for opcion in menu:
        print(opcion)

menu = ["1. mostar tema","2. mostrar temas con vistas",
        "3. Mostrar temas mas vistos", "4. Mostrar temas menos vistos", 
        "5. Mostrar el promedio de reproducciones", "6. Salir"]

system("cls")

while True: 
    print(".................................")
    mostrar_menu()
    lista_bzrp = parser_csv("data.csv")
    respuesta = int(input("Elija una opción: "))
    match respuesta:
        case 1: 
            print(".................................")
            mostrar_lista_tema(lista_bzrp)
        case 2: 
            print(".................................")
            mostrar_lista_tema_views(lista_bzrp)
        case 3: 
            print(".................................")
            buscar_tamas_mas_views(lista_bzrp)
        case 4: 
            print(".................................")
            buscar_temas_menos_views()
        case 5:
            print(".................................")
            mostrar_promedio_views()
        case 6:
            break













