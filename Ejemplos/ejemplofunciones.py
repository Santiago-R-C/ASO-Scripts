#!/usr/bin/python3

# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

# Definición de una función saludo
def saludo():
    salida = "Hola"
    return salida

# Llamada a la función saludo (no devuelve nada a menos que imprimas la función)
print (saludo())

# Definición de una función saludo con variable (por defecto vació)
def saludo2(nombre=''):
    salida = f"Hola {nombre}"
    return salida

# Llamada a la función saludo2 (no devuelve nada a menos que imprimas la función)
print (saludo2())

# Llamada a la función saludo2 con un nombre dado por el usuario
# (no devuelve nada a menos que imprimas la función)
n = input("Dime tu nombre: ")
print (saludo2(n))

# Definición de una función suma de 2 números
def suma2(n1,n2):
    resultado = n1 + n2
    return resultado

# Llamada a la función suma2 con 1 y 2
print(suma2(1,2))

# Llamada a la función suma2 con n1 y n2
n1 = 1
n2 = 2
print(suma2(n1,n2))