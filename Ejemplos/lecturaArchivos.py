#!/usr/bin/python3

# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

pathArchivo = "/proc/meminfo"

# # Lectura del archivo entero (Poco usado)
# fr = open(pathArchivo, "r")
# textoArchivo = fr.read()
# fr.close()

# # # # # -------------------------------------------------- # # # # #

# # Lectura del archivo entero, más usado
# with open(pathArchivo, "r") as fr:
#     textoArchivo = fr.read()
# print(textoArchivo)

# # # # # -------------------------------------------------- # # # # #

# # Lectura del archivo línea a línea
# with open(pathArchivo, "r") as fr:
#     for linea in fr:
#         print(linea.strip())

# # # # # -------------------------------------------------- # # # # #

# # Lectura del archivo línea a línea, más usado
# with open(pathArchivo, "r") as fr:
#     for linea in fr:
#         if linea.strip().startswith("SwapTotal"):
#             print(linea.strip())
#             break
#         else:
#             pass

# # # # # -------------------------------------------------- # # # # #

# # Lectura del archivo línea a línea e incorporamos nun diccionario
# dMemInfo = {}
# with open(pathArchivo, "r") as fr:
#     for linea in fr:
#         ll = linea.split(":") # Dividimos a línea nunha lista de dous campos
#         k = ll[0].strip()   #Clave = Elemento 0 da lista e limpo
#         if len(ll) == 2:
#             v = ll[1].strip()   #Valor = Elemento 1 da lista e limpo
#         else:
#             v = ""  #Se non hai valor, o poñemos cun string baleiro
#         dMemInfo.setdefault(k,v)
# print(dMemInfo)

# # # # # -------------------------------------------------- # # # # #

# # Lectura del archivo línea a línea e incorporamos nun diccionario, más usado
# dMemInfo = {}
# with open(pathArchivo, "r") as fr:
#     la = fr.readlines()
# print(la)
# for linea in la:
#     ll = linea.split(":") # Dividimos a línea nunha lista de dous campos
#     k = ll[0].strip()   #Clave = Elemento 0 da lista e limpo
#     if len(ll) == 2:
#         v = ll[1].strip()   #Valor = Elemento 1 da lista e limpo
#     else:
#         v = ""  #Se non hai valor, o poñemos cun string baleiro
#     dMemInfo.setdefault(k,v)
# print(dMemInfo)