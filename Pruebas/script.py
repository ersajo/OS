import os
import commands
import threading

def comandos(string):
    cadena = commands.getoutput('sudo find / -name "*.' + string + '"')
    lista = cadena.split("\n")

    for line in lista:
        if line[0] == '/':
            os.system("sudo cp " + line + " /home/erick/Documentos/OS/Pruebas/Ejemplo1/" + string + "/")
    cadena = commands.getoutput('sudo find /home/erick/Documentos/OS/Pruebas/Ejemplo1/' + string + '/ -name "*.' + string + '"')
    lineas = cadena.split("\n")
    for line in lineas:
        os.system("sudo chmod 666 " + line)
        os.system("sudo chown erick:erick " + line)
    os.system("ls -l /home/erick/Documentos/OS/Pruebas/Ejemplo1/" + string + "/")

os.system("mkdir /home/erick/Documentos/OS/Pruebas/Ejemplo1/")
os.system("mkdir /home/erick/Documentos/OS/Pruebas/Ejemplo1/img/")
os.system("mkdir /home/erick/Documentos/OS/Pruebas/Ejemplo1/pdf/")
os.system("mkdir /home/erick/Documentos/OS/Pruebas/Ejemplo1/sh/")


img = threading.Thread(target=comandos, args=('img',))
pdf = threading.Thread(target=comandos, args=('pdf',))
sh = threading.Thread(target=comandos, args=('sh',))

img.start()
pdf.start()
sh.start()
