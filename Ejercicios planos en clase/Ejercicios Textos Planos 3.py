import os
file=open("miarchivo.txt", "r")
mensaje=file.read()
print(mensaje)
file.close()