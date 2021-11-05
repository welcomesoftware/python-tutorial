print('Asignaturas optativas año 2021')
print('====================================================')
print('Informaticas Gráfica - Software Testing - Pentesting')
asignatura=input('Escribe la asignatura: ').capitalize()
print('====================================================')

# operador in
if asignatura in ('Informaticas Gráfica', 'Software Testing', 'Pentesting'):
    print('Asignatura Elegida: ', asignatura)
else:
    print('Asignatura elegida no está disponible')
