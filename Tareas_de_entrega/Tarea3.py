#!/usr/bin/python3

# Importaciones para python
from subprocess import run
from re import compile
from datetime import datetime
from requests import get
from time import sleep

# Vaciar el terminal
run("clear", shell=True)

# Solicitud de subrde
subred = input(f"Dame una subred: ")

# Expresión regular de subred
e = compile(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}")
comprobacionIP = e.findall(subred)

# If-else para comprobar si es una subred
if subred == comprobacionIP[0]:
    # Separación de ip y máscara
    ip = subred.split("/")[0].strip()
    mascara = subred.split("/")[1].strip()

    # Nombre archivo de salida
    archivo_salida = f"hostsRed_{ip}_"+datetime.now().strftime("%Y_%m_%d_%H_%M")+".csv"

    # Comando fping
    Cfping = f"fping -g {ip}/{mascara} -a -q -e"
    # Salida comando fping
    Sfping = run(Cfping, shell=True, capture_output=True, text=True).stdout
    for l in enumerate(Sfping.split("\n")):
        dEquipo = {}
        # if-else para una linea que queda en blanco al hacer el fping
        if l[1]:
            # Añadir ip al diccionario dEquipo
            dEquipo.setdefault("ip",l[1].split()[0])
            # Añadir latencia_ms al diccionario dEquipo
            dEquipo.setdefault("latencia_ms",l[1].split()[1].strip('('))
        else:
            continue
        
        # Comando para obtener la mac a partir de la ip
        CipNeigh = f"ip neigh show {l[1].split()[0]}"
        # Try-except por si alguna ip no tiene mac (VirtualBox)
        try:
            SipNeigh = run(CipNeigh, shell=True, capture_output=True, text=True, check=True).stdout.split()[4]
        except:
            SipNeigh = "none"
        # Añadir mac al diccionario dEquipo
        dEquipo.setdefault("mac",SipNeigh)

        if SipNeigh == "none":
            dEquipo.setdefault("fabricante", "none")
        else:
            # Petición de la mac a la api
            url = f'https://api.macvendors.com/{SipNeigh}' # Con macs reales funciona
            response = get(url)

            # If-else para comprobar si la api devuelve un valor válido
            if response.status_code == 200:
                # Añadir fabricante al diccionario dEquipo
                dEquipo.setdefault(f"fabricante",response.text)
                # Tiempo de 1,5 segundos entre peticiones para que no de problemas la api
                sleep(1.5)
            else:
                # Añadir fabricante al diccionario dEquipo
                dEquipo.setdefault("fabricante", "none")

        texto = (f"{dEquipo['ip']};{dEquipo['mac']};{dEquipo['fabricante']};{dEquipo['latencia_ms']}\n") # Real
        
        # Escribimos los datos en el archivo archivo_salida
        with open(archivo_salida,'a') as fw:
            fw.write(texto)

else:
    print ("-"*100)
    print (f"Subred inválida o inexistente\nIp separada con puntos y formato ip/mascara")
    print ("-"*100)



