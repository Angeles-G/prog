from os import system
from data import lista_bzrp


def prueba():
    titulo = 'QUEVEDO || BZRP Music Sessions #52'
    cadena = (titulo.split("||"))
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    tipo = cadena2[0].strip()
    numero = cadena2[1].strip()
    print(f"{artista} - {tipo} - {numero}" )


def prueba2(titulo:str):
    cadena = (titulo.split("||"))
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    tipo = cadena2[0].strip()
    numero = cadena2[1].strip()
    print(f"{artista} - {tipo} - {numero}" )

def prueba3(titulo:str):
    cadena = (titulo.split("||"))
    if len(cadena) >1:
        artista = cadena[0].strip()
        cadena2 = cadena[1].split("#")
        if len(cadena2) >1:
            tipo = cadena2[0].strip()
            numero = cadena2[1].strip()
            print(f"{artista} - {tipo} - {numero}" )

def prueba4(titulo:str):
    tipo = "BZRP Music Sessions"
    parte1 = titulo.split(tipo)
    if len(parte1) == 2:
        artista = parte1[0].replace("||","").strip()
        numero = parte1[1].replace("#","").strip()
        print(f"{artista} - {tipo} - {numero}" )


def url(tema:dict):
    # cadena = tema['url'].split("=")
    # print(cadena[1])

    # codigo= tema['url'].replace("https://youtube.com/watch?v=", "")
    # print(codigo
    url = tema['url']
    indice = url.index("=")
    codigo = url[indice+1:]
    print(codigo)
    # url = tema['url']
    # codigo = url[28:]
    # print (codigo)

#'date': '2021-07-28 00:00:00'
def formtear_fecha(fecha_cadena:str):
    fecha_split = fecha_cadena.split(" ")
    fecha = fecha_split[0].split("-")
    year = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    separador = "/"
    fecha_formato = separador.join([dia, mes, year])
    return fecha_formato


def test(lista:list):
    for tema in lista:
        #prueba4(tema["title"])
        #url(tema)
        formtear_fecha(tema["date"])