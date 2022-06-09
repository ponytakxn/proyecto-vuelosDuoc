import numpy as np

asientoNormal = 78900
asientoVip = 240000

def verAsientos(listaAsientos):
    print(listaAsientos)
    print("¿Qué desea hacer?")
    print("1. Comprar asiento")
    print("2. Volver al menú")

def comprarAsiento(listaAsientos):
    print("Para comenzar con su compra necesitamos que ingrese sus datos.")
    nom=input("Ingrese su nombre: ")
    rut=int(input("Ingrese su rut sin puntos ni guión, si su rut termina en K reemplazar por un 0: "))
    while rut < 50000000 or rut > 300000000:
        print("Rut no válido. Vuelva a ingresar su rut: ")
        rut=int(input())
    telefono=int(input("Ingrese su teléfono (formato 9 dígitos sin +56): "))
    while telefono < 199999999 or telefono > 999999999:
        print("Teléfono ingresado no válido. Vuelva a ingresar su teléfono (formato 9 dígitos sin +56): ")
        telefono=int(input())
    print("Ingrese su banco: ")
    print("1. Banco Santander")
    print("2. Banco Falabella")
    print("3. Banco Duoc")
    print("4. Otro banco")
    banco=int(input())
    while banco < 1 or banco > 4:
        print("Banco seleccionado no válido. Vuelva a ingresar su banco: ")
        banco=int(input())
    print("")
    print("Seleccione su asiento. Los asientos marcados con una X no se encuentran disponibles.")
    print(listaAsientos)
    print("Tarifas: ")
    print(f"Asiento 1 al 30: ${asientoNormal}")
    print(f"Asiento 31 al 42: ${asientoVip}")
    asiento = int(input("Seleccione su asiento: "))
    while asiento < 1 or asiento > 42:
        print("Asiento no existente. Seleccione otro asiento:")
        asiento=int(input())
    if asiento >= 1 and asiento<31:
        precio=asientoNormal
    else:
        precio=asientoVip
    if banco == 3:
        precioFinal=precio-(precio*(15/100))
        print(f"Sub total: ${precio}")
        print("Dscto Banco Duoc: 15%")
        print(f"Total a pagar: ${precioFinal}")
    else:
        precioFinal=precio
        print(f"Total a pagar: ${precioFinal}")
    print("")
    print("Asiento reservado. Regresando al menú principal")
    print("")
    return np.array([nom,rut,telefono,banco,asiento],dtype=object)

def modificarPasajero(listaPasajeros,m):
    rutMod=int(input("Ingrese rut del pasajero a modificar sin puntos ni guión. Si termina en K reemplazar por un 0: "))
    asientoMod=int(input("Ingrese el asiento del pasajero a modificar: "))
    for k in range(m):
        if listaPasajeros[k][1]==rutMod and listaPasajeros[k][4]==asientoMod:
            print("Pasajero validado.")
            print("¿Qué dato desea modificar?")
            print("1. Nombre pasajero")
            print("2. Teléfono pasajero")
        else:
            print("Pasajero no encontrado.")
            print("Regresando al menú principal.")
            print("")