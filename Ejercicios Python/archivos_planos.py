# semana 11 archivos planos presentacion

import os
file=open("miarchivo.txt", "w")
file.write("Mi primer texto")
file.write("escrito en Python")
file.close()


'''import os
file=open("miarchivo.txt", "w")
file.write("Mi primer texto\n")
file.write("escrito en Python mejorado ")
file.close() '''


'''import os
file=open("miarchivo.txt", "a")
file.write("Mi primer texto\n")
file.write("escrito en Python mejorado ")
file.write("Mi primer texto\n")
file.write("escrito en Python mejorado ")
file.write("Mi primer texto\n")
file.write("escrito en Python mejorado ")
file.close() '''

'''import os
file=open("miarchivo.txt", "r")
mensaje=file.read()
print(mensaje)
file.close()'''

import os
file=open("miarchivo.txt", "r")
mensaje=file.read()
valores =mensaje.split("\n")
for i in valores:
    print(i)


'''import os
file=open("miarchivo2.txt", "r")
mensaje=file.read()
valores =mensaje.split("\n")
for i in valores:
    print(i)
#file.close() #si no se cierra el archivo no se puede borrar
os.remove("miarchivo2.txt")'''



'''import os
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
    file.close()'''

'''
*/*/*/*/*/**/ gestion de archivos texto

import os

def agregar():
    if os.path.isfile('agenda.txt'):
        print('El archivo existe.')
        f = open ("agenda.txt", "a")
        nombre = input('Ingrese nombre persona: ')
        telefono = input('Ingrese numero teléfono: ') 
        direccion = input('Ingrese dirección: ') 
        print(nombre, telefono, direccion, file=f)
    else:
        print("-----------")
        print('El no archivo existe, debe crearlo primero opción 3')
        print("-----------\n")
    

def borrar():
    if os.path.isfile('agenda.txt'):
        print('El archivo existe.')
        confir=input("Desea borrar la agenda? S/N")
        if confir == "s" or confir == "S":
            os.remove("agenda.txt")
    else:
        print("-----------")
        print('El no archivo existe, debe crearlo primero ir a opción 4')
        print("-----------\n")


def crear():
    if os.path.isfile('agenda.txt'):
        print("-----------")
        print('El archivo existe.')
        print("-----------\n")
    else:
        f = open('agenda.txt', 'wt')
        n = 0
        while n < 1:
            n = int( input('¿Cuántas personas va a agregar a la agenda? ') )
        while n > 0:
            nombre = input('Ingrese nombre persona: ')
            telefono = input('Ingrese numero teléfono: ') 
            direccion = input('Ingrese dirección: ') 
            print(nombre, telefono, direccion, file=f)
            n=n-1
        f.close()


def mostrar():
    f=open("agenda.txt", "r")
    mensaje=f.read()
    valores =mensaje.split("\n")
    for i in valores:
        print(i)

              
def respaldar():
    f = open("agenda.txt", "r")
    f2 = open("agendares.txt", "w")
    linea=f.readline()
    while linea != "":
        f2.write(linea)
        linea=f.readline()
    f.close
    f2.close

def pedirNumero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Por favor ingrese algún número de opción: "))
            correcto=True
        except ValueError:
            print('Error, Ingrese un número entero')
     
    return num
 
salir = False
opcion = 0

while not salir:
 
    print ("1. Agregar")   
    print ("2. Borrar Agenda") 
    print ("3. Crear")     
    print ("4. Mostrar")   
    print ("5. Respaldar la Agenda")   
    print ("6. Salir")
     

 
    opcion = pedirNumero()
 
    if opcion == 1:
        agregar()
    elif opcion == 2:
        borrar()
    elif opcion == 3:
        crear()
    elif opcion == 4:
        mostrar()
    elif opcion == 5:
        respaldar()
    elif opcion == 6:
        salir = True
    else:
        print ("Ingrese una opción entre 1 y 6")
 
print ("Gracias por usar nuestra agenda")'''



