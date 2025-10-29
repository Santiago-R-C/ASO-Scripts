#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from pathlib import Path
from datetime import datetime

# Vaciar el terminal
run("clear", shell=True)

adAgenda = "./miAgenda.txt"
dAgenda = {}
tmp = {}

# Lectura del archivo línea a línea, más usado
with open(adAgenda, "r") as fr:
    la = fr.readlines()
    for l in la:
        ll = l.split(":")
        k = ll[0].strip()
        v = ll[1].strip()
        dAgenda.setdefault(k,v)

while True:
    # Información de la agenda
    print("Agenda")
    print("-"*30)
    for k,v in dAgenda.items():
        print(f"{k} : {v}")
    print("-"*30)
    # Configuración de los usuarios
    nombre = input("""Dame un nombre de usuario:
O pulse * para salir
Nombre: """)
    # Vaciado de terminal
    run("clear", shell=True)
    # Cuando los nombres ya estan en la agenda
    if nombre == "*":
        print("Saliendo del programa")
        break
    elif nombre in dAgenda:
        print(f"El usuario {nombre} esta en la agenda con el teléfono {dAgenda[nombre]}")
        opcion = int(input("""Seleciona la opcion que quiere
--- 1.- Desea modificar el teléfono
--- 2.- Desea eliminar el contacto
--- 3.- Salir
Opción: """))
        if opcion == 1:
            nTelefono = input("Ingresa el nuevo número de teléfono: ")
            if 111111111 <= int(nTelefono) <= 999999999:
                nTelefonoAntiguo = dAgenda[nombre]
                dAgenda.pop(nombre)
                dAgenda.setdefault(nombre,nTelefono)
                print(f"El usuario {nombre} modificó el número de teléfono de {nTelefonoAntiguo} a {dAgenda[nombre]}")
            else:
                print("Número no válido")
        elif opcion == 2:
            dAgenda.pop(nombre)
            print(f"El contacto {nombre} a sido eliminado")
        elif opcion == 3:
            print("Saliendo del programa")
            break
    # Cuando los nombres no estan en la agenda
    else:
        nTelefono = input("""Ingresa el numero de teléfono:
--- O pulse * para salir
Teléfono: """)
        if nTelefono == "*" or 111111111 <= int(nTelefono) <= 999999999:
            if nTelefono == "*":
                print("Saliendo del programa")
                break
            else:
                dAgenda.setdefault(nombre,nTelefono)
                print(f"El número de teléfono {dAgenda[nombre]} fue añadido al usuario {nombre}")
        else:
            print("Número no válido")
            break
# Añadir el diccionario al archivo y crar las copias de seguridad
archivo = Path("./miAgenda.txt")
copias_de_seguridad = Path("./copias_de_seguridad/")
sAgenda = ""
for k,v in dAgenda.items():
    sAgenda += f"{k}:{v}\n"
if archivo.exists():
    tmpT = ""
    with open(adAgenda, "r") as fr:
        la = fr.readlines()
        for l in la:
            ll = l.split(":")
            k = ll[0].strip()
            v = ll[1].strip()
            tmp.setdefault(k,v)
        for k,v in tmp.items():
            tmpT += f"{k}:{v}\n"
    adABackup = "copias_de_seguridad/Agenda_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".backup"
    with open(adABackup,"w", encoding="utf-8") as fw:
        fw.write(tmpT)
    archivo.unlink(missing_ok=True)

    # Cuando sean 6 copias de seguridad se elimina la más antigua
    # if len(list(copias_de_seguridad.glob('*'))) > 5
        # {nombre del archivo más antiguo}.unlink(missing_ok=True)
        # nombres = [archivo.name for archivo in carpeta.iterdir() if archivo.is_file()]


with open(adAgenda,"w") as fw:
    fw.write(sAgenda)