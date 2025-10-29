#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from hashlib import sha512
from getpass import getpass

# Vaciar el terminal
run("clear", shell=True)

usuario = "pepe"
passUsuario = sha512("abc123..".encode("utf-8")).hexdigest()

u = input("Introduce tu nombre de usuario: ")
p = sha512(getpass("Introduce tu contraseña: ").encode("utf-8")).hexdigest()
if u == usuario and p == passUsuario:
    print("Has entrado al sistema")
else:
    print("Error de usuario y/o contraseña no válidos")