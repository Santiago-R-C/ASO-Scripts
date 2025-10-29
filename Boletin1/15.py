#!/usr/bin/python3

# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)
from math import sqrt

esPrimo = True
num = int(input("Ingrese un número: "))

for i in range(2, int(sqrt(num))+1):
    resto = num%i
    # print(resto)
    if resto == 0:
        esPrimo = False
        break
print(esPrimo)