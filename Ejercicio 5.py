notas = []
nombres = []
acum_notas = 0

def incluir():
    cantidad = int(input("Por Favor ingresar la cantidad de alumnos"))
    for i in range(cantidad):
        notas.append([0]*cantidad)
    for p in range(cantidad):
        nombres.append(input("Nombre del Alumno: "))
        print("Alumno", (p+1),":",nombres[p])
        for m in range(5):
            nota = int(input("Ingrese nota"+str(m+1)+": "))
            notas[p][m] = nota
        for i in range(cantidad):
            print(nombres[i],notas[i],'\n')

incluir()