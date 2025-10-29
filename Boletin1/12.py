#!/usr/bin/python3

# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

n1 = int(input("Ingrese un numero: "))

factorial = 1

for i in range(2,n1+1):
    factorial *= i
print(f"El factorial de {n1} es {factorial}")