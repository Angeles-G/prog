#Angeles Belen Garcia
from os import system
from data_stark import lista_personajes

def extraer_iniciales(nombre_heroe:str)->str:
    '''
    Brief: parte el nombre ingresado por donde corresponda y obtiene la primera letra de las partes. 
    Parameters:
            nombre_heroe: parametro que indica el nombre del cual se van a sacar las iniciales. 
    return: retorna las iniciales en mayuscula con un punto, de ser posible. 
    '''
    if nombre_heroe != " " and nombre_heroe != "":
        if nombre_heroe.count("the") > 0:
            partes_nombre = nombre_heroe.split(" the ")
        elif nombre_heroe.count("-") > 0:
            partes_nombre = nombre_heroe.split("-")
        elif nombre_heroe.count(" ")>0:
            partes_nombre = nombre_heroe.split(" ")
        else:
            inicial = nombre_heroe[:1].capitalize()
            partes_nombre = []
        
        if len(partes_nombre) > 0:
            for parte in partes_nombre:
                inicial_mayuscula = parte[:1].capitalize()
                for otra_parte in partes_nombre:
                    if parte != otra_parte:
                        otra_inicial_mayusula = otra_parte[:1].capitalize()
                        unir = "."
                        inicial = unir.join([inicial_mayuscula, otra_inicial_mayusula])
                        break
                break
    else:
        inicial = "N/A"
    return inicial

def definir_iniciales_nombre(heroe:dict)->bool:
    '''
    Brief: defino una nueva key en el diccionario ingresado donde guardo las iniciales, obtenidas de la funcion Extraer_iniciales. 
    Parameters:
            heroe: diccionario que contiene los datos de un superHeroe. 
    return: retorna un booleano que determina si el dato se pudo agregar o no al diccionario
    '''
    tipo = type(heroe)
    if tipo != dict:
        definicion = False
    elif heroe['nombre'] != " " and heroe['nombre'] != "":
        nombre = heroe['nombre']
        iniciales = extraer_iniciales(nombre)
        heroe['iniciales'] = iniciales
        definicion = True
    else:
        definicion = False
    return definicion

def agregar_iniciales_nombre(lista:list)->bool:
    '''
    Brief: recibe una lista y le envia los diccionarios uno a uno a la funcion definir_iniciales. 
    Parameters:
            lista: lista de superheroes, que contiene en diccionarios la informacion de cada superheroe. 
    return: retorna un booleano que indica si el resultado de la funcion definir_iniciales_nombre funciono correctamente. 
    '''
    tipo = type(lista)
    if tipo == list and len(lista) !=0:
        for dic_heroe in lista:
            definicion = definir_iniciales_nombre(dic_heroe)
            if definicion == False:
                print("El origen de datos no contiene el formato correcto")
                agregar = False
            else:
                agregar = True
    return agregar

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    '''
    Brief: muestra el nombre de los superheroes que hay junto con sus iniciales. 
    Parameters:
            lista_heroes: lista de superheroes que contiene los datos de cada superheroe en diccionarios. 
    return: no retorna. 
    '''
    tipo = type(lista_heroes)
    if tipo == list and len(lista_heroes)>0:
        agregar_iniciales_nombre(lista_heroes)
        for super in lista_heroes:
            nombre = super['nombre']
            iniciales = super['iniciales']
            print(f"* {nombre} ({iniciales})")

def generar_codigo_heroe (id_heroe:int, genero_heroe:str)->str:
    '''
    Brief: genera un codigo de una cantidad exacta de caracteres, a partir de los parametros dados.
    Parameters:
            id_heroe: numero entero. Se espera un numero del 1 al len de la lista de superheroes.
            genero_heroe: un string que espera recibir el genero del heroe. 
    return: retorna el id generado.  
    '''
    tipo_id = type(id_heroe)
    if  tipo_id == int and genero_heroe != " " and (genero_heroe == "F" or genero_heroe == "M" or genero_heroe == "NB"):
        id_heroe = str(id_heroe)
        if len(genero_heroe) == 1:
            id_numerico = id_heroe.zfill(8)
        else:
            id_numerico = id_heroe.zfill(7)
        guion = "-"
        id =guion.join([genero_heroe, id_numerico])
        #print(id)
    else:
        print("N/A")
        id = 0
    return id 

