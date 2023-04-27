from os import system
from data_stark import lista_personajes

#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def obtener_nombre_y_dato(lista:list, clave:str= None):
    '''
    Brief: Obtiene el nombre junto con el dato corespondiente que se pida
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica a que va adjunto el nombre.
    return: no retorna. a medida que se ejecuta se imprime un mensaje con el nombre y el dato clave ingresado. 
    '''
    if clave != None:
        for nombre in lista:
            print(f"Nombre: {nombre['nombre']} | {clave}: { nombre[clave]}")
    else: 
        for nombre in lista:
            print(f"Nombre: {nombre['nombre']}")

#C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def stark_imprimir_nombres_alturas(lista:list):
    '''
    Brief: Obtiene el nombre junto con el dato altura, llamando a la funcion obtener_nombre_y_dato.
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
    return: no retorna. a medida que se ejecuta se imprime un mensaje con el nombre y la altura.  
    '''
    if len(lista) != "":
        obtener_nombre_y_dato(lista, "altura")

#Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def calcular_max(lista: list, clave:str)->float:
    '''
    Brief: Obtiene el nombre y el valor maximo de lo que se ingrese en el parametro llamado clave. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica sobre que se va calcular el maximo. 
    return: retorna el maximo
    '''
    flag_primero = True
    for valor in lista:
        if flag_primero == True or float(valor[clave]) > max:
            max = float(valor[clave])
            flag_primero = False
    return max

#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def calcular_min(lista: list, clave:str)->float:
    '''
    Brief: Obtiene el nombre y el valor minimo de lo que se ingrese en el parametro llamado clave. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica sobre que se va calcular el minimo. 
    return: retorna el minimo
    '''
    flag_primero = True
    for valor in lista:
        if flag_primero == True or float(valor[clave]) < min:
            min = float(valor[clave])
            flag_primero = False
    return min

#F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def sumar_dato_heroe(lista:list, clave:str)->float:
    '''
    Brief: Obtiene la suma de los datos que coresponden al parametro clave. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica de donde se toman los datos. 
    return: retorna la suma acumulada de los datos
    '''
    acumulador_datos = 0
    for dato in lista:
        acumulador_datos += float(dato[clave])
    return acumulador_datos

def dividir(dividendo:float, divisor:int) -> float:
    '''
    Brief: Realiza una divicion entre dos numeros. 
    Parameters: 
        dividendo: Numero que se desea dividir.
        divisor: Numero que dividira al parametro dividendo. 
    return: retorna el resultado de la divicion.
    '''
    if divisor != 0:
        divicion = dividendo / divisor 
    else:
        division = 0
    return divicion 

def cantidad_datos(lista:list)->int:
    '''
    Brief: cuenta la cantidad de datos en la lista
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
    return: retorna la cantidad de datos en la lista
    '''
    contador_personajes = 0
    for dato in range(len(lista)):
        contador_personajes += 1
    return contador_personajes

def calcular_promedio(lista:list, clave:str)->float:
    '''
    Brief: Calcula el promedio, de lo que se ingrese por parametro clave 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica de donde se toman los datos. 
    return: retorna el promedio
    '''
    dividendo = sumar_dato_heroe(lista, clave)
    divisor = cantidad_datos(lista)
    promedio = dividir(dividendo, divisor)
    return promedio

def stark_calcular_imprimir_promedio(lista:list, clave:str):
    '''
    Brief: muestra el promedio. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica de que se busca el promedio. 
    return: no retorna. imprime un mensaje cone l promdio
    '''
    if len(lista) != 0:
        promedio = calcular_promedio(lista, clave)
        print(f"El promedio de {clave} es {promedio}")
    else:
        print("Lista vacia")

#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
def calcular_max_min_dato(lista:list, calculo:str, clave:str):
    '''
    Brief: calcula quienes cumplen con los datos que se ingresan por parametro
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Calculo: parametro que indica que se va a calcular.
        Clave: Parametro que indica sobre que se va calcular lo que se ingrese por el parametro calculo. 
    return: no retorna. imprime el dato que cumple con lo que se pide, junto con los nombres que cumplen la condicion. 
    '''
    if calculo == "maximo":
        calcular = calcular_max(lista, clave)
    elif calculo == "minimo":
        calcular = calcular_min(lista, clave)
    print(f"La {clave} {calculo} es {calcular}: ")
    for valor in lista:
        if float(valor[clave]) == calcular:
            nombre = valor['nombre']
            imprimir_dato(nombre)

#Construir un menú que permita elegir qué dato obtener
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

def imprimir_menu(lista:list): 
    '''
    Brief: Imprime el menu
    Parameters: 
        lista: lista de menu. 
    return: no retorna. imprime el menu. 
    '''
    imprimir_dato(lista = lista)

def validar_entero(dato:str)->bool:
    '''
    Brief: Valida si el dato ingresado es un entero
    Parameters: 
        Dato: dato a validar 
    return: retorna true o false. 
    '''
    try:
        entero = int(dato) 
        tipo_de_dato = type(entero) 
        if tipo_de_dato == int:
            validar = True
    except:
        validar = False
    return validar

def stark_menu_principal(num: int)->int:
    '''
    Brief: Devuelve el numero ingresado casteado de ser posible. 
    Parameters: 
        Num: numero a validar
    return: retorna el numero casteado a entero. 
    '''
    validacion = validar_entero(num)
    if validacion:
        numero = int(num)
    else:
        numero = -1
    return numero

def stark_marvel_app(lista:list, numero: int): 
    '''
    Brief: Muestra aquello que se pide. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Numero: Opcion elegida por el usuario. 
    return: no retorna. imprime aquello que el usuario solicita 
    '''
    match numero:
        case 1:
            obtener_nombre_y_dato(lista = lista)
            print(".................................")
            opciones (lista_opciones)
        case 2:
            obtener_nombre_y_dato(lista , "altura")
            print(".................................")
            opciones (lista_opciones)
        case 3:
            calcular_max_min_dato(lista, "maximo", "altura")
            print(".................................")
            opciones (lista_opciones)
        case 4:
            calcular_max_min_dato(lista, "minimo", "altura")
            print(".................................")
            opciones (lista_opciones)
        case 5:
            stark_calcular_imprimir_promedio(lista, "altura")
            print(".................................")
            opciones (lista_opciones)
        case 6:
            calcular_max_min_dato(lista, "maximo", "peso")
            print(".................................")
            opciones (lista_opciones)
        case 7:
            calcular_max_min_dato(lista, "minimo", "peso")
            print(".................................")
            opciones (lista_opciones)
        case 8:
            pass

def opciones (lista:list):
    '''
    Brief: Solicita al usuario una opcion 
    Parameters: 
        Lista: Lista de opciones
        Numero: Opcion elegida por el usuario. 
    return: no retorna. Llama a funcion. 
    '''
    imprimir_menu(lista = lista)
    while True:
        numero = input("Ingrese un numero: ")
        num = stark_menu_principal(numero)
        if num != -1:
            break
    stark_marvel_app(lista_personajes, num)

lista_opciones = ["1. Mostrar nombres de los superheroes",
                "2. Mostrar los nombres con la altura",
                "3. Mostrar el mas alto",
                "4. Mostrar el mas bajo",
                "5. Mostrar promedio de altura",
                "6. Mostrar mas pesado",
                "7. Mostrar menos pesado",
                "8. salir ",]

system("cls")
opciones (lista_opciones)
print("Garcias por utilizar Stark Industries")
