nombre = input('Ingrese un archivo: ')
manejador = open(nombre, 'r')
contador = dict()

for linea in manejador:
    palabras = linea.split()
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1

grancuenta = None
granpalabra = None
for palabra, contador in list(contador.items()):
    if grancuenta is None or contador > grancuenta:
        granpalabra = palabra
        grancuenta = contador

print(granpalabra, grancuenta)


