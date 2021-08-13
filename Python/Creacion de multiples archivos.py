i = +1
c = int(input("# of .py to create? "))
for i in range(c) : 
 a="Ejercicio-"+str(i)
 filename=a+'.py'
 f=open( filename,'a')

 f.write("")
 f.close()
 i=i+1