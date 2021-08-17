def registro():
    datos_persona = []
    tarjeta_cred = []
    a_nombre = []
    a_cedula = []
    a_edad = []

    txt = open('registro.txt', 'w')
    n = str(input("Favor ingresar el nombre de la persona a registrar: "))
    id = str(input("Ingrese numero de identificacion de la persona a registrar en formato 0-0000-0000: "))
    localidad = str(input("Ingrese ubicacion en el siguiente formato: País, provincia, cantón, distrito y otras especificaciones de dirección. "))
    pago = int(input("Forma de pago:\n1- Efectivo, \n2- Transferencia bancaria\n3- Tarjeta de credito/debito: "))
    if pago == "1":
        pago = "Efectivo"
        print("Favor cancelar en recepcion una vez se encuentre en el sitio")
    elif pago == "2":
        pago == "Transferencia bancaria"
        iban = str(input("Ingrese el numero IBAN para la transferencia de fondos:" ))
    elif pago == "3":
        pago == "Tarjeta de credito/debito"
        tarj_num = str(input("Ingrese numero de la tarjeta de debito:" ))
        n_tarjeta = str(input("Ingrese el nombre del tarjetahabiente:" ))
        caducidad = str(input("Ingrese fecha de expiracion en el siguiente formato MM/YY: "))
        cod_seg = str(input("Ingrese codigo de seguridad: "))
        tarjeta_cred.append(tarj_num)
        tarjeta_cred.append(n_tarjeta)
        tarjeta_cred.append(caducidad)
        tarjeta_cred.append(cod_seg)

    datos_persona.append(n)
    datos_persona.append(id)
    datos_persona.append(localidad)
    datos_persona.append(pago)
    print(datos_persona, file = txt)
    print("Bienvenido", datos_persona[0])

    acompanantes = int(input("Indique el numero de personas le acompañan? "))

    if acompanantes >= 1:
        for x in range(acompanantes):
            acompanante_nombre = str(input("Ingrese el nombre de persona a registar: "))
            a_nombre.append(acompanante_nombre)
            acompanante_cedula = str(input("Ingrese la cedula de la persona a registar: "))
            a_cedula.append(acompanante_cedula)
            acompanante_edad = str(input("Edad del acompañante: "))
            a_edad.append(acompanante_edad)

    print("Datos de las personas que lo acompañan para su referencia")
    for i in range(acompanantes):
        print()
        print("Nombre: ",a_nombre[i])
        print("Cedula:", a_cedula[i])
        print("Edad:", a_edad[i])
        print()

    dueno_reservacion = 1 
    total_reservas = dueno_reservacion + acompanantes
    print("Numero total de reservaciones", total_reservas)


registro()