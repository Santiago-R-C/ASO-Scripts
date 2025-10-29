#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from random import randint

# Vaciar el terminal
run("clear", shell=True)

numerooculto = randint(1, 100)
# print(numerooculto)

# Contador de intentos
c = 0

# Bucle infinito
while True:
    
    # Incrementa el contador de intentos
    c += 1

    # Pedimos número con el que juega el usuario
    n = int(input("Dame un número: "))

    # Comparamos el número del usuario con el número oculto
    if (n < numerooculto):
        print("El número es mayor")
    elif (n > numerooculto):
        print("El número es menor")
    else:
        print(f"Has acertado en {c} intentos")

        # Fin del bucle infinito
        break