def agregar_codigo_heroe(heroe:dict, id_heroe:int)->bool:
    '''
    Brief: genera una nueva key en el diccionario que recibe, con un value que sera el id generado en la funcion generar_codigo_heroe.
    Parameters:
            id_heroe: numero entero. Se espera un numero del 1 al len de la lista de superheroes.
            heroe: un diccionario que contiene los datos especificos de un heroe. 
    return: retorna un booleano que indica si los nuevos datos ingresados al diccionario se agregaron. 
    '''
    if len(heroe) > 0:
        genero = heroe['genero']
        id = generar_codigo_heroe(id_heroe, genero)
        if id !=0:
            id_numerico = id.index("-")
            #print (id_numerico)
            if id_numerico == 1 or id_numerico == 2:
                heroe['codigo heroe'] = id
                validaciones = True
            else:
                validaciones = False
        else:
            validaciones = False
    else:
        validaciones = False
    return validaciones

def stark_generar_codigos_heroes(lista:list):
    '''
    Brief: 
        Establece el id del heroe de acuerdo a la posicion del mismo en la lista, comenzando en uno 
        Indica el primero y el ultimo de los codigos generados. 
    Parameters:
            lista: Lista de  heroes, que contiene un diccionario por heroe. 
    return: no retorna, muestra el primero y el ultimo de los codigos generados y la cnatidad total. 
    '''
    bandera_del_primero = True
    id_heroe = 0
    for dic_heroe in lista:
        id_heroe += 1
        agregado = agregar_codigo_heroe(dic_heroe, id_heroe)
        if agregado:
            if bandera_del_primero:
                id_heroe_primero = dic_heroe['codigo heroe']
                bandera_del_primero = False
            else:
                id_heroe_final = dic_heroe['codigo heroe']

    print (f"Se asignaron {id_heroe} codigos")
    print (f"El codigo del primer heroe es {id_heroe_primero}")
    print (f"El codigo del ultimo heroe es {id_heroe_final}\n")

def encontrar_numeros(numero_sin_espacios: str)->int:
    '''
    Brief: Busca en un string si hay algun numero. 
    Parameters:
            numero_sin_espacios: un string sin espacios, donde puede llegar a haber un numero. 
    return: retorna la cantidad de numeros encontrados. 
    '''
    cantidad_de_numeros = 0
    for numero in range(0, 10):
        numero_str = str(numero)
        if numero_sin_espacios.count(numero_str) > 0: 
            cantidad_de_numeros += numero_sin_espacios.count(numero_str)
    return cantidad_de_numeros

def sanitizar_entero(num_str:str)->int: 
    '''
    Brief: recibe un string que puede ser un numero, de serlo lo convierte a entero
    Parameters:
            num_str: posible entero. 
    return: retorna:
        -1: en caso que sea solo alfabetico. 
        -2: en caso que sea negativo.
        -3: en caso que sea alfanumerico.
        el numero convertido: si es que es solo numero. 
    '''
    if num_str != " " and num_str != "":
        tipo = type(num_str)
        if tipo == str:
            caracter_sin_espacios = num_str.strip()
            caracteres = caracter_sin_espacios.isalpha()
            if caracteres:
                #print("No es entero positivo")
                validar = -1
            else: 
                cantidad_de_numeros = 0
                cantidad_de_caracteres = len(caracter_sin_espacios)
                cantidad_de_numeros = encontrar_numeros(caracter_sin_espacios)
                if cantidad_de_caracteres == cantidad_de_numeros:
                    convertir_numero = int(caracter_sin_espacios)
                    #print (f"Numero convertido {convertir_numero}")
                    validar = convertir_numero
                elif cantidad_de_numeros > 0:
                    if caracter_sin_espacios.count("-") == 1 and caracter_sin_espacios.index("-") == 0:
                        partir = caracter_sin_espacios.split("-")
                        if len(partir) >2: 
                            #print("No es entero positivo")
                            validar = -3
                        else:
                            for parte in partir:
                                cantidad_de_numeros = 0
                                cantidad_de_caracteres = len(parte)
                                cantidad_de_numeros = encontrar_numeros(parte)
                            if cantidad_de_caracteres == cantidad_de_numeros:
                                #print("No es entero positivo")
                                validar = -2
                            else:
                                #print("No es entero positivo")
                                validar = -3
                    else:
                        #print("No es entero positivo")
                        validar = -3
                else:
                    #print("No es entero positivo")
                    validar = -3
    else:
        #print("No es entero positivo")
        validar = -3
    return validar 

