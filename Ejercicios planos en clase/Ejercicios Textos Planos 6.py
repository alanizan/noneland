import os
nombres =[]

for i in range(10):
    nombres.append(input("Ingrese nombre: "))

file=open("nombre.txt","w")
for nombre in nombres:
    file.write(nombre + "\n")
file.close()

file=open("nombre.txt","r")
datos= file.read()
otros =datos.split("\n")
for i in otros:
    print(i)
    file.close()