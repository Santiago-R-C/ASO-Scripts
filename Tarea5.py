
# dInfoUsuario = {
#           usuario1: {
#                      id: Entero,
#                      grupoPrin: String,
#                      gruposSec: Lista,
#                      pathHome: String,
#                      tamHome: Entero (los Bytes del tamaño del home), du -sb pathHome
#                      shell: String
#                      inicia: True o False (estudiar /etc/shadow si tiene password ahí)
#           },
#           usuario2: {},
#           usuario3: {},...
# }

# Importaciones para python
from subprocess import run
from datetime import datetime
from misfunciones import getInfoUsuarios, FormatoHumano

# # Vaciar el terminal
# run("clear", shell=True)

# Variables fecha y hora
fecha = datetime.now().strftime("%d/%m/%Y")
hora = datetime.now().strftime("%H:%M:%S")

archivo_salida = "./Tarea5.html"

# def getInfoUsuarios():
#     # Lista de Usuarios
#     dInfoUsuarios = {}
#     # Nombre del equipo
#     com = f"hostname"
#     nombre_equipo = run(com, shell=True, capture_output=True, text=True, check=True).stdout

#     # Diccionario de Contraseñas
#     dShadow = {}

#     # Ubicación de los archivos y permisos para poder abrirlos
#     aPasswd = "/etc/passwd"
#     aShadow = "/etc/shadow"

#     # Apertura del archivo aShadow
#     with open(aShadow, "r") as fr:
#         for l in fr:
#             ll = l.split(":")
#             dShadow.setdefault(ll[0], len(ll[1]) > 1)

#     # Apertura del archivo aPasswd
#     with open(aPasswd, "r") as fr:
#         for l in fr.readlines():
#             dUsuario = {}
#             ll = l.split(":")
#             id = int(ll[2].strip())
#             if (1000 <= id <= 60000 or id == 0):
#                 # Implementación del id en el diccionario dUsuario
#                 dUsuario.setdefault("id", int(ll[2].strip()))

#                 # Implementación del grupoPrincipal y los gruposSecundarios en el diccionario dUsuario
#                 comando = f"groups {ll[0]}"
#                 salida = run(comando, shell=True, capture_output=True, text=True, check=True).stdout.split(":")[1].strip().split()
#                 dUsuario.setdefault("grupoPrin", str(salida[0]))
#                 dUsuario.setdefault("gruposSec", list(salida[1:]))

#                 # Implementación del tamHome y el pathHome en el diccionario dUsuario
#                 dUsuario.setdefault("pathHome", str(ll[5].strip()))
#                 comando = f"sudo du -sb {ll[5]}"
#                 salida = run(comando, shell=True, capture_output=True, text=True).stdout.strip().split()[0]
#                 dUsuario.setdefault("tamHome", salida)

#                 # Implementación de la shell en el diccionario dUsuario
#                 dUsuario.setdefault("shell", ll[6].strip())

#                 # Implementación de la contraseña en el diccionario dUsuario

#                 dUsuario.setdefault("inicia", dShadow[ll[0].strip()])

#                 # Agregamos el diccionario dUsuario al diccionario dInfoUsuarios
#                 dInfoUsuarios.setdefault(ll[0].strip(),dUsuario)
#     return nombre_equipo, dInfoUsuarios.items()

# Variables salidas de la función
nombre, infoUser = getInfoUsuarios()

# Otras variables
contador = 0

# Creación del html
with open(archivo_salida,'w') as fw:
    fw.write("<!DOCTYPE html>")
    fw.write("<html lang='es'>")
    fw.write("<head>")
    fw.write("<meta charset='UTF-8'>")
    fw.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
    fw.write("<link rel='stylesheet' href='estilos/estilos.css' type='text/css'>")
    fw.write(f"<title>Usuarios {nombre}</title>")
    fw.write("</head>")
    fw.write("<body>")
    fw.write("<table>")
    fw.write(f"<caption>USUARIOS DEL EQUIPO {nombre}")
    fw.write("<br>")
    fw.write(f"FECHA: {fecha} HORA: {hora}</caption>")
    fw.write("<thead>")
    fw.write("<tr>")
    fw.write("<th>Usuario</th>")
    fw.write("<th>ID usuario</th>")
    fw.write("<th>Grupo Principal</th>")
    fw.write("<th>Grupos Secundarios</th>")
    fw.write("<th>Directorio personal</th>")
    fw.write("<th>Tamaño home</th>")
    fw.write("<th>Shell</th>")
    fw.write("<th>Inicia</th>")
    fw.write("</tr>")
    fw.write("</thead>")
    fw.write("<tfoot>")
    fw.write("<tr>")
    fw.write("<td colspan='8'>IES San Clemente</td>")
    fw.write("</tr>")
    fw.write("</tfoot>")
    fw.write("<tbody>")
    for usuario, valores in infoUser:
        contador += 1
        if int(valores["tamHome"])>20971520:
            fw.write("<tr class='rojo'>")
        elif (contador%2) == 0:
            fw.write("<tr>")
        else:
            fw.write("<tr class='fimpar'>")
        fw.write(f"<td>{usuario}</td>")
        for k, v in valores.items():
            if k == "tamHome":
                cantidad, unidad = FormatoHumano('B',int(v))
                fw.write(f"<td>{round(cantidad, 2)} {unidad}</td>")
            else:
                fw.write(f"<td>{v}</td>")

    fw.write("</tr>")
    fw.write("</tbody>")
    fw.write("</table>")
    fw.write("</body>")
    fw.write("</html>")
