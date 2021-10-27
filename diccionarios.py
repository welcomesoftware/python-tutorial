mi_diccionario = {'Alemania':'Berlin','Honduras':'Tegucigalpa','El Salvador':'San Salvador','España':'Madrid','Francia':'París','Reino Unido':'Londres'}

# imprime un valor en base a su clave
print(mi_diccionario['Francia'])

# imprime el valor de todo el diccionario
print(mi_diccionario)

# agregar un valor en el diccionario
mi_diccionario['Italia'] = 'Lisboa'
print(mi_diccionario)

# actualizar un valor en una clave
mi_diccionario['Italia'] = 'Roma'
print(mi_diccionario)

# eliminar un elemento del diccionario
del mi_diccionario['Reino Unido']
print(mi_diccionario)

# crear un diccionario con mezcla de tipos
diccionario_tipos = {'Honduras':'Tegucigalpa', 23:'Jordan','Mosqueteros':3}
print(diccionario_tipos)

# usando tuplas con diccionarios
mi_tupla = ['España', 'Francia', 'Alemania', 'Italia', 'Reino Unido']
new_dic = {
    mi_tupla[0]:'Madrid',
    mi_tupla[1]:'París',
    mi_tupla[2]:'Berlin',
    mi_tupla[3]:'Roma',
    mi_tupla[4]:'Londres'
}
print(new_dic)

# tuplas como valores de clave en un diccionario
diccionario_datos = {
    23:'Jordan',
    'Nombre':'Michael',
    'Equipo':'Chicago',
    'Anillos':[1991,1992,1993,1996,1997,1998]
}
print(diccionario_datos)
print(diccionario_datos['Anillos'])

# diccionarios como valor clave en un diccionario
diccionario_edades = {'Edades':{'Temporadas':[1991,1992,1993,1996,1997,1998]}}
