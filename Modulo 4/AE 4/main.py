import control_bodega
import control_venta

def menu_principal():
    while True:
        control_bodega.borrarPantalla()
        print('\n      Bienvenido a Te lo vendo systems 2.0')
        print('----- Todos los derechos reservados 1995 © ----- ')
        print('\nMenu Principal: ')
        print('1.- Control de Bodega')
        print('2.- Control de Ventas')
        print('9.- Salir del Programa')
        while True:    
            try:
                opcion = int(input('Ingrese su opcion: '))
                break
            except:
                print('Error: Debe ingresar un numero entero.')
        if opcion == 1:
            control_bodega.menu_bodega()
        elif opcion == 2:
            control_venta.menu_venta()
        elif opcion == 9:
            print('\n \n \n Muchas gracias por usarnos \n \n PencaLabs ©')
            break
        else:
            print('Opcion Selecionada NO Valida. ')


## INICIO DEL PROGRAMA
control_bodega.start()
menu_principal()















