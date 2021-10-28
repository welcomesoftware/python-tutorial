print('-----------------------------------------------------------------------')
print('\t\tPrograma de evaluación de notas de alumnos')
print('-----------------------------------------------------------------------')
def evaluacion(nota):
    valoracion = 'Aprobado'
    if nota < 5:
       valoracion = 'Reprobado'
    return valoracion

nota = input('Introduzca la nota del alumno: ')
nota = int(nota)

print(evaluacion(nota))
