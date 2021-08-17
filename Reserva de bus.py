bus1 = []
bus2 = []
bus3 = []
bus4 = []

#define la matriz de 50 * 60 con ceros
for i in range(5):
    bus1.append([0]*4)
    bus2.append([0]*4)
    bus3.append([0]*4)
    bus4.append([0]*4)
bus = int(input("Cual bus desea? "))
espacio = int(input("Cual espacio desea? "))
horario = int(input("Cual horario desea? "))
if bus == 1:
    bus1[horario][espacio] = 1
if bus == 2:
    bus2[horario][espacio] = 1
if bus == 3:
    bus3[horario][espacio] = 1
if bus == 4:
    [horario][espacio] = 1

print(bus1)
print(bus2)
print(bus3)
print(bus4)


'''last_month_sales = ["Vauxhall Corsa 2011", "Nissan Note 2014", "Honda Civic 2012", "Vauxhall Corsa 2015", "Vauxhall Mokka 2013", "Hyundai I20 2016"]

print(len(last_month_sales))


last_month_sales = ["Vauxhall Corsa 2011", "Nissan Note 2014", "Honda Civic 2012", "Vauxhall Corsa 2015", "Vauxhall Mokka 2013", "Hyundai I20 2016"]

for car in range(0, len(last_month_sales)):
	print(last_month_sales[car])'''