def sanitizar_flotante(num_str:str)->float:
    '''
    Brief: recibe un string que puede ser un numero flotante, de serlo lo convierte a flotante
    Parameters:
            num_str: posible flotante. 
    return: retorna:
        -1: en caso que sea solo alfabetico. 
        -2: en caso que sea negativo.
        -3: en caso que sea alfanumerico.
        el numero convertido: si es que es solo numero. 
    '''
    tipo = type(num_str)
    if tipo == str:
        caracter_sin_espacios = num_str.strip()
        caracteres = caracter_sin_espacios.isalpha()
        if caracteres:
            #print("No es flotante positivo")
            validar = -1
            return validar
        else:
            cantidad_de_numeros = encontrar_numeros(caracter_sin_espacios)
            if cantidad_de_numeros > 0:
                if caracter_sin_espacios.count(".") == 1 and caracter_sin_espacios.count("-") == 0:
                    partir = caracter_sin_espacios.split(".")
                    si_hay_numero = 0
                    for parte in partir:
                        if parte == "" or parte == " ":
                            #print("No es flotante positivo")
                            validar = -3
                            return validar
                        else:
                            hay_solo_letras = parte.isalpha()
                            if hay_solo_letras:
                                #print("No es flotante positivo")
                                validar = -3
                                return validar
                            else:
                                hay_numeros = encontrar_numeros(parte)
                                if len(parte) == hay_numeros:
                                    si_hay_numero += 1
                                else:
                                    #print("No es flotante positivo")
                                    validar = -3
                                    return validar
                    if len(partir) == si_hay_numero:
                        convertir_numero = float(num_str)
                        #print(f"El numero convertido es {convertir_numero}")
                        validar = convertir_numero
                        return validar
                    else:
                        #print("No es flotante positivo")
                        validar = -3
                        return validar
                elif caracter_sin_espacios.count(".") == 1 and caracter_sin_espacios.count("-") == 1:
                    if caracter_sin_espacios.index("-") == 0:
                        partir = caracter_sin_espacios.split(".")
                        si_hay_numero = 0
                        for parte in partir:
                            if parte == "" or parte == " ":
                                #print("No es flotante positivo")
                                validar = -3
                                return validar
                            else:
                                hay_solo_letras = parte.isalpha()
                                if hay_solo_letras:
                                    #print("No es flotante positivo")
                                    validar = -3
                                    return validar
                                else:
                                    hay_numeros = encontrar_numeros(parte)
                                    if parte.count("-") == 1:
                                        if len(parte)- 1  == hay_numeros:
                                            si_hay_numero += 1
                                        else:
                                            #print("No es flotante positivo")
                                            validar = -3
                                            return validar
                                    else:
                                        if len(parte)  == hay_numeros:
                                            si_hay_numero += 1
                                        else:
                                            #print("No es flotante positivo")
                                            validar = -3
                                            return validar
                        if len(partir) == si_hay_numero:
                            #print("No es flotante positivo")
                            validar = -2
                            return validar
                        else:
                            #print("No es flotante positivo")
                            validar = -3
                            return validar
                    else:
                        #print("No es flotante positivo")
                        validar = -3
                        return validar
                #print("No es flotante positivo")
                validar = -3
                return validar
            #print("No es flotante positivo")
            validar = -3
            return validar 

