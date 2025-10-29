#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from pathlib import Path

# Vaciar el terminal
run("clear", shell=True)

d = './datos'
directorio = Path(d)
archivos = list(directorio.glob('*.data'))
ruta_out = Path('./out')

ds = './datos/out/'
Pds = Path(ds)
try:
    Pds.mkdir(parents=True)
except:
    run("clear", shell=True)

for a in archivos:
    pa = f"{d}{a.name}"
    ssa = ""
    with a.open('r') as fr:
        for linea in fr:

            valores = list(map(int,linea.strip().split()))
            try:
                maximo = max(valores)
                minimo = min(valores)
                media = round(sum(valores) / len(valores),2)
                ssl = f"{maximo} {minimo} {media}\n"
            except:
                ssl = "\n"
            ssa += ssl

    with open(f"{ds}{a.name}.out",'w') as fw:
        fw.write(ssa)