import os
import control_bodega
import clases.classclientes
import clases.classvendedores

## CLIENTES
juanperez = clases.classclientes.Clientes(1,'Juan', 'Pérez', 'juanitoxBellakito@gmail.com', '02/02/2020')
ignaciomiranda = clases.classclientes.Clientes(2,'Ignacio', 'Miranda', 'nachito1313@gmail.com', '03/03/2020')
sofiaaraya = clases.classclientes.Clientes(3,'Sofia','Araya', 'sofiaAraya@gmail.com', '04/04/2020')
anasanchez = clases.classclientes.Clientes(4,"Ana", "Sánchez", "anaSanchez@mail.com", "2022-01-03")
carlosgomez = clases.classclientes.Clientes(5,"Carlos", "Gómez", "carlosGomez@mail.com", "2022-01-03")

clientes = [juanperez, ignaciomiranda, sofiaaraya, anasanchez, carlosgomez]

## Vendedores
vendedor1 = clases.classvendedores.Vendedor('17888111-1', 'Pablo', 'Picasso', 'Zapatillas')
vendedor2 = clases.classvendedores.Vendedor('18999666-9', 'Vincent', 'Vangoh', 'Poleras' )
vendedor3 = clases.classvendedores.Vendedor("33333333-3", "Marcela", "Torres", "Zapatos")
vendedor4 = clases.classvendedores.Vendedor("44444444-4", "Santiago", "Sánchez", "Poleron")
vendedor5 = clases.classvendedores.Vendedor("55555555-5", "Lucía", "González", "Chaqueta")

list_vendedores = [vendedor1, vendedor2, vendedor3, vendedor4, vendedor5]

def menu_venta():
    while True:
        control_bodega.borrarPantalla()
        print('Te lo vendo SA.')
        print('Control de ventas System 1.8v')
        print('1. Ver numero de clientes')
        print('2. Generar Pedidos')
        print('3. Mostrar Saldo')
        print('4. Agregar Saldo')
        print('9. Salir')
        while True:    
            try:
                opcion = int(input('Ingrese su opcion: '))
                break
            except:
                print('Error: Debe ingresar un numero entero.')
        if opcion == 1:
            printNumeroClientes()
        elif opcion == 2:
            compras()
        elif opcion == 3:
            mostrarSaldoCliente()
        elif opcion == 4:
            agregarSaldoCliente()
        elif opcion == 9:
            print('\n \n \n Muchas gracias por usarnos \n \n PencaLabs ©')
            break
        else:
            print('Opcion Selecionada NO Valida. ')

## Get Cliente
def getCliente(id_cliente):
    for cliente in clientes:
        if cliente.idcliente == id_cliente:
            return cliente
    return ''

#Mostrar Saldo Cliente
def mostrarSaldoCliente():
    id_cliente = int(input('Ingrese el ID del cliente: '))
    cliente = getCliente(id_cliente)
    if cliente:
        saldo = cliente.saldo()
        print(f"El saldo del cliente {cliente.nombre} es: {saldo}")
        input("Presione cualquier tecla para continuar")
    else:
        print("Cliente no encontrado.")

#Agregar Saldo Cliente
def agregarSaldoCliente():
    id_cliente = int(input('Ingrese el ID del cliente: '))
    cliente = getCliente(id_cliente)
    if cliente:
        try:                    
            saldo = int(input('Ingrese el saldo a agregar: '))
            saldoTotal = cliente.agregar_saldo(saldo)
            print(f"Saldo actual de {cliente.nombre}: {saldoTotal}")
        except ValueError:
            print('Por favor ingrese un valor numerico')
            
        input("Presione cualquier tecla para continuar")
    else:
        print("Cliente no encontrado.")
# Imprimir cantidad de clientes
def printNumeroClientes():
    print(' Actualmente hay registrados',len(clientes),'Clientes.')
    input('Presione Enter para continuar.')

# Armar Pedidos
def compras():
    vendedor = ''
    while True:
            rut_Vendedor = input('Ingrese rut del vendedor. (sin puntos solo con -): ')
            for vend in list_vendedores:
                if rut_Vendedor == vend.getRun():
                    vendedor = vend
                    break
                else:
                    continue
            if vendedor != '':
                break
            else:
                print('Run de trabajador no encontrado')
    while True:
        try:
            id = int(input('Indique N° de cliente: ')) 
            cliente = getCliente(id)
            if cliente != '':
                control_bodega.borrarPantalla()
                print('Cliente Selecionado: ', cliente.nombre )
                break
        except: 
            print('Debes ingresar un numero entero.')
    while True:
        try:
            id_producto = int(input('Indique Id Producto: '))
            producto = control_bodega.getProducto(id_producto)
            if producto:
                print('Producto Selecionado: ', producto.nombre)
                break
        except:
            print('Debe Ingresar un numero entero.')
    while True:
        try:
            stock_pedido = int(input('Indique cantidad de unidades: '))
            break
        except:
            print('Por defecto se pide 1.')
            stock_pedido = 1.
            break
    print('Procesando Pedido...')
    if control_bodega.validaStock(stock_pedido, producto):
        vendedor.vender(cliente,producto, stock_pedido)
    else:
        print('Compra Cancelada.')
        print('Stock Insuficiente.')
    input('Presione enter para continuar.')
