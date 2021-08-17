'''mayor=0
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
        print(estudiantes)'''


mayor=0
import random
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
        cantidad=random.randint(0,100)
        estudiantes[e][m] = cantidad
        print(estudiantes[e][m])
print(estudiantes)