
# {   'equipo' : String,
#     'discos' : [    {    'disco' : String,
#                     'tamDisco' : Entero,
#                     'modeloDisco' : String,
#                     'particiones' : [   {   'particion' : String,
#                                             'tamParticion' : Entero,
#                                             'fsParti' : String,
#                                             'pMontajeParti' : String },
#                                         { ... },...
#                                     ]},
#                     { ... },... ]
# }

from subprocess import run
from platform import node
from re import sub

run('clear',shell=True)

def InfoEquipo():
    dEquipo = {}
    dInfoEQ = {}

    lDiscos = []
    c = 'fdisk -l'
    sc = run(c, shell=True, capture_output=True, text=True, check=True).stdout
    for l in sc.splitlines():
        if l.startswith('Disco'):
            lDiscos.append(l.split()[1].strip().strip(':'))

    ldDiscos = []
    for disco in lDiscos:
        dInfoDisco = {}
        lParticiones = []
        c = f"fdisk -l --bytes {disco}"
        sc = run(c, shell=True, capture_output=True, text=True, check=True).stdout
        # print(sc)
        for l in sc.splitlines():
            if l.startswith('Disco'):
                tamDisco = int(l.split(',')[1].strip().split()[0])
            elif l.startswith('Modelo de disco'):
                modeloDisco = str(l.split(':')[1].strip())
                # modeloDisco = str(" ".join(l.split()[3:]))  # Otra forma de realizar lo mismo
            elif l.startswith(disco):
                ll = l.split()
                if ('Extendida' not in ll) and ('swap' not in ll):
                    dInfoParti = {}
                    dInfoParti.setdefault('particion',l.split()[0])
                    if ('*' in l.split()[1]):
                        dInfoParti.setdefault('tamParticion',l.split()[5])
                    else:
                        dInfoParti.setdefault('tamParticion',l.split()[4])
                    if ('/dev/nvme' in l.split()[0]):
                        dInfoParti.setdefault('fsParti'," ".join(l.split()[5:]))
                    elif ('/dev/sd' in l.split()[0]):
                        if ('*' in l.split()[1]):
                            dInfoParti.setdefault('fsParti'," ".join(l.split()[7:]))
                        else:
                            dInfoParti.setdefault('fsParti'," ".join(l.split()[6:]))
                    else:
                        pass
                    comando = f"df -Th {l.split()[0]}"
                    salida = run(comando, shell=True, capture_output=True, text=True, check=True).stdout
                    textoSalida = sub('\s+',';', salida)
                    dInfoParti.setdefault('pMontajeParti',textoSalida.strip(';').split(';')[-1])
                    lParticiones.append(dInfoParti)
                else:
                    continue
            else:
                pass

        dInfoDisco.setdefault('disco', disco)
        dInfoDisco.setdefault('tamDisco', tamDisco)
        dInfoDisco.setdefault('modeloDisco', modeloDisco)
        dInfoDisco.setdefault('particiones',lParticiones)

        ldDiscos.append(dInfoDisco)

    dInfoEQ.setdefault('equipo', node())
    dInfoEQ.setdefault('discos', ldDiscos)

    return dInfoEQ

# for k,v in InfoEquipo().items():
#     print(f"{k} : {v}")

for k,v in InfoEquipo().items():
    print(f"{k} :")
    # print(f"      {v}")
    if (isinstance(v,str)):
        print(f"        {v}")
    else:
        for valores in v:
            for a,b in valores.items():
                if (isinstance(b,list)):
                    print(f"        {a} :")
                    for c in b:
                        for d,e in c.items():
                            print(f"                {d} : {e}")
                else:
                    print(f"        {a} : {b}")