import os
import control_bodega
import classclientes

juanperez = classclientes.Clientes(1,'Juan', 'Pérez', 'juanitoxBellakito@gmail.com', '02/02/2020')
ignaciomiranda = classclientes.Clientes(2,'Ignacio', 'Miranda', 'nachito1313@gmail.com', '03/03/2020')
sofiaaraya = classclientes.Clientes(3,'Sofia','Araya', 'sofiaAraya@gmail.com', '04/04/2020')
anasanchez = classclientes.Clientes(4,"Ana", "Sánchez", "anaSanchez@mail.com", "2022-01-03")
carlosgomez = classclientes.Clientes(5,"Carlos", "Gómez", "carlosGomez@mail.com", "2022-01-03")

clientes = [juanperez, ignaciomiranda, sofiaaraya, anasanchez, carlosgomez]



def menu_venta():
    while True:
        control_bodega.borrarPantalla()
        for cliente in clientes:
            print(f"Nombre: {cliente.idcliente}, Apellido: {cliente.apellido}, Saldo:{cliente.mostrar_saldo()}")
        print('Te lo vendo SA.')
        print('Control de ventas System 1.8v')
        print('1. Ver numero de clientes')
        print('2. Generar Pedidos')
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
        elif opcion == 9:
            print('\n \n \n Muchas gracias por usarnos \n \n PencaLabs ©')
            break
        else:
            print('Opcion Selecionada NO Valida. ')

## Get Cliente
def getCliente(id_cliente):
    for cliente in clientes:
        if cliente.idcliente == id_cliente:
            return cliente.nombre
    return ''


# Imprimir cantidad de clientes
def printNumeroClientes():
    print(' Actualmente hay registrados',len(clientes),'Clientes.')
    input('Presione Enter para continuar.')

# Armar Pedidos
def compras():
    producto = {}
    while True:
        try:
            id = int(input('Indique N° de cliente: ')) 
            nombre = getCliente(id)
            if nombre != '':
                control_bodega.borrarPantalla()
                print('Cliente Selecionado: ', nombre )
                break
        except: 
            print('Debes ingresar un numero entero.')
    while True:
        try:
            id_producto = int(input('Indique Id Producto: '))
            producto = control_bodega.getProducto(id_producto)
            if producto:
                print('Producto Selecionado: ', producto['producto'])
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
    autorizarCompra(stock_pedido, producto)

# Procesamiento de pedidos
def autorizarCompra(stock_pedido, producto):
    print('Procesando Pedido...')
    if control_bodega.validaStock(stock_pedido, int(producto['id_producto'])):
        print('Compra Aprobada.')
        print('Procesando Despacho.')
        print('Gracias por Elegirnos.')
    else:
        print('Compra Cancelada.')
        print('Stock Insuficiente.')