# Escriba un programa para pedirle al usuario el número de horas y la tarifa
# por horas para calcular el salario bruto.
horas = input('Introduzca Horas: ')
tarifa = input('Introduzca Tarifa: ')

# calcula el salario bruto
horas = int(horas)
tarifa = float(tarifa)

salario = horas * tarifa

print(salario) 
