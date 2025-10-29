#!/usr/bin/python3

# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

for i in range(n1, n2 + 1):
    if i % 2 == 0:
        print(i)