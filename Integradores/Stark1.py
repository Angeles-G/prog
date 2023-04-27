from os import system
from data_stark import lista_personajes

#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
def obtener_nombre_y_dato(lista:list, genero: str):
    '''
    Brief: Obtiene el nombre de los datos que corresponden a genero. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Genero: Parametro que condiciona que nombres se mostraran 
    return: no retorna. Imprime los nombres que cumplen la condicion de genero. 
    '''
    for nombre in lista:
        if nombre['genero'] == genero:
            print(f"Nombre: {nombre['nombre']}")

#Recorrer la lista y determinar cuál es el superhéroe más alto de género M
#D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def calcular_max(lista: list, clave:str, genero:str)->float:
    '''
    Brief: Obtiene el nombre y el valor maximo de lo que se ingrese en el parametro llamado clave y cumpla la condicion de genero. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica sobre que se va calcular el maximo. 
        Genero: parametro determinante para calcular. 
    return: retorna el maximo
    '''
    flag_primero = True
    for valor in lista:
        if valor['genero'] == genero: 
            if flag_primero == True or float(valor[clave]) > max:
                max = float(valor[clave])
                flag_primero = False
    return max

#Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
#F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
def calcular_min(lista: list, clave:str, genero:str)->float:
    '''
    Brief: Obtiene el nombre y el valor minimo de lo que se ingrese en el parametro llamado clave y cumpla la condicion de genero.  
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica sobre que se va calcular el minimo. 
        Genero: parametro determinante para calcular. 
    return: retorna el minimo
    '''
    flag_primero = True
    for valor in lista:
        if valor['genero'] == genero: 
            if flag_primero == True or float(valor[clave]) < min:
                min = float(valor[clave])
                flag_primero = False
    return min

def calcular_max_min_dato(lista:list, calculo:str, clave:str, genero:str):
    '''
    Brief: calcula quienes cumplen con los datos que se ingresan por parametro
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Calculo: parametro que indica que se va a calcular.
        Clave: Parametro que indica sobre que se va calcular lo que se ingrese por el parametro calculo. 
        Genero: parametro que condiciona el calculo
    return: no retorna. imprime el dato que cumple con lo que se pide, junto con los nombres que cumplen la condicion. 
    '''
    if calculo == "maximo":
        calcular = calcular_max(lista,clave , genero)
    elif calculo == "minimo":
        calcular = calcular_min(lista,clave , genero)
    print(f"La {clave} {calculo} es {calcular}: ")
    for valor in lista:
        if float(valor[clave]) == calcular:
            nombre = valor['nombre']
            imprimir_dato(nombre)
#Recorrer la lista y determinar la altura promedio de los superhéroes de género M
#H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
def sumar_dato_heroe(lista:list, clave:str, genero:str)->float:
    '''
    Brief: Obtiene la suma de los datos que coresponden al parametro clave y cumpla la condicion de genero.  
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica de donde se toman los datos. 
        Genero: parametro determinante para calcular. 
    return: retorna la suma acumulada de los datos
    '''
    acumulador_datos = 0
    for dato in lista:
        if dato['genero'] == genero: 
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

def calcular_promedio(lista:list, clave:str, genero:str)->float:
    '''
    Brief: Calcula el promedio, de lo que se ingrese por parametro clave 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica de donde se toman los datos. 
        genero: parametro que determina el calculo
    return: retorna el promedio
    '''
    dividendo = sumar_dato_heroe(lista, clave, genero)
    divisor = cantidad_datos(lista)
    promedio = dividir(dividendo, divisor)
    return promedio

def stark_calcular_imprimir_promedio(lista:list, clave:str, genero:str):
    '''
    Brief: muestra el promedio. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica de que se busca el promedio. 
        Genero: parametro determinante para calcular. 
    return: no retorna. imprime un mensaje con el promdio
    '''
    if len(lista) != 0:
        promedio = calcular_promedio(lista, clave, genero)
        print(f"El promedio de {clave} de genero {genero} es {promedio}")
    else:
        print("Lista vacia")

# Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
def encontrar_valores(lista:list, clave:str):
    '''
    Brief: Obtiene la cantidad de aquello que se ingrese en el parametro clave. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica que se va a contar
    return: retorna la lista de cantidades . 
    '''
    valores = []
    for valor in lista:
        valores.append(valor[clave])
    valores = set(valores)
    lista_cantidades = []
    for valores_que_hay in valores:
        diccionario_cantidad_valores = {}
        diccionario_cantidad_valores ['valor']  = valores_que_hay
        contador = 0
        for valor in lista:
            if valor[clave] == valores_que_hay:
                contador += 1
        diccionario_cantidad_valores ['cantidad'] = contador
        lista_cantidades.append(diccionario_cantidad_valores)
    return lista_cantidades
