#!/usr/bin/python3

# Importaciones para python
from subprocess import run
# from pathlib import Path

# Vaciar el terminal
run("clear", shell=True)

# Lista de Usuarios
lInfoUsuarios = []

# Diccionario de Contraseñas
dShadow = {}

# Ubicación de los archivos y permisos para poder abrirlos
aPasswd = "/etc/passwd"
aShadow = "/etc/shadow"

# Apertura del archivo aShadow
with open(aShadow, "r") as fr:
    for l in fr:
        ll = l.split(":")
        dShadow.setdefault(ll[0], len(ll[1]) > 1)

# Apertura del archivo aPasswd
with open(aPasswd, "r") as fr:
    for l in fr.readlines():
        dUsuario = {}
        ll = l.split(":")
        uid = int(ll[2].strip())
        if (1000 <= uid <= 60000 or uid == 0):
            # Implementación de la cuenta, el uid, el pathHome y la shell en el diccionario dUsuario
            dUsuario.setdefault("cuenta", ll[0].strip())
            dUsuario.setdefault("uid", int(ll[2].strip()))
            dUsuario.setdefault("pathHome", ll[5].strip())
            dUsuario.setdefault("shell", ll[6].strip())

            # Implementación del grupoPrincipal y los gruposSecundarios en el diccionario dUsuario
            grupoPrincipal = ""
            gruposSecundarios = []
            comando = f"groups {ll[0]}"
            salida = run(comando, shell=True, capture_output=True, text=True, check=True).stdout.split(":")[1].strip().split()
            dUsuario.setdefault("grupoPrincipal", salida[0])
            dUsuario.setdefault("gruposSecundarios", salida[1:])
            
            # Implementación del tamHome en el diccionario dUsuario
            comando = f"sudo du -hs {ll[5]}"
            salida = run(comando, shell=True, capture_output=True, text=True).stdout.split()[0]
            dUsuario.setdefault("tamHome", salida)

            # Implementación de la contraseña en el diccionario dUsuario
            for k,v in dShadow.items():
                dUsuario.setdefault("password", v)

            # Agregamos el diccionario dUsuario a la lista lInfoUsuarios
            lInfoUsuarios.append(dUsuario)
# Ejecución para ver la lista que nos resulta línea por línea
for u in lInfoUsuarios:
    print(u)