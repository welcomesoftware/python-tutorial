# Tutorial de Python

## Listas en python

Una lista en python es una estructura de datos que nos permite almacenar gran
cantidad de información, es el equivalente a los arrays o arreglos en otros 
lenguajes de programación como C. En python las listas pueden guardar diferentes
tipos de valores, esto no ocurre en otros lenguajes de programación. Se pueden
expandir dinámicamente, añadiendo nuevos elementos, Esta es otra novedad de
python con respecto a otros lenguajes.

### Sintaxis de las listas 

```
nombre_lista = [elem1, elem2, elem3, ...]
```

## Tuplas en python

Las tuplas son listas inmutables, más parecidas a los arreglos en otros lenguajes
de programación, debido a que no se pueden modificar después de su creación.

Solo permiten extraer porciones de la tupla, sin embargo el resúltado se entrega
en una nueva tupla. También permiten comprobar si un elemento se encuentra en la
lista. 

### Ventajas de las tuplas
	Más rápidas
	Menos espacio en memoria *Optimización*
	Formatean Strings
	Pueden utilizarse como claves en un diccionario

### Sintaxis de las tuplas

```
nombre_tupla = (elem1, elem2, elem3, ...)
```

## Diccionarios en python

Los diccionarios son una estructura de datos parecida a las listas y las tuplas
la característica principal, es que los datos se almacenan con una clave, de 
forma que se crea una clave:valor para cada elemento almacenado. Los elementos 
almacenados no estan ordenados, debido a que cada clave es única.

### Sintaxis de los diccionarios

```
nombre_diccionario = {'clave':'valor', 'clave':'valor', ...}
```

## Ejecución condicional

### Expresiones booleanas

Una expresion booleana es aquella que puede ser verdadera (True) o falsa (False)

Los siguientes ejemplos usan el operador de compración (==), el cual compara los
operadores y retorna True si son iguales y retorna False en caso contrario.

### Operadores de compración

```
x == y 		# igual a
x != y 		# no igual a, o distinto de 
x >= y 		# mayor o igual
x <= y 		# menor o igual
x > y 		# mayor que 
x < y 		# menor que 
x is y 		# es lo mismo que
x is not 	# no es lo mismo que
```

### Sintaxis de los condicionales if en python

```
if x == y: 
	print('x es igual a y')
```
