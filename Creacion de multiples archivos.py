i = +1
c = int(input("Numero de ficheros .py a crear "))
for i in range(c) : 
 a="Ejercicio"+str(i+1)
 filename=a+'.py'
 f=open( filename,'a')

 f.write("")
 f.close()
 i=i+1