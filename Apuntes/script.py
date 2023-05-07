print ("Vamos a aprender Python!!!")
nombre = "Jose"
edad = 20
nombre_paciente = "pedro"
bandera_maximo = True

contador = 0

contador = contador +1
contador += 1

if nombre == "Juan" and edad > 20:
    print("Bienvenido Juan")
else:
    if nombre == "Maria":
        print("Bienvenida Maria")
        print("Gracias por utilizar nuestro sistema")
    else:
        if nombre == "Jose":
            print("Bienvenido Jose")
        else: 
            print("Usted no se llama Juan, Maria, ni Jose")
#-----------------------------------------------------------
color = "azul"
if color == "azul":
    print("Es azul")
if color == "verde":
    print("Es verde")
if color == "amarillo":
    print("Es amarillo")
if color == "rojo":
    print("Es rojo")
if color != "rojo" and color != "amarillo" and color != "verde" and color != "azul":
    print("Es otro color")
#----------------------------
if color == "azul":
    print("Es azul")
else:
    if color == "verde":
        print("Es verde")
    else:
        if color == "amarillo":
            print("Es amarillo")
        else:
            if color == "rojo":
                print("Es rojo")
            else:
                print("Es otro color")
#-----------------------------
color = "azul"
if color == "azul":
    print("Es azul")
elif color == "verde":
        print("Es verde")
elif color == "amarillo":
            print("Es amarillo")
elif color == "rojo":
    print("Es rojo")
else:
    print("Es otro color")
#------------------------------
contador = 0
seguir = True
acumulador = 0
while seguir:
    numero = int(input("Ingrese un numero: "))
    acumulador += numero
    seguir = input("¿Desea seguir? si / no")
    if seguir != "si":
        seguir = False
print(f"El acumulado es {acumulador}")
#-------------------------------------
contador = 0
seguir = True
acumulador = 0
while seguir:
    numero = int(input("Ingrese un numero: "))
    acumulador += numero
    seguir = input("¿Desea seguir?")
    if seguir != "si":
        break
print(f"El acumulado es {acumulador}")
#----------------------------
acumulador = 0
for x in range(5): #El cinco dice la cantidad de veces que quiero que itere. comienza en 0
    numero = int(input("Ingrese el {x}° numero: "))
    acumulador += numero
print(f"acumulado: {acumulador}")
#------------------------------
lista_nombre = {"luis", "nicolas", "federico","micaela" ,"silvina"}
for nombre in lista_nombre:#foreach
    print(nombre)
#------------------------------
lista_nombre = ["luis", "nicolas", "federico","micaela" ,"silvina"]
lista_nombre.reverse()
for nombre in lista_nombre:#foreachreverse
    print(nombre)
#-----------------------------
lista_nombre = ["luis", "nicolas", "federico","micaela" ,"silvina"]
lista_nombre.reverse()
for nombre in lista_nombre:#foreachreverse
    if nombre == "federico":
        continue #no va a mostrar a federico
    print(nombre)
#-----------------------------
color = "azul"
match color:
    case "azul":
        print("Es azul")
    case "verde":
        print("Es verde")
    case "amarillo":
        print("Es amarillo")
    case "rojo": 
        print("Es rojo")
    case _: # case other: 
        print("Es otro color")
#----------------------------
#Listas:
lista = [1,2,3,4,5,6,7,8,9,5,5,5]
print(lista)
print(f"Elemento 3: {lista[3]}") # 4
print(lista[0:3]) # DESDE : HASTA ---> Desde = INCLUSIVO / hasta = EXCLUSIVO
print(lista[3:5])# 4, 5

l = range(10)
print(l) #rango del 0 al 9 

acumulador = 0 
contador = 0
for i in range(len(lista)): # len = cantidad de elemento de la lista 
    acumulador = acumulador + lista[i]
    if(lista[i] == 5):
        contador += 1

print(acumulador)
print(contador)

lista.appened(100) # 100 = elemento que se agrega a la lista 
print(lista)

lista.insert(2,999) # 2 = posicion / 999 = dato a guardar en esa posicion y lo que habia antes en esa pocicion lo corre uno 
print(lista)

lista.extend([999,888,777]) #agrega esta sublista al final de la lista anterior
print(lista)

lista.remove(8) # 8 = dato a borrar dentro de la lista. Lo elimina la primera vez que aparece
print(lista)

print(lista.index(999))# me muestra el indice de la primera vez que aparece el 999

for numero in lista: # para cada numero que este en la lista voy hacer...
    print(numero)

