#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from misfunciones import nombreValido

# Vaciar el terminal
run("clear", shell=True)

n = input("Dame un nombre de usuario: ")

if nombreValido(n)["valido"]:
    print ("Nombre válido")
else:
    print ("Nombre no válido")