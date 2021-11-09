# continue
for letra in 'Python':

    # continue ignora el resto de código despues de él y ejecuta la siguiente iteración.
    if letra == 'h':
        continue

    print('Letra:', letra)

# hace uso de continue para contar la cantidad de letras en una cadena de texto.
# omitiendo los espacios en blanco.
nombre = 'Joshito Welcome'

def letralen(nombre):
    cantidad = 0
    for letra in nombre:
        if letra == ' ':
            continue
        else:
            cantidad += 1
    return cantidad

print('len(nombre):', len(nombre))
print('letralen(nombre):', letralen(nombre))

# hace uso de pass para entender como funciona
class miclase:
    pass    # clase nula para implementar mas tarde

# uso de else dentro de los bucles
# else se va a ejecutar siempre despues de la finalización del ciclo, y de la única forma
# que else no se ejecutará, será si el ciclo se rompe utilizando break.
email = input('Ingresa tu email: ')

for i in email:
    if i == '@':
        arroba = True
        break
else:
    arroba = False

print(arroba)
