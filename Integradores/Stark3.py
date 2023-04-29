#Angeles Belen Garcia
from os import system
from data_stark import lista_personajes

def extraer_iniciales(nombre_heroe:str):
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

def definir_iniciales_nombre(heroe:dict):
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

def agregar_iniciales_nombre(lista:list):
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
    tipo = type(lista_heroes)
    if tipo == list and len(lista_heroes)>0:
        agregar_iniciales_nombre(lista_heroes)
        for super in lista_heroes:
            nombre = super['nombre']
            iniciales = super['iniciales']
            print(f"* {nombre} ({iniciales})")

def generar_codigo_heroe (id_heroe:int, genero_heroe:str):
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

def agregar_codigo_heroe(heroe:dict, id_heroe:int):
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

def encontrar_numeros(numero_sin_espacios: str):
    cantidad_de_numeros = 0
    for numero in range(0, 10):
        numero_str = str(numero)
        if numero_sin_espacios.count(numero_str) > 0: 
            cantidad_de_numeros += numero_sin_espacios.count(numero_str)
    return cantidad_de_numeros

def sanitizar_entero(num_str:str): 
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

def sanitizar_flotante(num_str:str):
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

def sanitizar_string(valor_str: str, valor_por_defecto: str = "-"):
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

def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
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

def generar_indice_nombres(lista:list):
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
    lista_nombres = generar_indice_nombres(lista)
    elementos_en_lista = len(lista_nombres)
    for indice in range(elementos_en_lista):
        print (f"{lista_nombres[indice]}", end= "-")
    print("")

def convertir_cm_a_mtrs(valor_cm:float):
    validar = sanitizar_flotante(valor_cm)
    if validar != -1 and validar != -3 and validar != -2:
        cambio_de_unidad = validar / 100
    else:
        cambio_de_unidad = -1
    return cambio_de_unidad

def generar_separador(patron:str, largo:int, imprimir:bool = True):
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
    titulo_mayuscula = titulo.upper()
    generar_separador("*", 30, False)
    print(f"\n{titulo_mayuscula}")
    generar_separador("*", 30, False)

def imprimir_ficha_heroe(heroe:dict):
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
    stark_generar_codigos_heroes(lista)
    for heroe in lista:
        imprimir_ficha_heroe(heroe)
        nuevo_indice = 1
        break
    seguir = True
    while seguir:
        print("\n[ 1 ] Ir a la izquierda  [ 2 ] Ir a la derecha   [ S ] Salir")
        rta = input("Ingrese una opcion:")
        match rta:
            case "1":
                nuevo_indice -= 1
                if nuevo_indice == 0: 
                    mostrar = lista[len(lista)-1]
                    imprimir_ficha_heroe(mostrar)
                else:
                    mostrar = lista[nuevo_indice]
                    imprimir_ficha_heroe(mostrar)
            case "2":
                nuevo_indice  += 1
                if nuevo_indice == (len(lista)):
                    mostrar = lista[1]
                    imprimir_ficha_heroe(mostrar)
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
    for opcion in lista_opciones:
        print(f"{opcion}")

def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    return opcion

def stark_marvel_app_3(lista: list):
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