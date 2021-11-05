print('Programa de becas año 2021')
print('==================================================')

distancia_escuela=int(input('Introduce la distancia a la escuela en km: '))
numero_hermanos=int(input('Introduce el numero de hermanos: '))
salario_familiar=int(input('Introduce el salario anual bruto: '))
print('--------------------------------------------------')

# operadores lógicos and, or
if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <=20000:
    print('Tienes derecho al sistema de becados')
else:
    print('No tienes derecho al sistema de becados')
