#Angeles Belen Garcia 

#CALCULADORA SENCILLA: 

def sumar_numeros(primer_numero:int, segundo_numero:int)-> int: 
    suma_numeros = primer_numero + segundo_numero
    return suma_numeros 

def restar_numeros(primer_numero:int, segundo_numero:int)-> float: # --> retorna implementacion de la funcion 
    resta_numeros = primer_numero - segundo_numero
    return resta_numeros #el valor fuera de la funcion existe 

#                      (  parametros formales de la funcion  )
def multiplicar_numeros(primer_numero:int, segundo_numero:int)->float:
    multiplicacion = primer_numero * segundo_numero
    return multiplicacion

def dividir_numeros(primer_numero:int, segundo_numero:int):
    divicion = None
    if segundo_numero != 0:
        divicion = primer_numero / segundo_numero
    return divicion 


bandera_ingreso = False
while True:
    opcion = int(input("1. Ingresar numeros\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Sumar\n6. salir\n Ingrese una opcion: "))
    match opcion:
        case 1:
            x = int(input("Ingrese un numero "))
            y = int(input("Ingrese un numero "))
            bandera_ingreso = True
        case 2:
            if bandera_ingreso: 
                resultado = restar_numeros(x, y)
                print (f"El resultado de la resta es {resultado}")
            else: 
                print("No se ingresaron los numeros ")
        case 3:
            if bandera_ingreso: 
                resultado = multiplicar_numeros(x, y)
                print (f"El resultado de la multiplicacion es {resultado}")
            else: 
                print("No se ingresaron los numeros ")
        case 4:
            if bandera_ingreso: 
                resultado = dividir_numeros(x, y)
                if resultado != None:
                    print (f"El resultado de la divicion es {resultado}")
                else:
                    print("Error no se puede dividir por 0")
            else:
                print("No se ingresaron los numeros ")
        case 5:
            if bandera_ingreso: 
                resultado = sumar_numeros(x, y)
                print (f"El resultado de la suma es {resultado}")
            else:
                print("No se ingresaron los numeros ")
        case 6: 
            break




