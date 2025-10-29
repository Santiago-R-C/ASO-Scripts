#!/usr/bin/python3

# Importaciones para python
from subprocess import run


# Vaciar el terminal
run("clear", shell=True)

dPC = {
    "micro":"Intel Core i7",
    "ram":"DDR4",
    "disco":"M.2",
    "tamDisco":"1TB",
    "fuente":"aerocool"
}

# # Añadir valores y claves
# dPC.setdefault("gpu","nvidia")

# # Eliminar claves (y al eliminar la clave eliminas el valor al que esta anclado)
# dPC.pop("ram")

# # Cambiar valores
# dPC["ram"] = "DDR5"

# # Cambiar claves (añade una nueva clave con el valor de la otra y se elimina la clave antigua)
# dPC.setdefault("memoria",dPC["ram"])
# dPC.pop("ram")

# listaClaves = dPC.keys()
# print(listaClaves)
# listaValores = dPC.values()
# print(listaValores)

for k,v in dPC.items():
    print (f"El valor de {k} es {v}")