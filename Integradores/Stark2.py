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

def obtener_nombre_y_dato(heroe:dict, clave:str):
    '''
    Brief: Obtiene el nombre junto con el dato corespondiente que se pida
    Parameters: 
        heroe: diccionarios de los superheroes.
        Clave: Parametro que indica a que va adjunto el nombre.
    return: no retorna. a medida que se ejecuta se imprime un mensaje con el nombre y el dato clave ingresado. 
    '''
    print(f"Nombre: {heroe['nombre']} | {clave}: {heroe[clave]}")

def stark_imprimir_nombres_alturas(lista:list):
    '''
    Brief: Obtiene el nombre junto con el dato altura, llamando a la funcion obtener_nombre_y_dato.
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
    return: no retorna. a medida que se ejecuta se imprime un mensaje con el nombre y la altura.  
    '''
    if len(lista) != "":
        for heroe in lista:
            obtener_nombre_y_dato(heroe, "altura")

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

def calcular_max_min_dato(lista:list, calculo:str, clave:str):
    '''
    Brief: calcula quienes cumplen con los datos que se ingresan por parametro
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Calculo: parametro que indica que se va a calcular.
        Clave: Parametro que indica sobre que se va calcular lo que se ingrese por el parametro calculo. 
    return: retorna el maximo o minimo
    '''
    if calculo == "maximo":
        calcular = calcular_max(lista, clave)
    elif calculo == "minimo":
        calcular = calcular_min(lista, clave)
    return calcular

def stark_calcular_imprimir_heroe(lista:list, calculo:str, clave:str):
    '''
    Brief: calcula quienes cumplen con los datos que se ingresan por parametro
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes.
        Calculo: parametro que indica que se va a calcular.
        Clave: Parametro que indica sobre que se va calcular lo que se ingrese por el parametro calculo. 
    return: no retorna. imprime el dato que cumple con lo que se pide, junto con los nombres que cumplen la condicion. 
    '''
    calcular = calcular_max_min_dato(lista, calculo, clave)
    print(f"La {clave} {calculo} es {calcular}: ")
    for valor in lista:
        if float(valor[clave]) == calcular:
            #obtener_nombre_y_dato(valor,clave)
            nombre = valor['nombre']
            imprimir_dato(nombre)

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
        divicion = 0
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

def stark_calcular_imprimir_promedio_altura(lista:list):
    '''
    Brief: muestra el promedio. 
    Parameters: 
        Lista: Lista de personajes, que contiene diccionarios de los superheroes. 
    return: no retorna. imprime un mensaje cone l promdio
    '''
    if len(lista) != 0:
        promedio = calcular_promedio(lista, "altura")
        print(f"El promedio de altura es {promedio}")
    else:
        print("Lista vacia")

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
            normalizar = stark_normalizar_datos(lista)
            if normalizar:
                print("Datos normalizados")
            else:
                print(-1)
            print(".................................")
            opciones (lista_opciones)
        case 2:
            stark_imprimir_nombres_heroes(lista)
            print(".................................")
            opciones (lista_opciones)
        case 3:
            stark_imprimir_nombres_alturas(lista)
            print(".................................")
            opciones (lista_opciones)
        case 4:
            stark_calcular_imprimir_heroe(lista, "maximo", "altura")
            print(".................................")
            opciones (lista_opciones)
        case 5:
            stark_calcular_imprimir_heroe(lista, "minimo", "altura")
            print(".................................")
            opciones (lista_opciones)
        case 6: 
            stark_calcular_imprimir_promedio_altura(lista)
            print(".................................")
            opciones (lista_opciones)
        case 7:
            stark_calcular_imprimir_heroe(lista, "maximo", "peso")
            print(".................................")
            opciones (lista_opciones)
        case 8:
            stark_calcular_imprimir_heroe(lista, "minimo", "peso")
            print(".................................")
            opciones (lista_opciones)
        case 9:
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

lista_opciones = ["1. Normalizar datos",
                "2. Mostrar nombres de los superheroes",
                "3. Mostrar los nombres con la altura",
                "4. Mostrar el mas alto",
                "5. Mostrar el mas bajo",
                "6. Mostrar promedio de altura",
                "7. Mostrar mas pesado",
                "8. Mostrar menos pesado",
                "9. salir ",]

system("cls")
opciones (lista_opciones)
print("Garcias por utilizar Stark Industries")