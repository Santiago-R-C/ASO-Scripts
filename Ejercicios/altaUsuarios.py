#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from misfunciones import eliminaTildes,cifrar_contraseña

# Vaciar el terminal
run("clear", shell=True)

# 6.- Crear un script en python que nos permita dar de alta usuarios en un equipo
# linux desde un csv separado por comas (usuarios.csv) : 
    #    - Crear un nombre de usuario único 'a23[PrimerNombre][PrimerasLetras]'.
    #    -- Ver si existe ya en el /etc/passwd y… si es así… cambiarle de nombre…
    #        'a25[PrimerNombre][InicialApe1][InicialApe2][DosUltimasCifrasAñoNacimiento]'
    #    - Contraseña "abc123..".
    #    - Que pertenezcan al grupo primario “alumnos” que tienes que crear antes.
	# - Que pertenezca a los mismos secundarios que el usuario jefe.
    #    - home único para cada usuario. /home/cuenta
    #    - /bin/bash como shell por defecto...
# Comando:
# $ useradd -d /home/cuenta -m -g alumnos
# -G [listaGruposSeparadosPorComas]
# -s /bin/bash -p [passwordCifrado] cuenta
aU = "./Usuarios.csv"

with open(aU, "r") as fr:
    laU = fr.readlines()
# print (laU)

comando = "groups jefe"
salida = run(comando, shell=True, capture_output=True, text=True, check=True).stdout.split()[3:]
gSec = ",".join(salida)

for l in laU[1:]:
    dU = {}
    ll = l.split(";")
    cuenta = eliminaTildes(f"a25{ll[2].split()[0]}{ll[0][0]}{ll[1][0]}{ll[7][-2:]}".\
        lower())
    
    pc = cifrar_contraseña("abc123..")
    c = f"useradd -d /home/{cuenta} -m -g alumnos -G {gSec} -s /bin/bash -p \'{pc}\' {cuenta}"
    run(c, shell=True, text=True, check=True)
    print (c)

# Eliminar desde bash los que empiezan por a25
# grep -E "^a25" /etc/passwd | cut -d: -f1 | xargs -I {} sudo userdel -r {}