#---------------------------
#Diccionarios
mi_diccionario = {}
print(type(mi_diccionario)) # <class = ´dic'>

mi_diccionario ['Nombre '] = 'Juan'
print(mi_diccionario["Nombre "])

mi_diccionario ["Edad "] =  25
print(mi_diccionario["Edad "])

print(mi_diccionario)

otro_diccionario = {"Nombre " : "Luis", "Edad " : 32}
print(otro_diccionario)

for key in otro_diccionario: #por cada clave del diccionario hacer.....
    print(f"{otro_diccionario[key]}") # muestra el dato referente a la clave

for valor in otro_diccionario.values: # toma solo los valores 
    print(f"{valor}") 

#------------------------------
#Listas paralelas
cantidad_alumnos = 3
lista_nombres = []
lista_apellidos = []

for i in range(cantidad_alumnos):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apaellido: ")
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)

for i in range(cantidad_alumnos):
    print(f"{i+1}) Nombre: {lista_nombres[i]} - Apellido: {lista_apellidos[i]}")

#----------------------------------

#lista_alumnos = [{"Nombre: " : "Juan", "Edad: ": 25},
#               {"Nombre: " : "Luis", "Edad: ": 36}, #Lista Harcodeada
#               {"Nombre: " : "Maria", "Edad: ": 23}]

lista_alumnos = [] #Lista

for i in range(3):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = int(input("Ingrese edad: "))
    un_alumno = {} #Diccionario
    un_alumno["Nombre"] = nombre
    un_alumno["Apellido"] = apellido
    un_alumno["Edad"] = edad
    lista_alumnos.append(un_alumno) # Meto en la lista un diccionario

print(lista_alumnos)

for alumno in lista_alumnos:
    apellido = alumno["Apellido"]
    nombre =  alumno["Nombre"]
    edad = alumno["Edad"]
    if edad > 30 : 
        print(f"{apellido},{nombre},{edad}")

for alumno in lista_alumnos:
    edad = alumno["Edad"]
    if edad > 30 : 
        print(f"{alumno['Apellido']},{alumno['Nombre']},{alumno['Edad']}")

#-----------------------------------------
heroes_info = [

{
"Nombre":"Super Girl",
"ID": 1,
"Origen":"Krypton ",
"Habilidades  ": ["Volar","Fuerza ","Velocidad","Volar","Fuerza","Velocidad"],
"Identidad":"Kara Zor-El"
},
{
"Nombre":"Shazam",
"ID": 25,
"Origen":"Tierra",
"Habilidades": ["Volar","Fuerza ","Velocidad","Magia","Fuerza","Velocidad"],
"Identidad":"Billy Batson",
},
{
"Nombre":"Power Girl  ",
"ID": 14,
"Origen":"Krypton ",
"Habilidades": ["Volar","Fuerza ","Congelar","Congelar", "Congelar "],
"Identidad":"Karen Starr"
},
{
"Nombre":"Wonder Woman",
"ID": 29,
"Origen":"Amazonia",
"Habilidades": ["Agilidad ","Fuerza", "Lazo de la verdad","Escudo"],
"Identidad":"Diana Prince"
}
]
#......................................
mi_lista = []
mi_lista.append(78)
mi_lista.append(3)
mi_lista.append(4)
mi_lista.append(6)
mi_lista.append(2)
for i in range(len(mi_lista)): #Recorrer y consultar la lista por indice
    print(mi_lista[i])
#...................................
for numero in mi_lista :
    print(numero) #Recorro la lista con una variable contextual, 
    #la variable de control toma uno a uno los datos de la lista
#....................................
#Eliminar un elemento 
mi_lista.remove(2) #Remueve un elemento de la lista el numero "2"
print(mi_lista)#(78,3,4,6)
#....................................
#Tuplas
mi_tupla = (3,6,8,9) #Es inmutable no se puede cambiar elementos ni eleminarlos }
#............................................
#SET 
#Toma como badse otra coleccion y elimina los duplicados
mi_set = set([3,4,6,4,2,3,7,8,1])
print(mi_set)
#.........................................................
#Diccionarios
mi_diccionario =  {"codigo": 5, "descripcion":"Coca cola"}
print(mi_diccionario)
mi_diccionario ["codigo"] = 5
mi_diccionario ["descripcion"] = "Coca cola"
for clave in mi_diccionario:
    print(f"{clave} : {mi_diccionario[clave]}")
#............................................
lista_diccionarios = []

producto1 = {"codigo": 5, "Descripcion": "Pepsi", "precio": 400}
producto2 = {"codigo": 3, "Descripcion": "Fanta", "precio": 200}
producto3 = {"codigo":1, "Descripcion": "Coca", "precio": 900}

