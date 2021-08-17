import os
file=open("miarchivo2.txt", "r")
mensaje=file.read()
valores =mensaje.split("\n")
#file.close()
for i in valores:
    print(i)
file.close() #si no se cierra el archivo no se puede borrar
os.remove("miarchivo2.txt")