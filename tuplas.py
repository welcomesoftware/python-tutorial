# imprime un mensaje en pantalla
print("Esto es un ejemplo de las tuplas")
mi_tupla = ('Darío',10,9,1991)
print(mi_tupla,'\n')

# métodos para convertir una tupla en una lista
print("Convirtiendo una tupla en lista: list(tupla)")
mi_lista = list(mi_tupla)
print(mi_lista, '\n')

print("Convirtiendo una lista en tupla: tuple(lista)")
tupla = tuple(mi_lista)
print(tupla)

print("\nValida si Darío se encuentra en la tupla")
print("Darío" in tupla)
print("\nVerifica cuantas veces se encuentra Darío en la tupla")
print(tupla.count("Darío"))
print("\nDetermina la longitud de una tupla: len(tupla)")
print(len(tupla))

print("\nDesempaquetado de una tupla")
# asigna todos los valores de una tupla a variables individuales
nombre, dia, mes, agno = tupla
print(nombre, dia, mes, agno)
