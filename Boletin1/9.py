#!/usr/bin/python3

# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

dNotas = {
    0:"Muy Deficiente",
    1:"Muy Deficiente",
    2:"Muy Deficiente",
    3:"Insuficiente",
    4:"Insuficiente",
    5:"Suficiente",
    6:"Bien",
    7:"Notable",
    8:"Notable",
    9:"Sobresaliente",
    10:"Sobresaliente"
}

n = int(input("Dame una nota: "))
print (f"Tu nota es {dNotas[n]}")