# biblioteca
import math

print('Programa de cálculo de raíz cuadrada')
print('====================================')

# entrada de datos
numero=int(input('introduce un número: '))

# variables
intentos=0

# bucle
while numero < 0:
    print('¡No se puede calcular la raíz de un número negativo!')

    if intentos == 2:
        print('¡Has intentado demasiadas veces!')
        print('El programa debe finalizar...')
        break

    numero=int(input('introduce un número: '))
    intentos += 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print('Solucion:', solucion)
