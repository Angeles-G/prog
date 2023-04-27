'''
Angeles Belen Garcia - 1B
Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
de memoria es la que mas ocurrencias tiene dentro de esa lista.
'''
seguir = True
lista_numero = []
mayor = 0
while seguir:
    numero_ingresado = int(input("Ingrese un numero: "))
    lista_numero.append(numero_ingresado)
    rta = input("¿Desea ingresar mas numeros?")
    if rta != "si": 
        seguir = False

for numero in lista_numero:
    repeticiones = lista_numero.count(numero)
    if  repeticiones > mayor:
        mayor = repeticiones
        numero_mas_repetido = numero

for numero_repetido in lista_numero:
    if  numero_repetido == numero_mas_repetido:
        indice_del_repetido = lista_numero.index(numero_repetido)
    break

print(f"El numero mas repetido es {numero_mas_repetido} y la primera ocurrencia se encuentra en la posicion {indice_del_repetido}")
