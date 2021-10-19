mi_lista = ["María", "Pepe", "Antonio", "Marta", "Darío"]

print("Imprime todos los índices de la lista[:]")
print(mi_lista[:])
print("")

print("Acceder a un índice en concreto lista[2]")
print(mi_lista[2])
print("")

print("Acceder a un índice negativo hace que la lista se muestre en orden inverso lista[-1]")
print(mi_lista[-1])
print("")

print("Acceder a una porción de la lista[1:3]")
print(mi_lista[1:3])
print("")

print("Acceder a una porcion de la lista desde el índice 0 hasta 3 lista[:3]")
print(mi_lista[:3])
print("")

print("Acceder a los elementos desde el índice 2 hasta el final lista[2:]")
print(mi_lista[2:])
print("")

print("Agregar nuevos elementos al final de la lista lista.append(\"Jamileth\")")
mi_lista.append("Jamileth")
print(mi_lista, "\n")
print()

print("Agregar nuevos elementos en un índice especifico lista.insert(2, \"Joshua\")")
mi_lista.insert(2, "Joshua")
print(mi_lista)
print()

print("Agregar varios elementos a la lista lista.extend(nueva_lista[])")
nueva_lista = ["Carlos", "German", "Moisa", "Saul", "Marbella", "Po", "Pipa","Checho","Fercho", "Breco", "Discipulo", "Mini Po"]
mi_lista.extend(nueva_lista)
print(mi_lista, "\n")

print("Para obtener el índice de un elemento en la lista.index(\"Joshua\")")
print(mi_lista.index("Joshua"), "\n")

print("Para saber si un elemento se encuentra en la lista: \"Pepe\" in lista")
print("Mini Po" in mi_lista, "\n")

mi_lista.extend([5, True, 78.35])
print(mi_lista, "\n")

print("Eliminar elementos de la lista.remove(\"Marta\")")
mi_lista.remove("Marta")
print(mi_lista, "\n")

print("Eliminar el ultimo elemento de la lista.pop()")
mi_lista.pop()
print(mi_lista, "\n")

print("Sumar dos listas: lista1 + lista2")
lista=["Victor", "Manuel"]
mi_lista += lista
print(mi_lista, "\n")

print("Repetir una lista n veces: lista * 3")
print(mi_lista[:] * 3, "\n")
