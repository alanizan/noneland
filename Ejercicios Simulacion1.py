mayor=0
estudiantes=[]



#define la matriz de 7*3 con ceros
for i in range(3):
    estudiantes.append([0]*5)
    print(estudiantes) # muestra como se crea el arreglo.


#llena la matriz
for e in range (3):
    print("Curso",(e+1)) #p+1 es para que presente provincia 1 y no CERO
    for m in range(5):
        # En la siguiente linea m+1 es la misma logica de p+1 que muestre 1
        # en vez de CERO.
        cantidad=int(input("Nota final de estudiante "+str(m+1)+ ":" ))
        estudiantes[e][m]=cantidad



print(estudiantes)
for p in range(3):
    suma=0 # reinicializa en valor de suma en cada ciclo para resetearlo
    for m in range(5):
        suma+=estudiantes[e][m] #ciclo de acumulacion de [p][m] m(1) m(2) m(3)
        promedio = suma / len(estudiantes[e])
        print("Promedio de clase"+str(e),promedio)
    '''if (suma > mayor):
        mayor=suma #reemplaza el dato mayor acumulado inicia en CERO.'''
        


