import os
file=open("miarchivo.txt", "r")
mensaje=file.read()
valores =mensaje.split("\n")
for i in valores:
    print(i)