lista_diccionarios.append(producto1)
lista_diccionarios.append(producto2)
lista_diccionarios.append(producto3)

print(lista_diccionarios)

#.................................
lista_diccionarios = []

producto1 = {"codigo": 5, "Descripcion": "Pepsi", "precio": 400}
producto2 = {"codigo": 3, "Descripcion": "Fanta", "precio": 200}
producto3 = {"codigo":1, "Descripcion": "Coca", "precio": 900}

lista_diccionarios [producto1,producto2, producto3]
#.....................................................
#lista_diccionarios = [{"codigo": 5, "Descripcion": "Pepsi", "precio": 400}
#                      {"codigo": 3, "Descripcion": "Fanta", "precio": 200}
#                      {"codigo":1, "Descripcion": "Coca", "precio": 900}
#]
#.............................................................................
lista_productos = []
CANTIDAD = 3
for i in range(CANTIDAD):
    codigo = int(input("Ingrese el codigo: "))
    descripcion = input("Ingrese la descripcion: ")
    precio =  float(input("Ingrese el precio: "))
    un_producto = {}
    un_producto ["Codigo"] =  codigo
    un_producto ["Descripcion"] = descripcion
    un_producto ["Precio"] = precio
    lista_productos.append (un_producto)

for producto in lista_productos:
    print(f"{producto['Codigo']}, {producto['Descripcion']}, {producto['Precio']}")

#.........................................................
# from os import system
# #from data import lista_bzrp

# menu = ["1. mostar tema","2. mostrar temas con vistas",
#         "3. Mostrar temas mas vistos", "4. Mostrar temas menos vistos", 
#         "5. Mostrar el promedio de reproducciones", "6. Salir"]

# system("cls")

# while True: 
#     print(".................................")
#     for opcion in menu:
#         print(opcion)
#     respuesta = int(input("Elija una opción: "))
#     match respuesta:
#         case 1: #B. Recorrer la lista imprimiendo por consola el título de cada video
#             #FOREACH:
#             for tema in lista_bzrp:
#                 print(f"{tema['title']}")
#         case 2: #C. Recorrer la lista imprimiendo por consola el título de cada video junto a la cantidad de reproducciones del mismo
#             for tema in lista_bzrp:
#                 print(f"{tema['title']}, - {tema['views']}")
#         case 3: #Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones (MÁXIMO)
#             flag_primero = True
#             #maxima_view = lista_bzrp [0]['views']
#             for tema in lista_bzrp:
#                 if flag_primero == True or tema['views'] > maxima_view:
#                     maxima_view = tema['views']
#                     flag_primero = False
#             print(f"Cantidad maxima de reproduccion: {maxima_view}")
#             for tema in lista_bzrp:
#                 if tema['views'] == maxima_view:
#                     print(f"{tema['title']}")
#         case 4: #E. Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones (MÍNIMO)
#             flag_primero = True
#             for tema in lista_bzrp:
#                 if flag_primero == True or tema['views'] < minima_views:
#                     minima_views = tema['views']
#                     flag_primero = False
#             print(f"Cantidad minima de reproduccion: {minima_views}")
#             for tema in lista_bzrp:
#                 if tema['views'] == minima_views:
#                     print(f"{tema['title']}")
#         case 5:#G.Recorrer la lista y determinar la cantidad promedio de reproducciones que tiene un video (PROMEDIO)
#             acumulador_views = 0
#             for tema in lista_bzrp:
#                 acumulador_views += tema['views']
#             print(f"Sumatoria de reproducciones: {acumulador_views}")
#             contador_tema = len(lista_bzrp)
#             # for tema in lista_bzrp:
#             #     contador_tema += 1
#             promedio_views = acumulador_views / contador_tema
#             print(f"El promedio de vistas es {promedio_views}")
#         case 6:
#             break

#.........................................................

#ARGUMENTO POR NOMBRE 
def potenciar(base, exponente):
    return base ** exponente

base = 2
exponente = 3

resultado = potenciar(base, exponente)
print(resultado)
resultado = potenciar(base = base, exponente=exponente)
print(resultado)

#ARGUMENTO OPCIONAL 
def potenciar(base, exponente = 2):
    return base ** exponente

base = 2
exponente = 3

resultado = potenciar(base)
print(resultado)
resultado = potenciar(base = base, exponente=exponente)
print(resultado)

#--------------------------------------
mi_cadena = "python, JS, java, C"

#............................................
#REGEX: EXPPRECIONES REGULARES