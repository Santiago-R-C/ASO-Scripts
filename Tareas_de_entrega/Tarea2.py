#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from datetime import datetime
from re import sub

# Vaciar el terminal
run("clear", shell=True)

# Listas
listas_de_lineas = []
lista_users = []

# Comando top -bn1 -o %MEM
comando = "top -bn1 -o %MEM"
salida = run(comando, shell=True, capture_output=True, text=True, check=True).stdout

# Separar la salida en lineas
lineas = salida.splitlines()

# Mostrar cada línea como lista
for i, linea in enumerate(lineas):
    if "PID" in linea:
        textoSalida = lineas[i+1:]
        for l in textoSalida:
            ll = sub(r'\s+', ';', l.strip()).split(";")
            listas_de_lineas.append(ll)

# Mostrar cada línea como lista
for fila in listas_de_lineas:

    # Convertir la fila[9] que es la memoria a un float que se pueda comparar
    memoria_str = sub(r',', '.', sub(r'%MEM', '1.0', fila[9]))
    memoria_en_puntos = float(memoria_str)

    # Comparar si memoria_en_puntos es superior a 0.0
    if memoria_en_puntos > 0.0:
        dUser = {}
        # Insertar el user, command, cpu, mem, pid a dUser
        dUser.setdefault("user",fila[1])
        dUser.setdefault("command",fila[11])
        dUser.setdefault("cpu",fila[8])
        dUser.setdefault("mem",fila[9])
        dUser.setdefault("pid",fila[0])
        
        # Comando ps -f {pid}
        comando = f"ps -f {fila[0]}"

        # Intento con try except por si da error que de valor nulo
        try:
            salida = run(comando, shell=True, capture_output=True, text=True, check=True).stdout
            partes = sub(r'\s+', ';', salida).split(";")
            ppid = partes[11]
        except:
            ppid = "null"
        
        # Insertar el ppid a dUser
        dUser.setdefault("ppid",ppid)

        # Meter todos los valores del diccionario dUser a la lista lista_users
        lista_users.append(dUser)

# Guardar archivo de nombre la top_fecha.csv
nombre_archivo = "top_"+datetime.now().strftime("%Y_%m_%d_%H_%M")+".csv"
with open(nombre_archivo,"w") as fw:
    # fw.write("Generado archivo:"+nombre_archivo+"\n\n")   # Para ver el nombre del archivo que se genera dentro del archivo
    fw.write("USER;COMMAND;%CPU;%MEM;PID;PPID\n")
    for i in lista_users:
        linea = ';'.join(v for k, v in i.items())
        fw.write(linea + '\n')
