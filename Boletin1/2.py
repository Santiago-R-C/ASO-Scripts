#!/usr/bin/python3

# Importaciones para python
from math import radians, sin, degrees
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

try:
    # Pedimos
    a = float(input("Dame uno de los lados del triángulo en metros: "))
    b = float(input("Dame otro de los lados del triángulo en metros: "))
    c = radians(float(input("Dame el ángulo que los une en grados: ")))

    # Calculamos
    area = (1 / 2) * a * b * sin(c)

    # Mostramos por pantalla el resultado
    print(f"El área del triángulo de lados {a:.4f} metros, {b:.4f} metros y {degrees(c):.4f} radianes es de {area:.4f} metros\xb2")
except:
    print("Introduce valores válidos")