import re

#split 
#print(re.split(" ", "hola mundo"))
print(re.split("[a-z ] +", "hola mundo 125c"))
#corta en todas las letras que esten entre la a y la z,
#o bien sea un espacio y corta. Con el mas agrupa la cantidad de
#veces que una parte del la lista se repite y lo agrupa en uno solo. 
print(re.split("[0-9 ]+", "hola mundo 125c"))
print(re.split("hola|chau", "hola mundo 125 chau"))
#donde encontro una ocurrencia de hola o chau corto del acadena. 
print(re.split("[a-z]|[0-9| ]", "hola mundo @@ 125 chau"))

#search

print(re.search(" ", "hola"))
#devuelve none porque no encuentra lo que le pido
print(re.search("como", "hola como estan ?").span)
#me devuelde un objeto del tipo match , y me dice delde donde hasta donde
#lo encontro.
#span devuelve una tupla que indoca de donde a hasta donde(en caracteres) encontro el daro en l acaden.
print(re.search("como", "hola como estan ?").start)#donde empieza
print(re.search("como", "hola como estan ?").end)#donde termina

print(re.search("[0-9]+", "texto con numeros: 123 letras: aaa"))
#busca un numero del 0 al 9 dentro de la cadena donde haya una o mas ocurrencias.

#FINDALL

texto = "Uno 1 Dos 2 tres 3 cuatro"

print(re.findall(" ", texto))
print(re.findall("[0-9]+", texto))
print(re.findall("[a-zA-Z]+", texto))
print(re.findall("[a-zA-Z]{3,6}", texto))
#trae como minimo tres caracteres, trae solo 3 caracteres
#las llaves indican minimo y maximo de caracteres que puden traer

#SUB

texto = "abc abc ccc   ddd abc aaaa"

result = re.sub("abc", "", texto)
print (result)

result = re.sub('\\s+', " ", texto)
#reemplaza los espacios duplicados por un solo espacio
print(result)
result = re.sub(r'\s+', " ", texto)
#\s un spacio 
#la + le indica que puede ser una cantidad x de espacios
#la r le indica que es una exprecion regular sino deberiamos poner \\s

#---------------------
texto = "QUEVEDO || BZRP Music Sessions #52"

print(re.split(" [\|#]+", texto))

fecha = "2022-02-03 19:20:33"

print(re.findall(" [0-9]{4}-[0-9]{2}-[0-9]{2}", fecha))

print(re.findall("[0-9]{4}", fecha))
print(re.findall("-[0-9]{2}-", fecha))#con guiones
print(re.findall("-([0-9]{2})-", fecha))#sin guiones
print(re.findall("-([0-9]{2}) ", fecha))

año = "([0-9]{2,4})"
mes = "([0-9]{1,2})"
dia = "([0-9]{1,2})"

print(re.findall(f"{año}-{mes}-{dia}", fecha))