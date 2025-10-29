#!/usr/bin/python3

# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

print ("""Operaciones a realizar:
1.- Suma
2.- Resta
3.- Multiplicación
4.- División""")
print("-"*20)
n1 = float(input("Dame un número: "))
n2 = float(input("Dame otro número: "))
op = input("Dame el número de la operación: ")
if (op == "1"):
    sol = n1 + n2
    print (f"{n1} + {n2} = {sol}")
elif (op == "2"):
    sol = n1 + n2
    print (f"{n1} - {n2} = {sol}")
elif (op == "3"):
    sol = n1 + n2
    print (f"{n1} * {n2} = {sol}")
elif (op == "4"):
    if n2 == float(0):
        print("No se puede dividir por 0")
    else:
        sol = n1 / n2
        print (f"{n1} * {n2} = {sol}")
else:
    print ("Operación no válida")
print("-"*50)
salir = input("Pulsa 's' para salir: ")
if salir.lower() == "s":
    exit()
else:
    pass