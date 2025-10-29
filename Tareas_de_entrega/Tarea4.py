
# Importaciones para python
from re import findall
from misfunciones import get_geolocation_ipinfo

# # Vaciar el terminal
# from subprocess import run
# run("clear", shell=True)

aAuthLog = './auth.log'         # Archivo auth.log
archivo_salida = './salida.json'
dInfoAuthLog = {}               # Diccionario de salida (JSON) con toda la información

patronIP = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
patronUsu = r"Failed password for (.*)"

with open(aAuthLog, "r") as fr:
    for l in fr:
        if 'Failed password for' in l:
            l = l.strip()
            ip = findall(patronIP,l)[0]
            lUsu = findall(patronUsu,l)[0].split()
            if not " ".join(lUsu[0:2]) == 'invalid user':
                usuario = lUsu[0]
            else:
                if not lUsu[2] == 'from':
                    usuario = lUsu[2]
                else:
                    usuario = "Blank"
            if ip not in dInfoAuthLog:
                dInfoIp = {}
                info, error = get_geolocation_ipinfo(ip)
                try:
                    dInfoIp.setdefault("ciudad",f"\"{info['city']}\"")
                except:
                    dInfoIp.setdefault("ciudad",None)
                try:
                    dInfoIp.setdefault("region",f"\"{info['region']}\"")
                except:
                    dInfoIp.setdefault("region",None)
                try:
                    dInfoIp.setdefault("pais",f"\"{info['country']}\"")
                except:
                    dInfoIp.setdefault("pais",None)
                try:
                    dInfoIp.setdefault("latitud",f"\"{info['latitude']}\"")
                except:
                    dInfoIp.setdefault("latitud",None)
                try:
                    dInfoIp.setdefault("longitud",f"\"{info['longitude']}\"")
                except:
                    dInfoIp.setdefault("longitud",None)
                usuarios = []
                usuarios.append(usuario)
                dInfoIp.setdefault("usuarios",usuarios)
                dInfoAuthLog.setdefault(ip,dInfoIp)
            else:
                if usuario not in dInfoAuthLog[ip]['usuarios']:
                    dInfoAuthLog[ip]['usuarios'].append(usuario)
                pass

with open(archivo_salida,'w') as fw:
    fw.write("{\n")
    for i, (ip, valores) in enumerate(dInfoAuthLog.items()):
        fw.write(f"\"{ip}\""+': {')
        for k,v in valores.items():
            fw.write(f"\"{k}\": ")
            if v == None:           # Cambie el valor None a null, porque la extensión que
                fw.write(f"null,")  # tengo me indica que con null no genera ningun error
            else:                   # (creo que se devería de poner clave: null en el json)
                if not isinstance(v, list):
                    fw.write(f"{v},")
                else:
                    fw.write("["+", ".join(f"\"{usuario}\"" for usuario in v)+"]")
        fw.write("}")
        if i < len(dInfoAuthLog) - 1:
            fw.write(",\n")
        else:
            fw.write("\n")
    fw.write("}")
