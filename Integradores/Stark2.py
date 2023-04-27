#Angeles Belen Garcia
from os import system
from data_stark import lista_personajes

def stark_normalizar_datos(lista: list)->bool:
    '''
    Brief: transforma y valiad si los datos pueden convertirse en nuemros flotantes
    Parameters: 
        lista: lista de personajes
    return: retorna True o False segun corresponda
    '''
    validar = False # inicializo una variable booleana en flase 
    if len(lista) != 0:
        for super in lista: # -> dict de cada super heroe
            super = list(super) # -> me da las claves 
            break # -> salgo cuando encuentro las claves por primera vez
        for dato in lista: # -> recorro la lista de personajes
            for clave in super: # -> busco en cada uno de los personajes el dato de la clave(las claves estan en super)
                try: # -> controlo que el dato en dicha clave pueda pasarse a float 
                    dato[clave] = float(dato[clave])
                    validar = True # Declaro una variable booleana en true 
                except: # -> sino no hace nada
                    pass
    else:
        print("lista vacia")
    return validar

def imprimir_dato(dato:str = None, lista:list = None):
    '''
    Brief: Muestra el dato que se ingrese
    Parameters: 
        dato: aquello que se quiere mostrar
        lista: lista que se quiere mostrar
    return: no retorna. imprime el dato. 
    '''
    if lista == None:
        print(dato)
    else:
        for datos in lista:
            print(datos)


def heroes(lista:list):
    '''
    Brief: obtener el diccionario de cada superheroe. 
    Parameters: 
        lista: lista de personajes
    return: no retorna, le envia  el diccionario a la funcion Obtener_nombre. 
    '''
    for super in lista:
        obtener_nombre(super)

def obtener_nombre(heroe: dict):
    '''
    Brief: Obtiene la key 'nombre' de un diccionario de datos. 
    Parameters: 
        heroe: Diccionario de un superHeroe. 
    return: no retorna, le envia los datos que se deben imprimir a la funcion que corresponde
    '''
    nombre = heroe['nombre']
    imprimir_dato(nombre)


def stark_imprimir_nombres_heroes(lista: list):
    '''
    Brief: muestra la lista de nombres de los personajes 
    Parameters: 
        lista: Lista que contiene a todos los personajes
    return: no retorna, llama a otra funcion para mostrar datos
    '''
    if (len(lista) != 0):
        print("Muestra la lista de nombres: ")
        print("Nombres: ")
        heroes(lista)    
    else:
        print(-1)

if stark_normalizar_datos(lista_personajes): # si me devuelve True: 
    print("Datos normalizados")# -> si se puede me dice que se normalizaron los datos 
stark_imprimir_nombres_heroes(lista_personajes)
