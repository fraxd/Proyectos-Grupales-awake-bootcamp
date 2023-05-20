import copy
import os
import random
from clases.classCarrito import Carrito
from clases.classException import notFoundExcept
import control_bodega
import clases.classclientes
import clases.classvendedores
import clases.classOrdenCompra as classOrdenCompra
# CLIENTES
juanperez = clases.classclientes.Clientes(
    1, 'Juan', 'Pérez', 'juanitoxBellakito@gmail.com', '02/02/2020')
ignaciomiranda = clases.classclientes.Clientes(
    2, 'Ignacio', 'Miranda', 'nachito1313@gmail.com', '03/03/2020')
sofiaaraya = clases.classclientes.Clientes(
    3, 'Sofia', 'Araya', 'sofiaAraya@gmail.com', '04/04/2020')
anasanchez = clases.classclientes.Clientes(
    4, "Ana", "Sánchez", "anaSanchez@mail.com", "2022-01-03")
carlosgomez = clases.classclientes.Clientes(
    5, "Carlos", "Gómez", "carlosGomez@mail.com", "2022-01-03")

clientes = [juanperez, ignaciomiranda, sofiaaraya, anasanchez, carlosgomez]

# Vendedores
vendedor1 = clases.classvendedores.Vendedor(
    '17888111-1', 'Pablo', 'Picasso', 'Zapatillas')
vendedor2 = clases.classvendedores.Vendedor(
    '18999666-9', 'Vincent', 'Vangoh', 'Poleras')
vendedor3 = clases.classvendedores.Vendedor(
    "33333333-3", "Marcela", "Torres", "Zapatos")
vendedor4 = clases.classvendedores.Vendedor(
    "44444444-4", "Santiago", "Sánchez", "Poleron")
vendedor5 = clases.classvendedores.Vendedor(
    "55555555-5", "Lucía", "González", "Chaqueta")

list_vendedores = [vendedor1, vendedor2, vendedor3, vendedor4, vendedor5]

def login(nombre_sucursal):
   ran=random.randint(1,len(list_vendedores)-1)
   control_bodega.borrarPantalla()
   print('----- Te lo vendo SA. -----')
   print('- Iniciar Sesion 1.8v -')
   print(f'----- Sucursal: {nombre_sucursal} -----\n')
   print("Usted será atendido por :", list_vendedores[ran].nombre, list_vendedores[ran].apellido,"Run :", list_vendedores[ran].run )
   
   while True:
        try:
            id = int(input("Ingrese su ID de usuario :"))
            cliente = getCliente(id)
            if cliente != '':
                control_bodega.borrarPantalla()
                print('Cliente Selecionado: ', cliente.nombre)
                break
        except:
            print('Debes ingresar un usuario valido')
   menu_venta(nombre_sucursal,list_vendedores[ran],cliente)

def menu_venta(nombre_sucursal,vendedor,cliente):
    while True:
        control_bodega.borrarPantalla()
        print('----- Te lo vendo SA. -----')
        print(f'- Bienvenido {cliente.nombre} {cliente.apellido} -')
        print('- Control de ventas System 1.8v -')
        print(f'----- Sucursal: {nombre_sucursal} -----\n')
        print('1. Ver numero de clientes')
        print('2. Generar Pedidos')
        print('3. Mostrar Saldo')
        print('4. Agregar Saldo')
        print('5. Efectuar compra')
        print('6. Ver promedio de compras')
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
            compras(cliente)
        elif opcion == 3:
            mostrarSaldoCliente(cliente)
        elif opcion == 4:
            agregarSaldoCliente(cliente)
        elif opcion == 5:
            efectuarCompra(vendedor,cliente)
        elif opcion == 6:
            promediarCompras(cliente)
        elif opcion == 9:
            print('\n \n \n Muchas gracias por usarnos \n \n PencaLabs ©')
            break
        else:
            print('Opcion Selecionada NO Valida. ')

# Get Cliente


def getCliente(id_cliente):
    for cliente in clientes:
        if cliente.idcliente == id_cliente:
            return cliente
    return ''

# Mostrar Saldo Cliente


def mostrarSaldoCliente(cliente):
    
    saldo = cliente.saldo()
    print(f"El saldo del cliente {cliente.nombre} es: {saldo}")
    input("Presione cualquier tecla para continuar.")

# Agregar Saldo Cliente


def agregarSaldoCliente(cliente):
    
        try:
            saldo = int(input('Ingrese el saldo a agregar: '))
            saldoTotal = cliente.agregar_saldo(saldo)
            print(f"Saldo actual de {cliente.nombre}: {saldoTotal}")
        except ValueError:
            print('Por favor ingrese un valor numerico')

        input("Presione cualquier tecla para continuar")
    
# Imprimir cantidad de clientes


def printNumeroClientes():
    print(' Actualmente hay registrados', len(clientes), 'Clientes.')
    input('Presione Enter para continuar.')

# Armar Pedidos


def compras(cliente):
    carrito=copy.copy(cliente.carrito.productos)
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
        except:
            print("ingrese un numero valido")
        try:
            if stock_pedido>10:
                raise 
                return True  # Retornar True en caso de error
        except:
            print("La cantidad no puede exceder las 10 unidades.")
            input()
            return True  # Retornar True en caso de error
        try:
            if control_bodega.validaStock(stock_pedido, producto):
                break
            else:
                raise notFoundExcept(producto.nombre)   
        except notFoundExcept as e:
            print(e)
            input()
            return True  # Retornar True en caso de error
    newprodu=copy.copy(producto)
    newprodu.stock=stock_pedido
    carrito.append(newprodu)
    cliente.carrito = Carrito(carrito)
    print("Su pedido se ha añadido al carrito.")
    print(cliente.nombre)
    for produ in cliente.carrito.productos:
        print(produ.nombre,"cantidad :",produ.stock)
    input('Presione enter para continuar.')

def efectuarCompra(vendedor, cliente):
    print('Procesando Pedido...')
    try:
        for produ in cliente.carrito.productos:
            producto = control_bodega.getProducto(produ.sku)
            if control_bodega.validaStock(produ.stock, producto):
                pedido = classOrdenCompra.OrdenCompra(len(cliente.pedidos)+1, producto, produ.stock)
                if vendedor.vender(cliente, pedido):
                    cliente.pedidos.append(pedido)
            else:
                print('Compra Cancelada.')
                print('Stock Insuficiente.')
    except:
        print("el carrito está vacio.")
    cliente.carrito.productos = []
    print("El carrito de compras ha sido vaciado.")
    input('Presione enter para continuar.')

def promediarCompras(cliente):
    try:
        promedio=0
        total=0
        suma=0
        for pedido in cliente.pedidos:
            total=(pedido.cantidad * pedido.producto.valor_neto)
            suma+=total
        promedio=suma/len(cliente.pedidos)
        print("el valor de compra promedio es:",promedio)
        input('Presione enter para continuar.')
    except:
        print(cliente.nombre,"aún no ha hecho ninguna compra.")
        input('Presione enter para continuar.')
