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

## Captura de Excepciones usando try y except

Existen estructuras de ejecución condicional en python para manejar tipos de errores
esperados e inesperados, llamadas 'try / except'. La idea de *try* y *except* es que 
si se sabe cierta secuencia de instrucciones puede generar un problema, y es posible
añadir ciertas sentencias, para que sean ejecutadas en caso de error. Estas sentencias
extras '**except**' serán ignoradas si no se produce ningún error.

### Sintaxis de try / except

```
entrada = input('Introduza la Temperatura Fahrenheit: ')
try: 
	fahrenheit = float(entrada)
	celcius = (fahrenheit - 32) * 5.0 / 9.0
	print(celcius, 'Celcius')
except: 
	print('¡Valor no válido! ', fahrenheit)
	print('Por favor, introduzca una temperatura')
```

## Bucles o Ciclos

La utilidad del bucle es repertir n cantidad de veces alguna linea, instrucción o 
función de código sin tener que escribirlo tantas veces, solo escribirlo una vez.

Habrá ocaciones en las cuales no sabremos cuantas veces se repirá un bloque o linea 
de código.

### Tipos de bucles en python

**Determinados**: 
1. Se ejecutan un número determinado de veces.
2. Se sabe cuantas veces se va a ejecutar el código en el interior del bucle.

**Indeterminados**: 
1. Se ejecutan un número indeterminado de veces.
2. No se sabe a priori cuantas veces se va a ejecutar el código en el interior del bucle.
3. El número de veces que se ejecutará dependerá de las circunstancias durante la ejecución.

### Bucle for

**Sintaxis**: 

```
for variable in elemento_a_recorrer:
	cuerpo del bucle
```

### Continue, Pass, Else dentro de los bucles
	**continue**: permite ejecutar una siguiente ejecución de un bucle.
	**pass**: se utiliza para declarar nulo un bucle y que este mismo no se ejecute.
	**else**: tiene la misma función que en un condicional if, solo que aplicado a bucles.
