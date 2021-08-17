cedula = input("Numero de cedula en formato 0-0000-0000? ")
nombre = input("Nombre? ")
salario = int(input("Monto de salario? "))
ccss = (salario * 0.08)
bp = salario * 0.01
dedu = ccss + bp
salario_neto = salario-dedu
print("Salario Bruto:",+salario)
print("8% de la Caja:",+ccss)
print("1% Banco Popular:",+bp)
print("Total de deducciones:",+dedu)
print("Salario neto:",+salario_neto)
