print('-\t\tSistema de verificación de acceso\t\t-')

usuario_edad = int(input('Introduce tu edad: '))

if usuario_edad < 18:
    print('Acceso denegado: no puedes pasar')
elif usuario_edad > 100:
    print('Acceso denegado: edad incorrecta')
else:
    print('Acceso concedido: puedes pasar')
print('\nPrograma finalizado')
