# Escribe un programa que solicite una puntuación entre 0.0 y 1.0, si la 
# puntuación está fuera de ese rango, muestra un mensaje de error. si la 
# puntuación está entre 0.0 y 1.0, muestra la calificación usando la tabla
# siguiente:

# Puntuación Calificación
# >= 0.9    Sobresaliente
# >= 0.8    Notable
# >= 0.7    Bien
# >= 0.6    Suficiente
# < 0.6     Insuficiente

entrada = float(input('Introduzca una puntuación: '))

if entrada < 0.0 or entrada > 1.0:
    print('Puntuación fuera de rango')
elif entrada < 0.6:
    print('Insuficiente')
elif entrada == 0.6:
    print('Suficiente')
elif entrada == 0.7:
    print('Bien')
elif entrada == 0.8:
    print('Notable')
elif entrada == 0.9:
    print('Sobresaliente')
