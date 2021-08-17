
c = int(input("Numero de ficheros .py a crear"))
for i in range(c) : 
 a="Practica"+str(i+1)
 filename=a+'.py'
 f=open( filename,'a')

 f.write("")
 f.close()
 i=i+1