def sanitizar_string(valor_str: str, valor_por_defecto: str = "-")->bool:
    '''
    Brief: Convierte un string todo a minusculas. 
    Parameters:
            valor_str: un string que puede tener numeros o caracteres fuera del alfabeto
            valor_por_defecto: un "-" que en el caso de estar convierte al string directamente. 
    return: retorna un booleano que indica si se pudo convertir o no.  
    '''
    if (valor_str == " " or valor_str == "") and valor_por_defecto != "-":
        convertir = valor_por_defecto.lower()
        #print(convertir)
        sanitizar = True
    else:
        caracter_sin_espacios = valor_str.strip()
        if caracter_sin_espacios.isalpha():
            convertir = caracter_sin_espacios.lower()
            #print(convertir)
            sanitizar = True
        else:
            cantidad_de_numeros = encontrar_numeros(valor_str)
            if cantidad_de_numeros > 0:
                #print("N/A")
                sanitizar = False
            elif caracter_sin_espacios.count("/") > 0:
                partir = caracter_sin_espacios.split("/")
                letra  = 0
                for parte in partir:
                    cambio = parte.replace(" ", "a")
                    if cambio.isalpha():
                        letra += 1
                if letra == len(partir):
                    caracter_sin_espacios = caracter_sin_espacios.replace("/", " ")
                    convertir = caracter_sin_espacios.lower()
                    #print(convertir)
                    sanitizar = True
                else:
                    #print("carcteres no validos")
                    sanitizar = False
            else:
                
                if valor_str == " " or valor_str == "":
                    #print("Vacio")
                    sanitizar = True
                else:
                    convertir_sin_espacios = caracter_sin_espacios.replace(" ", "a")
                    if convertir_sin_espacios.isalpha():
                        convertir = caracter_sin_espacios.lower()
                        #print(convertir)
                        sanitizar = True
                    else:
                        #print("carcteres no validos")
                        sanitizar = False
    return sanitizar 

def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str)->bool:
    '''
    Brief: convierte el value, de la key, del diccionario ingresado, en el tipo de dato que se ingrese.  
    Parameters:
            heroe: diccionario qu econtiene los datos de un superheroe. 
            clave: clave valida que pertenece al diccionario antes mencionado.
            tipo_de_dato: tipo de dato al que se quiere convertir lo que se encuentra en el value de la clave antes mencionada. 
    return: retorna un booleano que indica si se pudo convertir o no, al tipo de dato ingresado.  
    '''
    clave_existe = False
    sanitizar = False
    lista_de_claves = []
    for super in heroe:
        lista_de_claves.append(super)
    for clave_en_lista in lista_de_claves:
        if clave == clave_en_lista:
            clave_existe = True
    if clave_existe == False:
        print("La clave especificada no existe en el héroe.")
    else:
        tipo_dato = tipo_dato.lower()
        match tipo_dato:
            case "string":
                sanitizar = sanitizar_string(heroe[clave])
            case "entero":
                validar = sanitizar_entero(heroe[clave])
                if validar != -1 and validar != -2 and validar != -3:
                    #print(validar)
                    sanitizar = True
            case "flotante":
                validar = sanitizar_flotante(heroe[clave])
                if validar != -1 and validar != -2 and validar != -3:
                    #print(validar)
                    sanitizar = True
            case _:
                print("Tipo de dato no reconocido")
                sanitizar = False
    return sanitizar

def stark_normalizar_datos(lista:list):
    '''
    Brief: convierte los datos de los diccionarios de una lista, al tipo de dato que corresponde. 
    Parameters:
            Lista: lista de superheroes. 
    return: no retorna, muestra si se pudieron o no normalizar los datos. 
    '''
    validacion = False
    if len(lista) != 0:
        lista_claves = ['altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia']
        #lista_tipo_dato = ['string', 'entero','flotante']
        for super_heroe in lista:
            #print(super_heroe)
            for clave in lista_claves:
                if clave == 'altura'or  clave == 'peso':
                    validacion = sanitizar_dato(super_heroe, clave, 'flotante')
                elif clave == 'fuerza':
                    validacion = sanitizar_dato(super_heroe, clave, 'entero')
                else:
                    validacion = sanitizar_dato(super_heroe, clave, 'string')
        if validacion:
            print("datos normalizados")
        else:
            print("no se pudieron noralizar todos los datos")

