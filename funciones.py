# Funciones
# Es un conjunto de una o mas lineas de código agrupadas en un bloque, se util-
# izan para cumplir una tarea especifica. Las funciones también se denominan
# métodos cuando están definidas dentro de una clase.

# Las funciones pueden devolver valores, tener parámetros y recibir argumentos,
# la principal utilidad de una función es reutilizar el codigo. 

# Sintaxis:
# ---------------------------------
# def nombre_función(parámetros):
#   instrucciones_de_función
#   retorno (opcional)



# función propia
def saludo(numero=5):
    for i in range(numero):
        print("Hola Mundo", i+1)

def mensaje():
    print("Estamos aprendiendo funciones")
    print("Estamos aprendiendo instrucciones básicas")
    print("Poco a poco iremos avanzando")

saludo()
mensaje()

def suma():
    num1=5
    num2=7
    print(num1+num2)

suma()

def suma(num1, num2):
    print(num1+num2)

suma(10, 15)

def saludo(nombre):
    print("Hola mucho gusto es un placer conocerte.")

saludo("Darío")
