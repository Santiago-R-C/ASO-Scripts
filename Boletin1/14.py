#!/usr/bin/python3

# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

base = float(input("Dame un número: "))
expo = int(input("Dame el exponente: "))

sol = 1
for _ in range(expo):
    sol = sol * base

print(f"La solución de {base}^{expo} es {sol}")