#Angeles Belen Garcia - 1 B - Turno mañana 
'''
La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.
Se registra por cada compra:
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.
Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.
'''
descuento = 0
total_bruto = 0
mas_caro_tipo_precio = 0
acumulador_precio_kilo = 0

for compras in range(14):
    peso = float(input("Ingrese el peso: entre 10 y 100 kg "))
    while peso < 10 or peso > 100:
        peso = float(input("Error - Ingrese el peso: entre 10 y 100 kg "))
    precio_por_kilo = float(input("Ingrese el precio por kilo "))
    while precio_por_kilo < 1:
        precio_por_kilo = float(input("Error - Ingrese el precio por kilo "))
    tipo_variedad = input("Ingrese que tipo de alimento compro, vegetal, animal o mezcla ")
    while tipo_variedad != "vegetal" and tipo_variedad != "animal" and tipo_variedad != "mezcla":
        tipo_variedad = input("Error - Ingrese que tipo de alimento compro, vegetal, animal o mezcla ")
    if peso > 300:
        descuento = 25
    elif peso > 100:
        descuento = 15
    if precio_por_kilo > mas_caro_tipo_precio or total_bruto == 0:
        mas_caro_tipo_precio = precio_por_kilo
        mas_caro_nombre = tipo_variedad
    acumulador_precio_kilo += precio_por_kilo
    total_bruto += peso * precio_por_kilo 

print("El importe total a pagar sin descuento es de ", total_bruto)
if descuento != 0:
    bruto_descuento = 25 * total_bruto / 100
    print("El descuento es de ", descuento , "%")
    print("El importe total a pagar con descuento es de ", bruto_descuento)
promedio_precio_kilo = acumulador_precio_kilo / 15
print("El alimento mas caro es del tipo ", mas_caro_nombre)
print("El promedio de peso por kilo es de ", promedio_precio_kilo)


