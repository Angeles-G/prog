from os import system
from data_stark import lista_personajes

#Recorrer la lista y determinar cuál es el superhéroe más alto de género M
#Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def encontrar_maximo(lista:list, clave:str):
    flag_primero = True
    if (type(lista) == list and len(lista) >0 and type(clave)== str and clave != ""):
        for super in lista:
            if (flag_primero == True or float(super['altura']) > maximo) and super['genero'] == clave:
                maximo = float(super['altura'])
                flag_primero = False
    return maximo
#Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
#Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
def listar_por_genero(lista:list, clave: str, maximo = None, minimo = None):
    if maximo is None and minimo is None:
        for super in lista:
            if super['genero'] == clave:
                print(super['nombre'])
    elif minimo is None:
        for altura in lista:
            if float(altura['altura']) == maximo and altura['genero'] == clave:
                maximo_nombre = altura['nombre']
                print(maximo_nombre)
    else:
        for altura in lista:
            if float(altura['altura']) == minimo and altura['genero'] == clave:
                minimo_nombre = altura['nombre']
                print(minimo_nombre)
def encontrar_mas_alto(lista:list, clave:str):
    maximo = encontrar_maximo(lista, clave)
    print(f"La altura maxima de los {clave} es {maximo}: ")
    listar_por_genero(lista, clave, maximo = maximo)
#Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
#Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
def encontrar_minimo(lista:list, clave:str):
    flag_primero = True
    if (type(lista) == list and len(lista) >0 and type(clave)== str and clave != ""):
        for super in lista:
            if (flag_primero == True or float(super['altura']) < minimo) and super['genero'] == clave:
                minimo = float(super['altura'])
                flag_primero = False
    return minimo
def encontrar_mas_bajo(lista:list, clave: str):
    minimo = encontrar_minimo(lista,clave )
    print(f"La altura minima de los {clave} es {minimo}: ")
    listar_por_genero(lista, clave, minimo = minimo)
#Recorrer la lista y determinar la altura promedio de los superhéroes de género M
# Recorrer la lista y determinar la altura promedio de los superhéroes de género F
def calcular_promedio(lista:list, clave:str):
    acumulador_alturas = 0
    contador_personajes = 0
    for altura in lista:
        if altura['genero'] == clave:
            acumulador_alturas += float(altura['altura'])
            contador_personajes += 1
    promedio_altura = acumulador_alturas / contador_personajes
    return promedio_altura
def buscar_promedio_altura(lista:list, clave:str):
    promedio_altura = calcular_promedio(lista,clave)
    print(f"La altura promedio de los personajes {clave} es de {promedio_altura}")
#Determinar cuántos superhéroes tienen cada tipo de color de ojos.
#Determinar cuántos superhéroes tienen cada tipo de color de pelo.
#Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
def encontrar_valores(lista:list, clave:str):
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
#Listar todos los superhéroes agrupados por color de pelo.
#Listar todos los superhéroes agrupados por color de ojos
#Listar todos los superhéroes agrupados por tipo de inteligencia.
def listar_valores(lista:list, clave:str):
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

def mostrar_opciones():
    for opcion in lista_opciones:
        print(opcion)

system("cls")
#Ordenar el código implementando una función para cada uno de los valores informados.
#Construir un menú que permita elegir qué dato obtener
while True:
    print(".................................")
    mostrar_opciones()
    respuesta = int(input("Elija una opcion: "))
    match respuesta:
        case 1:
            print(".................................")
            listar_por_genero(lista_personajes, "M")
        case 2:
            print(".................................")
            listar_por_genero(lista_personajes, "F")
        case 3:
            print(".................................")
            encontrar_mas_alto(lista_personajes, "M")
        case 4:
            print(".................................")
            encontrar_mas_alto(lista_personajes, "F")
        case 5:
            print(".................................")
            encontrar_mas_bajo(lista_personajes, "M")
        case 6:
            print(".................................")
            encontrar_mas_bajo(lista_personajes, "F")
        case 7:
            print(".................................")
            buscar_promedio_altura(lista_personajes, "M")
        case 8:
            print(".................................")
            buscar_promedio_altura(lista_personajes, "F")
        case 9:
            print(".................................")
            mostrar_valores_cantidades(lista_personajes, "color_ojos")
        case 10:
            print(".................................")
            mostrar_valores_cantidades(lista_personajes, "color_pelo")
        case 11:
            print(".................................")
            mostrar_valores_cantidades(lista_personajes, "inteligencia")
        case 12:
            print(".................................")
            listar_valores(lista_personajes, "color_ojos")
        case 13:
            print(".................................")
            listar_valores(lista_personajes, "color_pelo")
        case 14:
            print(".................................")
            listar_valores(lista_personajes, "inteligencia")
        case 15:
            break