def mostrar_valores_cantidades(lista:list, clave:str):
    '''
    Brief: muestra el color y las cantidades de lo que se ingrese por parametro clave 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica que se va a contar.  
    return: no retorna . Imprime las cantidades de cada clave. 
    '''
    lista = encontrar_valores(lista, clave)
    for valor in lista:
        match clave:
            case "color_pelo":
                if valor['valor'] != "":
                    print(f"color: {valor['valor']}, cantidad: {valor['cantidad']}")
                else:
                    print(f"color: NO ESPECIFICA, cantidad: {valor['cantidad']}")
            case "color_ojos":
                print(f"color: {valor['valor']}, cantidad: {valor['cantidad']}")
            case "inteligencia":
                if valor['valor'] != "":
                    print(f"inteligencia: {valor['valor']}, cantidad: {valor['cantidad']}")
                else:
                    print(f"inteligencia: No tiene, cantidad: {valor['cantidad']}")

# Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia
def listar_valores(lista:list, clave:str):
    '''
    Brief: lista los superheroes por clave. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Clave: Parametro que indica que se va a listar
    return: no retorna . Imprime los nombres por cada clave. 
    '''
    match clave:
            case "inteligencia":
                nombre = "inteligencia"
            case "color_ojos":
                nombre = "color de ojo"
            case "color_pelo":
                nombre = "color de pelo"
    valores = []
    for valor in lista:
        valores.append(valor[clave])
    valores = set(valores)
    for valores_que_hay in valores:
        
        print(".................................")
        if valores_que_hay == "":
            print(f"{nombre}: No tiene")
        else:
            print(f"{nombre}: {valores_que_hay}")
        for valor in lista:
            if valor[clave] == valores_que_hay:
                print(valor['nombre'])


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
            obtener_nombre_y_dato(lista, "M")
            print(".................................")
            opciones (lista_opciones)
        case 2:
            obtener_nombre_y_dato(lista, "F")
            print(".................................")
            opciones (lista_opciones)
        case 3:
            calcular_max_min_dato(lista, "maximo", "altura", "M")
            print(".................................")
            opciones (lista_opciones)
        case 4:
            calcular_max_min_dato(lista, "maximo", "altura", "F")
            print(".................................")
            opciones (lista_opciones)
        case 5:
            calcular_max_min_dato(lista, "minimo", "altura", "M")
            print(".................................")
            opciones (lista_opciones)
        case 6:
            calcular_max_min_dato(lista, "minimo", "altura", "F")
            print(".................................")
            opciones (lista_opciones)
        case 7:
            stark_calcular_imprimir_promedio(lista, "altura", "M")
            print(".................................")
            opciones (lista_opciones)
        case 8:
            stark_calcular_imprimir_promedio(lista, "altura", "F")
            print(".................................")
            opciones (lista_opciones)
        case 9:
            mostrar_valores_cantidades(lista, "color_ojos")
            print(".................................")
            opciones (lista_opciones)
        case 10:
            mostrar_valores_cantidades(lista, "color_pelo")
            print(".................................")
            opciones (lista_opciones)
        case 11:
            mostrar_valores_cantidades(lista, "inteligencia")
            print(".................................")
            opciones (lista_opciones)
        case 12:
            listar_valores(lista, "color_ojos" )
            print(".................................")
            opciones (lista_opciones)
        case 13:
            listar_valores(lista, "color_pelo" )
            print(".................................")
            opciones (lista_opciones)
        case 14:
            listar_valores(lista, "inteligencia" )
            print(".................................")
            opciones (lista_opciones)
        case 15:
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

lista_opciones = ["1. Mostrar nombres de los superheroes Masculinos",
                "2. Mostrar nombres de los superheroes Femeninos",
                "3. Mostrar el/los mas alto masculino",
                "4. Mostrar el/las mas alto femenino",
                "5. Mostrar el/los mas bajo masculino",
                "6. Mostrar el/las mas bajo femenino",
                "7. Promedio de altura de masculinos",
                "8. Promedio de altura de femeninos",
                "9. Cantidad de cada color de ojos",
                "10. Cantidad de cada color de pelo",
                "11. Cantidad de cada tipo de inteligencia",
                "12. Lista superHeroes por color de ojos",
                "13. Lista superHeroes por color de pelo",
                "14. Lista superHeroes por tipo de inteligencia",
                "15. salir ",]
system("cls")
opciones (lista_opciones)
print("Garcias por utilizar Stark Industries")