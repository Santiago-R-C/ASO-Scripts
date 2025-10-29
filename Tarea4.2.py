
# Importaciones para python
from subprocess import run
from re import findall
from ipaddress import IPv4Address

# Vaciar el terminal
run("clear", shell=True)

dInfoAuthLog = {}                   # Diccionario con toda la información
a = './auth.log'                    # Archivo auth.log
archivo_salida = './salida.json'    # Archivo de salida

ppl = r'for\s+.*(?:[0-9]{1,3}\.){3}[0-9]{1,3}'

with open(a, "r") as fr:
    for l in fr:
        if ': Failed password' in l:
            uEntro = False
        elif ': Accepted password' in l:
            uEntro = True
        else:
            continue
        lpl = findall(ppl,l)[0].split()
        ip = lpl[-1]
        if ' '.join(lpl[1:3]) == 'invalid user':
            usuario = lpl[3]
            if usuario == 'from':
                usuario = 'Blank'
        else:
            usuario = lpl[1]
        # Completamos el diccionario (json) con toda la información
        if ip not in dInfoAuthLog:  # La ip no está en el diccionario
            dInfoIp = {}
            uNo = []
            uSi = []
            # Comprobamos si la ip es pública o privada
            dInfoIp.setdefault('privada',IPv4Address(ip).is_private)
            dInfoIp.setdefault('uNo',uNo)
            dInfoIp.setdefault('uSi',uSi)
            dInfoAuthLog.setdefault(ip,dInfoIp)
        else:                       # La ip ya está en el diccionario
            pass

        # Rellenamos la lista correspondiente con el usuario - Debe ser único en la lista
        if uEntro:
            if usuario not in dInfoAuthLog[ip]['uSi']:
                dInfoAuthLog[ip]['uSi'].append(usuario)
        else:
            if usuario not in dInfoAuthLog[ip]['uNo']:
                dInfoAuthLog[ip]['uNo'].append(usuario)

with open(archivo_salida,'w') as fw:
    fw.write('{\n')
    for i, (k, v) in enumerate(dInfoAuthLog.items()):
        fw.write(f"\"{k}\": " + "{")
        for l, (claves, valores) in enumerate(v.items()):
            fw.write(f"\"{claves}\": ")
            if not isinstance(valores, list):
                if valores == True:
                    fw.write(f"true")
                else:
                    fw.write(f"false")
            else:
                fw.write("["+", ".join(f"\"{usuario}\"" for usuario in valores)+"]")
            if l < len(v) - 1:
                fw.write(',')
        fw.write('}\n')
        if i < len(dInfoAuthLog) - 1:
            fw.write(',')
    fw.write('}')