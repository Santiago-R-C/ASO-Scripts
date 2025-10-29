#!/usr/bin/python3

# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

dineros = {}
lBiMo = [500,200,100,50,20,10,5,2,1]
cantidad = 1238


for i in lBiMo:
    while cantidad > 0:
        prueba = cantidad - i
        if prueba < 0:
            contador = 0
            break
        else:
            contador =+ 1
            cantidad = cantidad - i
            dineros.setdefault(i,contador)
print (dineros)
    

# for i in lBiMo:
#     resultado = int(cantidad / i)
#     cantidad = cantidad - (i * resultado)
#     dineros.setdefault(i,resultado)
# print (dineros)