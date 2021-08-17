#Define las objetos a utilizar
mayor=0
carros=[]

#define la matriz de 7*3 con ceros
for i in range(3):
    carros.append([0]*5)
    print(carros) # muestra como se crea el arreglo.

#llena la matriz
for p in range (3):
    print("Provincia",(p+1)) #p+1 es para que presente provincia 1 y no CERO
    for m in range(3):
        # En la siguiente linea m+1 es la misma logica de p+1 que muestre 1
        # en vez de CERO.
        cantidad=int(input("Cantidad para el cuatrimestre "+str(m+1)+ ":" ))
        carros[p][m]=cantidad
print(carros[p][m])
#busca el mayor
for p in range(3):
    suma=0 # reinicializa en valor de suma en cada ciclo para resetearlo
    for m in range(3):
        suma+=carros[p][m] #ciclo de acumulacion de [p][m] m(1) m(2) m(3)
    if (suma > mayor):
        mayor=suma #reemplaza el dato mayor acumulado inicia en CERO.
print("La mayor cantidad en una provincia es: ", mayor)
