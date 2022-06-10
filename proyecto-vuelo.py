import numpy as np
import funciones as fn
initFlag = True
asientoNormal = 78900
asientoVip = 240000
n=1
m=1
listaPasajeros = np.array([[1,2,3,4,5]],dtype=object)

listaAsientos = np.zeros((9,12),dtype=object)
for i in range(9):
    for j in range(12):
        if i == 4 or i == 5:
            listaAsientos[i][j] = "_"
        elif j == 0 or j == 1 or j == 10 or j == 11:
            listaAsientos[i][j] = "|"
        elif j == 5 or j == 6:
            listaAsientos[i][j] = " "
        else:
            listaAsientos[i][j] = n
            n += 1
copiaAsientos = listaAsientos.copy()

print("-"*30)
print("Bienvenide a Vuelos Duoc")
print("-"*30)
print("")

while initFlag == True:
    print("Seleccione una opción del menú.")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Modificar pasajero")
    print("4. Anular vuelo")
    print("5. Salir")
    opMenu = int(input(""))

    while opMenu < 1 or opMenu > 5:
        print("Opción ingresada no válida. Vuelva a intentarlo")
        opMenu=int(input(""))
    
    if opMenu == 1:
        fn.verAsientos(listaAsientos)
        opVer=int(input(""))
        while opVer < 1 or opVer > 2:
            print("Opción ingresada no válida. Vuelva a intentarlo.")
            opVer=int(input(""))
        if opVer==1:
            datos=fn.comprarAsiento(listaAsientos)
            reserva=np.where(listaAsientos==datos[4])
            listaAsientos[reserva] = 'X'
            m+=1
            listaPasajeros=np.vstack([listaPasajeros,[datos]])
        else:
            print("Regresando al menú principal")
            print("")
    
    elif opMenu==2:
        datos=fn.comprarAsiento(listaAsientos)
        reserva=np.where(listaAsientos==datos[4])
        listaAsientos[reserva] = 'X'
        m+=1
        listaPasajeros=np.vstack([listaPasajeros,[datos]])

    elif opMenu==3:
        rutMod=int(input("Ingrese rut del pasajero a modificar sin puntos ni guión. Si termina en K reemplazar por un 0: "))
        asientoMod=int(input("Ingrese el asiento del pasajero a modificar: "))
        for k in range(m):
            if listaPasajeros[k][1]==rutMod and listaPasajeros[k][4]==asientoMod:
                print("Pasajero validado.")
                print("¿Qué dato desea modificar?")
                print("1. Nombre pasajero")
                print("2. Teléfono pasajero")
                opMod=int(input())
                while opMod < 1 or opMod > 2:
                    print("Opción no válida. Vuelva a intentarlo")
                    opMod=int(input())
                if opMod==1:
                    print(f"Nombre: {listaPasajeros[k][0]}")
                    nomMod=input("Ingrese nuevo nombre: ")
                    listaPasajeros[k][0]=nomMod
                    print(f"Nuevo nombre: {listaPasajeros[k][0]}")
                    print("Operación exitosa. Regresando al menú principal.")
                    print("")
                else:
                    print(f"Teléfono: {listaPasajeros[k][2]}")
                    telMod=int(input("Ingrese nuevo teléfono (formato sin +56): "))
                    while telMod < 199999999 or telMod > 999999999:
                        print("Teléfono ingresado no válido. Vuelva a ingresar su teléfono (formato 9 dígitos sin +56): ")
                        telMod=int(input())
                    listaPasajeros[k][2]=telMod
                    print(f"Nuevo teléfono: {listaPasajeros[k][2]}")
                    print("Operación exitosa. Regresando al menú principal.")
                    print("")
                break
            else:
                print("Pasajero no encontrado.")
                print("Regresando al menú principal.")
                print("")
    
    elif opMenu == 4:
        rutAnul=int(input("Ingrese rut del pasajero de la reserva a anular sin puntos ni guión. Si termina en K reemplazar por un 0: "))
        asientoAnul=int(input("Ingrese el asiento del pasajero de la reserva a anular: "))
        for h in range(m):
            if listaPasajeros[h][1]==rutAnul and listaPasajeros[h][4]==asientoAnul:
                print("Pasajero validado.")
                opAnul=input(f"¿Segure desea anular la reserva a nombre de {listaPasajeros[h][0]}? (s/n): ")
                while opAnul != 's' and opAnul != 'n':
                    opAnul=input("Opción ingresada no válida. Vuelva a intentarlo: ")
                if opAnul == 's':
                    anular=np.where(copiaAsientos==listaPasajeros[h][4])
                    listaAsientos[anular]=listaPasajeros[h][4]
                    listaPasajeros=np.delete(listaPasajeros,h,0)
                    break
                else:
                    pass

    else:
        initFlag==False
        break
        