# evaluar los salarios de los empleados
salario_presidente = int(input('Introduce salario presidente: '))
print('Salario presidente:', salario_presidente)

salario_director = int(input('Introduce salario director: '))
print('Salario director:', salario_director)

salario_jefe_area = int(input('Introduce salario jefe de área: '))
print('Salario jefe área:', salario_jefe_area)

salario_administrativo = int(input('Introduce salario administrativo: '))
print('Salario administrativo:', salario_administrativo)

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print('Todo funciona correctamente')
else:
    print('Algo falla en esta empresa')
