#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from misfunciones import FormatoHumano

# Vaciar el terminal
run("clear", shell=True)


# 'discos' : [ { 'disco' : '',
#              'tamDisco' : '',
#              'veloDisco' : '',
#              'tipoDisco' : 'mbr o gpt',
#              'particiones' : [ { 'particion' : '',
#                                  'tamParticion' : '',
#                                  'tipoParticion' : 'Extendida, swap, linux...',
#                                  'fs' : '',
#                                  'activa' : True o False,
#                                  'porcenOcupacion' : '',
#                                  'puntoMontaje' : ''},
#                              ]
#             },...
#               ],
# Ejecutar este script con sudo delante

lInfoDiscos = []


# Descubrimos los discos del equipo. Creamos una lista con ellos.
ld = []
c = 'fdisk -l'
sc = run(c, shell=True, capture_output=True, text=True, check=True).stdout
for l in sc.split('\n'):
    if l.startswith('Disco'):
        ld.append(l.split()[1].strip(':'))
# print(ld)

for disco in ld:
    # print(disco)
    dInfoDisco = {}
    dInfoDisco.setdefault('disco',disco)

    c = f"fdisk -l --bytes {disco}"
    sc = run(c, shell=True, capture_output=True, text=True, check=True).stdout

    # print(sc)
    tipoDisco = None
    particiones = []
    for l in sc.split('\n'):
        # print(l)

        if l.startswith('Disco'):
            dInfoDisco.setdefault('tamDisco',l.split(",")[1].strip().split()[0])

        elif l.startswith('Tipo'):
            tipoDisco = l.split(':')[1].strip()

        elif l.startswith(f"{disco}"):
            dInfoParticion = {}
            ll = l.split()

            activa = False
            if ll[1].strip() == '*':
                activa = True
                ll.pop(1)

            particion = ll[0].strip()
            dInfoParticion.setdefault('particion',particion)
            dInfoParticion.setdefault('tamParticion',ll[4].strip())
            tipoParticion = " ".join(ll[6:])
            dInfoParticion.setdefault('tipoParticion',tipoParticion)

            fs = None
            porcenOcupacion = None
            puntoMontaje = None

            if not tipoParticion == 'Extendida' and 'swap' in tipoParticion:
                cdf = f"df -Th {particion}"
                scdf = run(cdf, shell=True, capture_output=True, text=True, check=True).stdout
                llscdf = scdf.split('\n')[1].split()
                fs = llscdf[1]
                porcenOcupacion = llscdf[5]
                puntoMontaje = llscdf[6]
                # print(llscdf)

            dInfoParticion.setdefault('fs',fs)

            dInfoParticion.setdefault('activa',activa)

            dInfoParticion.setdefault('porcenOcupacion',porcenOcupacion)
            dInfoParticion.setdefault('puntoMontaje',puntoMontaje)

            particiones.append(dInfoParticion)
            # print(dInfoParticion)

        else:
            pass

    chdparm = f"hdparm -Tt {disco}"
    schdparm = run(chdparm, shell=True, capture_output=True, text=True, check=True).stdout
    dInfoDisco.setdefault('veloDisco',f"{schdparm.strip().split()[22]} {schdparm.strip().split()[23]}")

    dInfoDisco.setdefault('tipoDisco',tipoDisco)
    if particiones == []:
        particiones = None
    dInfoDisco.setdefault('particiones',particiones)

    lInfoDiscos.append(dInfoDisco)

# for dd in lInfoDiscos:
    # print(dd)
print(lInfoDiscos)



# sudo fdisk -l
# sudo hdparm -tT /dev/sda
# df -h /dev/sda1
