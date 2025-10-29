#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from re import compile, search, findall, IGNORECASE

# Vaciar el terminal
run("clear", shell=True)

# --------------------------------------------------

texto = input("Introduce texto: ")

stringPatronSimbol = '\W'
patronSimbol = compile(stringPatronSimbol)
if(patronSimbol.search(texto)):
    print("Sí hay símbolos")
else:
    print("No hay símbolos")

# --------------------------------------------------

c = "ip a show enp0s3"
s = run(c, shell=True, capture_output=True, text=True).stdout

pIP = compile(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}")
lIPs = pIP.findall(s)
print(lIPs)

pMAC = compile(r"(?:[0-9A-F]{2}[:-]){5}[0-9A-F]{2}", IGNORECASE)
lMAC = pMAC.findall(s)
print(lMAC)