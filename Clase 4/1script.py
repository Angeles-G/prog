'''
Ángeles Belén García 
Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
listas primero, y despues usando listas y comparar la composición del código.
'''
#Sin listas: 
respuesta = "si"
seguir = True
print("Stock de autos")
while seguir:
    marca = str(input("Ingrese la marca del auto: "))
    year = int(input("Ingrese el año del auto: "))
    while year < 1970 or year >2023:
        year = int(input("Error-Ingrese el año del auto: "))
    precio = int(input("Ingrese el precio del auto: "))
    while precio < 50000:
        precio = int(input("Error-Ingrese el precio del auto: "))
    print(f"Marca: {marca}, Año: {year}, Precio: {precio} ")
    print("---------------------------------------------------")
    respuesta = input("¿Desea ingresar mas datos ? si/no \n")
    if respuesta != "si":
        seguir = False

#Con listas
respuesta = "si"
seguir = True
lista_autos = []
while seguir:
    marca = input("Ingrese la marca del auto: ")
    year = int(input("Ingrese el año del auto: "))
    while year < 1970 or year >2023:
        year = int(input("Error-Ingrese el año del auto: "))
    precio = int(input("Ingrese el precio del auto: "))
    while precio < 50000:
        precio = int(input("Error-Ingrese el precio del auto: "))
    stock_autos = {}
    stock_autos ['Marca'] = marca
    stock_autos ['Año'] = year
    stock_autos ['Precio'] = precio
    respuesta = input("¿Desea ingresar mas datos ? si/no \n")
    lista_autos.append(stock_autos)
    if respuesta != "si":
        seguir = False

print("Stock de autos")
for auto in lista_autos:
    print(f"Marca: {auto['Marca']}, Año: {auto['Año']}, Precio: {auto['Precio']}")
    print("--------------------------------------------------")

