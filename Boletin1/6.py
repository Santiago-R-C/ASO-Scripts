#!/usr/bin/python3

# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

# Lista vacía
lista = []

# Bucle para pedir números
while True:
    numero = int(input("Dame un número: "))
    if numero != 0:
        lista.append(numero)
    else:
        break

# Operaciones
if len(lista) == 0:
    print("No se han introducido números.")
else:
    suma = sum(lista)
    media = suma / len(lista)

    # Resultado
    print (f"La suma de la lista es {suma} y la media {media}")