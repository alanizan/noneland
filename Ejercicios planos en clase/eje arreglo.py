#Carga una lista y mostrar datos'''
a = [[1, 2, 3], [4, 5, 6]]
print(a[0])         #muestra primera serie de elementos
print(a[1])         #muestra segunda lista de elementos
b = a[0]            #crea un elemento "b" que contiene 1-2-3
print(b)            #Lo muestra
print(a[0][2])      #muestra la posicion A cero posicion 2 ="3"
a[0][1] = 7         #cambia 2 por un 7 en serie 0 y el objeto B TB que lo referencia
print(a)            #muestra a lista
print(b)            #muestra la otra lista B
b[2] = 9            #cambia 3 * 9
print(a[0])         #imprime primera serie de A
print(b)            #imprime B con sus datos'''

