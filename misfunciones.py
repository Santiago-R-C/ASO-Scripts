#!/usr/bin/python3

# Importaciones para las funciones de python
from unicodedata import normalize,category
from bcrypt import gensalt, hashpw, checkpw
import socket
import requests
from geopy.distance import distance
from faker import Faker

# Función validación nombres de usuario ############################
def nombreValido(nombre):
    # La salida es un diccionario con dos claves:
    ## valido = True o False
    ## mensaje = ""
    if not nombre.isalnum():
        valido = False
        mensaje = "El nombre de usuario puede contener solo letras y números"
    elif len(nombre) < 6:
        valido = False
        mensaje = "El nombre de usuario debe contener al menos 6 caracteres"
    elif len(nombre) > 12:
        valido = False
        mensaje = "El nombre de usuario no puede contener más de 12 caracteres"
    else:
        valido = True
        mensaje = "Nombre de usuario correcto"
    
    # Creamos el diccionario con la salida
    salida = {}
    salida.setdefault("valido", valido)
    salida.setdefault("mensaje", mensaje)
    return salida
####################################################################

# Función validación contraseñas de usuario ########################
def comprobacionContraseñas(nombre):
    # Las expresiones regulares necesarias
    mayuscula = compile(r'.*[A-ZÑ]+.*')
    minusculas = compile(r'.*[a-zñ]+.*')
    numeros = compile(r'.*[0-9]+.*')
    caracterNoAlfaNum = compile(r'.*[\W]+.*')
    espacios = compile(r'.*[:blank:]+.*')
    # Busqueda con las expresiones regulares
    lMayuscula = mayuscula.findall(nombre)
    lminusculas = minusculas.findall(nombre)
    lnumeros = numeros.findall(nombre)
    lcaracterNoAlfaNum = caracterNoAlfaNum.findall(nombre)
    lespacios = espacios.findall(nombre)
    # Las comprobación de que cumplen los parámetros necesarios
    if len(nombre) < 8:
        valido = False
        print("Hola1")
    elif not lespacios:
        valido = False
        print("Hola2")
    elif nombre:
        contador = 0
        if lMayuscula:
            contador = contador + 1
            print("Holac1")
        if lminusculas:
            contador = contador + 1
            print("Holac2")
        if lnumeros:
            contador = contador + 1
            print("Holac3")
        if lcaracterNoAlfaNum:
            contador = contador + 1
            print("Holac4")
        if contador >= 3 :
            print("Holac5")
            valido = True
        else:
            print("Holac6")
            valido = False
####################################################################

# Elimina tildes ###################################################
def eliminaTildes(s):
    return ''.join(c for c in normalize('NFD', s) if category(c) != 'Mn')
####################################################################

# Cifrar Contraseña ################################################
def cifrar_contraseña(p):
    salt = gensalt()
    password_bytes = p.encode('utf-8')
    pc = hashpw(password_bytes, salt)
    salida = pc.decode('utf-8')
    return salida
####################################################################

# Convertir a formato humano #######################################
def FormatoHumano (unidad_i,capacidad_i):
    capacidad_o = float(0)
    multiplicador = float(1024)
    lista_unidades = ('B','KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB','BiB','GeiB')
    indice_i = lista_unidades.index(unidad_i)
    capacidad_o = capacidad_i
    indice = indice_i

    while True:
        if capacidad_o >= multiplicador:
            capacidad_o = capacidad_o / 1024
            indice += 1
        elif capacidad_o < float(1):
            capacidad_o = capacidad_o * 1024
            indice -= 1
        else:
            break

        if indice == 0 or indice == len(lista_unidades) - 1:
            break
        else:
            pass

    salida = list()
    salida.append(capacidad_o)
    salida.append(lista_unidades[indice])
    return(salida)
####################################################################

####################################################################
def get_geolocation_ipinfo(ip):
    """
    Obtiene detalles de geolocalización usando la API pública de IPinfo.io.
    """

    # URL de la API de IPinfo.io para la IP dada.
    url = f"https://ipinfo.io/{ip}/json"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Lanza excepción si la respuesta no es 200 OK
        data = response.json()
        
        # Verifica si la respuesta contiene un error (ej. IP privada o no encontrada)
        if 'bogon' in data and data['bogon']:
            return None, "IP Privada o Reservada (Bogon)"
        if 'error' in data:
            return None, f"Error en la API: {data['error']['title']}"
        
        # Extracción y formateo de la ubicación
        coords = data.get('loc', 'N/A,N/A').split(',')
        latitude = coords[0]
        longitude = coords[1]

        details = {
            "ip_address": data.get('ip', ip),
            "city": data.get('city', 'N/A'),
            "region": data.get('region', 'N/A'),
            "country": data.get('country', 'N/A'),
            "latitude": latitude,
            "longitude": longitude
        }
        
        return details, None
        
    except requests.exceptions.RequestException as e:
        return None, f"Error de conexión o HTTP: {e}"
    except Exception as e:
        return None, f"Error desconocido: {e}"
####################################################################

####################################################################
def printDetails_ipinfo(ip):
    details, error = get_geolocation_ipinfo(ip)
    
    if error:
        print(f"Error al obtener detalles para {ip}: {error}")
        return

    print(f"IP Address: {details['ip_address']}")
    print(f"Location: {details['city']}, {details['region']}, {details['country']}")
    print(f"Coordinates: (Lat: {details['latitude']}, Lng: {details['longitude']})")
####################################################################

####################################################################
def dameDNI():
    from random import randint

    POSSIBLE_LETTERS = ("T","R","W","A","G","M","Y","F",
        "P","D","X","B","N","J","Z","S","Q","V","H",
        "L","C","K","E","T",)
    NUMBER_DNI = randint(10000000, 99999999)
    LETTER_DNI = POSSIBLE_LETTERS[NUMBER_DNI % 23]
    return f"{NUMBER_DNI}{LETTER_DNI}"
####################################################################

####################################################################
def dameUsuarios(n):
    fake = Faker('es_ES')
    lUsuarios = []

    for _ in range(n):
        dTemp = {}
        dTemp.setdefault('nombre', fake.name())
        dTemp.setdefault('cumple', fake.\
date_of_birth(tzinfo=None, minimum_age=18, maximum_age=55).strftime("%d-%m-%Y"))
        dTemp.setdefault('direccion', fake.address().replace('\n',' '))
        dTemp.setdefault('telefono', fake.phone_number())
        dTemp.setdefault('trabajo', fake.job())
        dTemp.setdefault('dni', dameDNI())
        lUsuarios.append(dTemp)

    return lUsuarios
####################################################################