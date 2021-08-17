#imprimir lista
lista = []

filas = int(input("Cuantas filas? "))
columnas = int(input("Cuantas columnas? "))

for i in range(filas):
    lista.append([0]*columnas)
    int(input("ingrese numero: "))
print(lista)

for x in range(lista):
    for m in range(lista):
        int(input("ingrese numero: "))
