'''
Ángeles Belén García - 1 B - Turno mañana 
Ejercicio 02
Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
al ingresar el número debemos mostrarle que regla de estilo representa y su
descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
“Error, regla de estilo inexistente”
'''
print("Reglas de estilo")

numero_regla = int(input("Ingrese un numero entre 1 y 8 "))

while numero_regla < 1 or numero_regla > 8: 
    print("Numero de regla inexistente")
    numero_regla = int(input("Ingrese un numero entre 1 y 8 "))

if numero_regla == 1: 
    print("¿Cual es el sentido? ")
    print("Según Guido van Rossum, el código es leído más veces que escrito,\npor lo que resulta importante escribir código que no sólo funcione,\nsino que además pueda ser leído con facilidad.")
else:
    if numero_regla == 2:
        print("¿Que es PEP? ")
        print("Python Enhancement Proposal es un documento que proporciona información\na la comunidad de Python, o que describe una nueva característica")
    else:
        if numero_regla == 3:
            print("Identado: ")
            print("Python no usa corchetes para designar bloques de código como\notros lenguajes de programación, sino que usa bloques identados\npara indicar que un determinado bloque de código pertenece a por ejemplo un if.")
        else:
            if numero_regla == 4:
                print("Tamaño de lineas: ")
                print("Se recomienda limitar el tamaño de cada línea a 79 caracteres,\npara evitar tener que hacer scroll a la derecha.")
            else:
                if numero_regla == 5:
                    print("Espacios en blanco: ")
                    print("El uso de espacios en blanco mejora la legibilidad del código,\ny es por lo que la PEP8 indica dónde debemos usar espacios y dónde no.")
                else:
                    if numero_regla == 6:
                        print("Comentarios: ")
                        print("Cualquier comentario que contradiga el código es \npeor que ningún comentario. Si actualizamos el código, \nse debe actualizar los comentarios para evitar crear inconsistencias")
                    else:
                        if numero_regla == 7:
                            print("Nombres: ")
                            print("Funciones: Uso de snake_case, letras en minúscula separadas por guión bajo: mi_funcion.")
                            print("Variables: Al igual que las funciones: variable, mi_variable.") 
                            print("Clases: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba.")
                            print("Métodos: Al igual que las funciones, usar snake case: metodo, mi_metodo.")
                            print("Constantes: Nombrarlas usando mayúsculas y separadas por guión bajas: UNA_CONSTANTE")
                            print("Módulos: Igual que las funciones: modulo.py, mi_modulo.py.")
                        else:
                            if numero_regla == 8:
                                print("Encoding: ")
                                print("Los archivos se codifican por defecto en ASCII para Python 2 \ny UTF-8 para Python 3, por lo que será necesario definir la \ncodificación que usemos cuando pretendamos usar otro tipo.")





