#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from re import compile, search
from misfunciones import comprobacionContraseñas

# Vaciar el terminal
run("clear", shell=True)

nombre = input("Dame un nombre de usuario: ").strip()

print(comprobacionContraseñas(nombre))