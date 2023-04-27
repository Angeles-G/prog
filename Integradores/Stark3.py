#Angeles Belen Garcia
from os import system
from data_stark import lista_personajes

def obtener_lista_nombre(lista:list)->list:
    lista_nombres = []
    for super in lista:
        if super != " ":
            nombre = super['nombre']
            lista_nombres.append(nombre)
    extraer_solo_nombre(lista_nombres)

def extraer_solo_nombre(lista:list):
    for nombre in lista:
        if nombre.isalpha():
            extraer_iniciales(nombre)
        else:
            if nombre.count("-") > 0:
                nombre_heroe = nombre.replace("-", " ")
                extraer_iniciales(nombre_heroe)
            elif nombre.count("the") > 0:
                nombre_heroe = nombre.replace("the", "")
                extraer_iniciales(nombre_heroe)
            else: 
                extraer_iniciales(nombre)



#"nombre": "Howard the Duck",
#"nombre": "Spider-Man",
def extraer_iniciales(nombre_heroe:str):
        nombre = nombre_heroe.split(" ")
        lista_nombres = []
        for parte in nombre:
            if parte != " ":
                nombre_con_mayuscula = parte.capitalize()
                nombre_inicial = nombre_con_mayuscula[:1]
                lista_nombres.append(nombre_inicial)
        if len(lista_nombres) == 1:
            print(lista_nombres[0])
        else:
            lista_nombres[1] != ""
            print(f"{lista_nombres[0]}.{lista_nombres[1]}")
            


obtener_lista_nombre(lista_personajes)