#Angeles Belen García - 1B - Turno mañana 

tipo = str(input("Ingrese un producto de prevención de contagio: barbijo, jabon o alcohol"))
while tipo != "barbijo" and tipo !="jabon" and tipo != "alcohol":
    tipo = str(input("Error-Ingrese un producto de prevención de contagio: barbijo, jabon o alcohol"))  
precio = float (input("Ingrese el precio del producto por unidad"))
while precio <100 or precio >1000:
    precio = float (input("Error-Ingrese el precio del producto por unidad"))
cantidad_unidades = int(input("Ingrese la cantidad de unidades"))
while cantidad_unidades <1:
    cantidad_unidades = int(input("Error-Ingrese la cantidad de unidades"))
marca = str(input("Ingrese la marca del producto"))
fabricante = str(input("Ingrese el fabricante del producto"))

print("Usted compro "+ tipo + " de la marca "+ marca + " y fabricante "+ fabricante )
print("El precio por unidad es ", precio , " y compro ", cantidad_unidades , "unidad / es ")