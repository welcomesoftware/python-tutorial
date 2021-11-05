print('Conversor de temperatura')
print('=======================================================')
entrada = input('Introduza la temperatura Fahrenheit: ')
try:
    fahr = float(entrada)
    celcius = (fahr - 32) * 5.0 / 9.0
    print(celcius, 'Celcius')
except:
    print('¡Valor invalido!')
    print('Por favor introduzca una temperatura')
