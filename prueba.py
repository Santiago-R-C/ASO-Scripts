
# Importaciones para python
from subprocess import run

# Vaciar el terminal
run("clear", shell=True)

def infoUsuario(nombre):
    a = '/etc/passwd'
    with open(a,'r') as fr:
        for l in fr.readlines():
            ll = l.strip().split(":")
            try:
                if ll[0] == nombre.strip():
                    dUsuario = {}
                    
                    dUsuario.setdefault("nombre",ll[0])
                    comando = f"id {ll[0]}"
                    salida = run(comando, shell=True, capture_output=True, text=True, check=True).stdout.strip().split()[0].split("=")[1].split("(")[0]
                    dUsuario.setdefault("uid",salida)

                    comando = f"groups {ll[0]}"
                    salida = run(comando, shell=True, capture_output=True, text=True, check=True).stdout.strip().split()
                    dUsuario.setdefault("grupoPrin",salida[0])
                    dUsuario.setdefault("gruposSec",",".join(salida[2:]))
                    
                    dUsuario.setdefault("home",ll[5])

                    comando = f"sudo du -sh {ll[5]}"
                    salida = run(comando, shell=True, capture_output=True, text=True, check=True).stdout.strip().split()[0]
                    dUsuario.setdefault("tamHome",salida)
                    return dUsuario
                else:
                    pass
            except:
                print(None)
            
nombre = input("Dame un nombre: ")
resultado = infoUsuario(nombre)
print(resultado)