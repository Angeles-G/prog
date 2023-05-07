#TEXTO # defecto lo abre solo lectura
# mi_archivo = open("nombre.txt", "a", encoding="utf-8")
# mi_archivo.write("\n hola mundo")
# mi_archivo.close()

# mi_archivo = open("nombre.txt", "r", encoding="utf-8")
# registro = mi_archivo.readline()
# print(registro)
# mi_archivo.close()

# mi_archivo = open("nombre.txt")
# registro = mi_archivo.readline()
# print(registro)
# registro = mi_archivo.readline()
# print(registro)
# registro = mi_archivo.readline()
# print(registro)
# registro = mi_archivo.readline()
# print(registro)
# mi_archivo.close()

# lista = ["Thiago", "Gio", "Mario", "Marian"]
# with open("lista_nombres.txt", "w") as mi_archivo:
#     for nombre in lista:
#         mi_archivo.write(f"{nombre}\n")

# mi_archivo = open("lista_nombres.txt", "r")
# lista = mi_archivo.readlines()
# #readlines me trae la lista literal
# for line in lista:
#     print(line, end="")
#muestra saltos de linea cuando no los hay porque en el archivo ya estan los saltos escritos
#por mas que pongamos el end, escribe los saltos que estan escritos en el txt

# with open("lista_nombres.txt", "r") as mi_archivo:
#     for line in mi_archivo:
#         print(line)


#CSV
# nombres = ["Thiago", "Gio", "Marian"]
# apellidos = ["Mejias", "Lucheta", "Fernandez"]
# edades = [21, 23, 24]

# with open("agenda.csv", "w") as archivo:
#     for i in range(len(nombres)):
#         registro = "{0},{1},{2}\n".format(nombres[i],apellidos[i], edades[i])
#         archivo.write(registro)
# import re
# with open("agenda.csv", "r") as archivo:
#     for line in archivo:
#         registro = re.split(r",|\n",line)
#         print(f"{registro[0]}-{registro[1]}-{registro[2]}")

#JSON
# import json

# data = {}
# data["alumnos"] = []
# data["alumnos"].append({"nombre":"Juan", "Edad": 20})
# data["alumnos"].append({"nombre":"Luis", "Edad": 29})
# data["alumnos"].append({"nombre":"Maria", "Edad": 32})


# with open("agenda.json", "w") as mi_archivo:
#     json.dump(data, mi_archivo, indent = 4)

# with open("agenda.json", "r") as mi_archivo:
#     data =  json.load(mi_archivo)

# print(data)
import re 
from data import lista_bzrp
# archivo = open("agendita.json", "r")
# print(archivo)

def parser_csv(path:str)->list:
    lista = []
    archivo = open(path, "r", encoding = "utf-8")
    for line in archivo:
        lectura = re.split(r",|\n", line)
        tema = {}
        tema ["title"] = lectura[0]
        tema ["views"] = lectura[1]
        tema ["length"] = lectura[2]
        tema ["img_url"] = lectura[3]
        tema["url"] = lectura[4]
        tema["date"] = lectura[5]
        lista.append(tema)
    archivo.close()
    return lista

def generar_csv(path:str, lista:list):
    archivo = open(path, "w", encoding= "utf-8")
    for tema in lista:
        registro = "{0},{1},{2},{3},{4},{5} \n"
        registro = registro.format(tema["title"], tema["views"], tema["length"], tema ["img_url"], tema["url"], tema["date"])
        archivo.write(registro)
    archivo.close()
    print()
generar_csv("nueva_lista.csv", lista_bzrp)
#lista = parser_csv("nueva_lista.csv")
