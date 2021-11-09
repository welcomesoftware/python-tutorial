salir = False

while salir == False:
	email = input('Introduce tu email: ')
	valido = False
	contador = 0
	
	for i in email:
		if i == ' ':
			valido = False
			break
		
		if (i == '@'):
			contador = 1

		elif contador == 1:
			if (i == '.'):
				valido = True

			elif i == '@' or i == ' ' or i == '.':
				valido = False
				break

	if valido:
		print('Email bueno')
	else:
		print('Email malo')

	opcion = input('Quieres salir [y/n]')
	if opcion == 'y':
		salir = True
	else:
		salir = False

