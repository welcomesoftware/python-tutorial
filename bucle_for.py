for i in range(5):
    print('Hola ', i)


for i in [1,2,3]:
    print('Dario')

for i in range(10):
    print('Número n. ', i)

for i in range(30):
    # esta es una forma de formatear el final de la linea
    print(i, end = " ")
    if i == 29:
        print(i)

# recorre una cadena de texto
# valida si el correo es valido en función si tiene @ o no
validate = False

email=input('Introduzca su email: ')

for i in email:
    if (i == '@'):
        if i == '.':
            validate = True

if validate:
    print('Dirrección de correo válido')
else:
    print('Dirrección de correo invalido')