def generar_indice_nombres(lista:list)->list:
    '''
    Brief: Crea una lista de nombres. 
    Parameters:
            lista: lista de superheroes. 
    return: retorna una lista con nombres. 
    '''
    if len(lista) > 0:
        lista_nombres = []
        for super_heroe in lista:
            tipo_de_dato = type(super_heroe)
            if tipo_de_dato == dict:
                nombre = super_heroe['nombre']
                nombre = nombre.strip()
                if nombre != " ":
                    if nombre.count(" ")>0:
                        partir = nombre.split(" ")
                        for parte in partir :
                            lista_nombres.append(parte)
                    elif nombre.count("-")>0:
                        partir = nombre.split("-")
                        for parte in partir :
                            lista_nombres.append(parte)
                    else:
                        lista_nombres.append(nombre)
        #print(lista_nombres)
    else:
        print("El origen de datos no contiene el formato correcto")
    return lista_nombres

def stark_imprimir_indice_nombre(lista:list):
    '''
    Brief: imprime una lista con nombres seguidos de sus iniciales. 
    Parameters:
            lista: lista de superheroes. 
    return:no retorna, muetsra la lista de nombres con iniciales. 
    '''
    lista_nombres = generar_indice_nombres(lista)
    elementos_en_lista = len(lista_nombres)
    for indice in range(elementos_en_lista):
        print (f"{lista_nombres[indice]}", end= "-")
    print("")

def convertir_cm_a_mtrs(valor_cm:float)-> float:
    '''
    Brief: Convierte un numero que esta en cm a metros. 
    Parameters:
            valor_cm: numero en cm a convertir. 
    return: retorna el numero convertido a metros.  
    '''
    validar = sanitizar_flotante(valor_cm)
    if validar != -1 and validar != -3 and validar != -2:
        cambio_de_unidad = validar / 100
    else:
        cambio_de_unidad = -1
    return cambio_de_unidad

def generar_separador(patron:str, largo:int, imprimir:bool = True):
    '''
    Brief: genera un separador de las dimenciones dadas. 
    Parameters:
            patron: aquello que va a funcionar de separador.
            largo: cantidad de veces que se debera repetir ese patron. 
            imprimir: parametro opcional que me indicara si se imprimira o no el patron. 
    return: no retorna, muestra el patron generado. 
    '''
    if len(patron) > 0 and len(patron) < 3:
        if largo != -1 and largo != -2 and largo != -3:
            if largo > 0 and largo <= 235:
                if imprimir:
                    print(imprimir)
                for patro in  range(largo):
                    print(patron, end = " ")
            else:
                print("N/A")
        else:
            print("N/A")
    else:
        print("N/A")

def generar_encabezado(titulo:str):
    '''
    Brief: genera un encabezado a partir de un titulo dado y utilizar la funcion generar_patron. 
    Parameters:
            titulo: titulo del encabezado.  
    return: no retorna, muestra el encabezado generado. 
    '''
    titulo_mayuscula = titulo.upper()
    generar_separador("*", 30, False)
    print(f"\n{titulo_mayuscula}")
    generar_separador("*", 30, False)

