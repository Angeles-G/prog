from os import system
from data_stark import lista_personajes

def stark_normalizar_datos (lista:list):
    '''
    Brief: Convierte los datos que deben ser numeros y son strings a numeros. 
    Parameters:
        Lista --> lista sobre la cual voy hacer la busqueda.
    Return: retorna un mensaje de acuerdo a lo ocurrido al intentar normalizar los datos 
    '''
    flag = 0
    if len(lista) != 0:
        contador= 0
        for indice in range(len(lista)):
            for datos in lista:
                if type(datos['altura']) != int:
                    datos['altura'] = float(datos['altura'])
                    flag = 1
                if type(datos['peso']) != int:
                    datos['peso'] = float(datos['peso'])
                    flag = 1
                if type(datos['fuerza']) != int:
                    datos['fuerza'] = float(datos['fuerza'])
                    flag = 1
    else:
        mensaje = "Error: Lista de héroes vacía"
    if flag == 1:
        mensaje = "Datos normalizados"
    return mensaje

def obtener_nombre (heroe:dict ):
    pass
    






mensaje = stark_normalizar_datos(lista_personajes)
print(mensaje)



