#Angeles Belen Garcia
from os import system
from data_stark import lista_personajes
import re

#"Star-Lord"
#"Howard the Duck"
def extraer_iniciales(nombre_heroe:str)->str:
    '''
    Brief: parte el nombre ingresado por donde corresponda y obtiene la primera letra de las partes. 
    Parameters:
            nombre_heroe: parametro que indica el nombre del cual se van a sacar las iniciales. 
    return: retorna las iniciales en mayuscula con un punto, de ser posible. 
    '''
    if nombre_heroe != "":
        mayusculas = nombre_heroe.upper()
        if nombre_heroe.count("THE")>0:
            reemplazar = nombre_heroe.replace("THE", "")
            print(reemplazar)
            nombre_sin_espacio = re.sub(r'\s+', "", reemplazar)
            nombre = re.findall("([A-Z])[A-Z]+", nombre_sin_espacio)
            print(nombre)
            punto = "."
            text = punto.join(nombre)
            print(text)
        else:
            nombre = re.findall("([A-Z])[A-Z]+", mayusculas)
            punto = "."
            text = punto.join(nombre)
            print(text)
    else:
        inicial = "N/A"


extraer_iniciales("star THE lord")
