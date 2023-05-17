import control_bodega
import control_venta


def menu_principal(sucursal):
    while True:
        control_bodega.start(sucursal)
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
            control_bodega.menu_bodega(sucursal)
        elif opcion == 2:
            control_venta.menu_venta(sucursal)
        elif opcion == 9:
            print('\n \n \n Muchas gracias por usarnos \n \n PencaLabs ©')
            break
        else:
            print('Opcion Selecionada NO Valida. ')


def menu_sucursales():
    while True:
        control_bodega.borrarPantalla()
        print('\n      Bienvenido a Te lo vendo systems 2.0')
        print('----- Todos los derechos reservados 1995 © ----- ')
        print('\nSelecione Sucursal: ')
        print('1.- Valparaiso')
        print('2.- Viña del Mar')
        print('3.- Quilpue')
        print('4.- Quillota')
        print('9.- Salir del Programa')
        while True:
            try:
                opcion = int(input('Ingrese su opcion: '))
                break
            except:
                print('Error: Debe ingresar un numero entero.')
        if opcion == 1:
            menu_principal('valparaiso')
        elif opcion == 2:
            menu_principal('viña del mar')
        elif opcion == 3:
            menu_principal('Quilpue')
        elif opcion == 4:
            menu_principal('Quillota')
        elif opcion == 9:
            print('\n \n \n Muchas gracias por usarnos \n \n PencaLabs ©')
            break
        else:
            print('Opcion Selecionada NO Valida. ')


# INICIO DEL PROGRAMA
menu_sucursales()
