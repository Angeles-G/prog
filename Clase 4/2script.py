'''
Angeles Belen Garcia
La real academia española nos pide desarrollar un pequeño programa que contenta el
diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
algoritmo que nos permita el ingreso de una palabra en español y su traducción al
ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
inglés. Recordar validar los datos de forma correcta.
'''
diccionario = []
respuesta = "si"
seguir = True
bandera = True
esta =  False

while seguir:
    español = input("Ingrese la palabra en español a traducir: ")
    ingles = input("Ingrese la palabra traducida al ingles: ")
    if bandera != True: 
        for palabra in diccionario:
            if  palabra['Español'] == español:
                print(f"La palabra ya existe es la numero {diccionario.index(palabra)+1}")
                esta = True
        if esta != True:
            lengua_traducida = {}
            lengua_traducida ['Español'] = español
            lengua_traducida ['Ingles'] = ingles
            diccionario.append(lengua_traducida)
    else:
        lengua_traducida = {}
        lengua_traducida ['Español'] = español
        lengua_traducida ['Ingles'] = ingles
        diccionario.append(lengua_traducida)
    bandera = False
    respuesta = input("¿Desea ingresar mas datos? si/no ")
    print("-------------------------------------------")
    if respuesta != "si":
        seguir = False

for palabras in diccionario:
    print(f"Español: {palabras['Español']} | Ingles: {palabras['Ingles']}")