#!/usr/bin/python3

# Importaciones para python
from math import pi, pow
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

try:
    # Pedimos por pantalla el valor del radio pasándolo a número
    radio = float(input("Dame el radio: "))

    # Calculamos
    perimetro = 2 * pi * radio
    area = pi * pow(radio,2)
    volumen = 4 * pi * pow(radio,3) / 3

    # Mostramos por pantalla el resultado
    print(f"El perímetro de un aro de radio {radio} cm es {perimetro:.4f} cm")
    print(f"El área de una circunferencia de radio {radio} cm es {area:.4f} cm\xb2")
    print(f"El volumen de una esfera de radio {radio} cm es {volumen:.4f} cm\xb3")

except:
    print("Introduce valor de radio válido")



# # # # # --------------------------------------------------- # # # # #
# # # # # ----------- Lo mismo pero con funciones ----------- # # # # #

def perimetro(radio):
    perimetro = 2 * pi * radio
    return perimetro

def area(radio):
    area = pi * pow(radio,2)
    return area

def volumen(radio):
    volumen = 4 * pi * pow(radio,3) / 3
    return volumen

try:
    # Pedimos por pantalla el valor del radio pasándolo a número
    radio = float(input("Dame el radio: "))

    # Llamamos a las funciones
    perimetro = perimetro(radio)
    area = area(radio)
    volumen = volumen(radio)

    # Mostramos por pantalla el resultado
    print(f"El perímetro de un aro de radio {radio} cm es {perimetro:.4f} cm")
    print(f"El área de una circunferencia de radio {radio} cm es {area:.4f} cm\xb2")
    print(f"El volumen de una esfera de radio {radio} cm es {volumen:.4f} cm\xb3")

except:
    print("Introduce valor de radio válido")