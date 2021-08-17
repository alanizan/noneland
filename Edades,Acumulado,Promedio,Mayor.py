edades = []
acum_edades = 0
prome_edades = 0

for x in range(3):
    edad = int(input("Ingrese edad "))
    edades.append(edad)
for x in range(3):
    acum_edades=acum_edades+edades[x]
print("El acumulado de edades es de: ",acum_edades)
prome_edades=acum_edades/len(edades)
print("El promedio es de", prome_edades)
for x in range(3):
    if edades[x]>prome_edades:
        print(edades[x])