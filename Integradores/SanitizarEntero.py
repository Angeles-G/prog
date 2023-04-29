def sanitizar_entero (numero_str:str)->int:
    num = numero_str.strip() #Saco los espacios en blanco de adelante y atrás
    num = num.replace(" ", "") #Saco todos los espacios del medio

    if num.isalpha():
            print("Sólo Texto") #Todos los caracteres son letras
            return -1
    else:
        if num.isnumeric():
            print("Número") #Todos los caracteres son números
            num = int(num)
            print(f"El tipo de dato es: {type(num)}")
            return num
        else:            
            try:
                int(num)
                print("Número Negativo") #Es un número no positivo distinto de 0
                return -2
            except:
                print("Alfanumerico") #Es un cadena alfanumerica
                return -3

print(sanitizar_entero('123'))