def imprimir_ficha_heroe(heroe:dict):
    '''
    Brief: imprime los datos de cada heroe por separado en fichas. 
    Parameters:
            heroe: diccionario que contiene los datos de unheroe. 
    return: no retorna, muestra las fichas. 
    '''
    # stark_generar_codigos_heroes(lista_personajes)
    lista_titulos = [
        "NOMBRE DEL HÉROE:","IDENTIDAD SECRETA:","CONSULTORA:","CÓDIGO DE HÉROE :",
        "ALTURA:", "PESO:", "FUERZA:",
        "COLOR DE OJOS:", "COLOR DE PELO:"
        ]
    
    generar_encabezado("principal")
    print(f"\n{ lista_titulos[0]}", end = " ")
    print(heroe['nombre'])
    print(f"\n{ lista_titulos[1]}", end = " ")
    print(heroe['identidad'])
    print(f"\n{ lista_titulos[2]}", end = " ")
    print(heroe['empresa'])
    print(f"\n{ lista_titulos[3]}", end = " ")
    print(f"{heroe['codigo heroe']} \n")

    generar_encabezado("fisico")
    numero_convertido = convertir_cm_a_mtrs(heroe['altura'])
    print(f"\n{ lista_titulos[4]}", end = " ")
    print(f"{numero_convertido} Mts")
    print(f"\n{ lista_titulos[5]}", end = " ")
    print(f"{heroe['peso']} Kgs")
    print(f"\n{ lista_titulos[6]}", end = " ")
    print(f"{heroe['fuerza']} N\n")

    generar_encabezado("señas particulares")
    print(f"\n{ lista_titulos[7]}", end = " ")
    print(f"{heroe['color_ojos']}")
    print(f"\n{ lista_titulos[8]}", end = " ")
    print(heroe['color_pelo'])

def stark_navegar_fichas(lista:list):
    '''
    Brief: muestra las fichas una a una de forma secuencial, pudiendo ir para atras o para delante. 
    Parameters:
            lista: lista de superheroes. 
    return: no retorna, muestra la ficha que corresponda. 
    '''
    stark_generar_codigos_heroes(lista)
    imprimir_ficha_heroe(lista[0])
    nuevo_indice = 0
    seguir = True
    while seguir:
        print("\n[ 1 ] Ir a la izquierda  [ 2 ] Ir a la derecha   [ S ] Salir")
        rta = input("Ingrese una opcion:")
        match rta:
            case "1":
                nuevo_indice -= 1
                if nuevo_indice == -1: 
                    mostrar = lista[len(lista)-1]
                    imprimir_ficha_heroe(mostrar)
                    nuevo_indice = len(lista)-1
                else:
                    mostrar = lista[nuevo_indice]
                    imprimir_ficha_heroe(mostrar)
            case "2":
                nuevo_indice  += 1
                if nuevo_indice == (len(lista)):
                    mostrar = lista[0]
                    imprimir_ficha_heroe(mostrar)
                    nuevo_indice = 0
                else:
                    mostrar = lista[nuevo_indice]
                    imprimir_ficha_heroe(mostrar)
            case "s":
                seguir = False

lista_opciones = [
    "1 - Imprimir la lista de nombres junto con sus iniciales",
    "2 - Generar códigos de héroes",
    "3 - Normalizar datos",
    "4 - Imprimir índice de nombres",
    "5 - Navegar fichas",
    "S - Salir",
]

def imprimir_menu():
    '''
    Brief: imprime el menu de opciones.  
    Parameters: no recibe parametros 
    return: no retorna, muestra el menu de opciones. 
    '''
    for opcion in lista_opciones:
        print(f"{opcion}")

def stark_menu_principal():
    '''
    Brief: le pide al usuario que seleccione una opcion del menu.   
    Parameters: no recibe parametros 
    return: retorna la opcion ingresada por el usuario. 
    '''
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    return opcion

def stark_marvel_app_3(lista: list):
    '''
    Brief: Llama a las funciones correspondientes de acuerdo con lo que el usuario solicita.  
    Parameters: 
            lista: lista de superheroes. 
    return: no retorna, muestra aquello que pide el usuario. 
    '''
    seguir = True
    while seguir:
        opcion = stark_menu_principal()
        match opcion:
                case "1":
                    stark_imprimir_nombres_con_iniciales(lista)
                case "2":
                    stark_generar_codigos_heroes(lista)
                case "3":
                    stark_normalizar_datos(lista)
                case "4":
                    stark_imprimir_indice_nombre(lista)
                case "5":
                    stark_navegar_fichas(lista)
                case "s":
                    seguir = False
                case _:
                    print("Opcion no valida")
    print("¡Gracias ppor utilizar Stark_marvel_app_3!")

system("cls")
stark_marvel_app_3(lista_personajes)