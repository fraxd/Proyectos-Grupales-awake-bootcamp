import copy
import os
import random
from clases.classCarrito import Carrito
from clases.classException import notFoundExcept
from clases.classproductos import Productos
import control_bodega
import clases.classclientes
import clases.classvendedores
import clases.classOrdenCompra as classOrdenCompra
from clases.classProveedor import proveedor as proveedorClass
import json
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
            input('Presione enter para continuar.')
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
    for product in cliente.carrito.productos: #revisa si el producto ya se encuetra en el carrito
        if product.sku == producto.sku:
            product.stock+=stock_pedido
            mensajecarro(cliente)
            return

    #si no lo encuentra crea un producto nuevo
    newprodu=copy.copy(producto)
    newprodu.stock=stock_pedido
    carrito.append(newprodu)
    cliente.carrito = Carrito(carrito)
    mensajecarro(cliente)

def mensajecarro(cliente):
    print("Su pedido se ha añadido al carrito.")
    print(cliente.nombre)
    for produ in cliente.carrito.productos:
        print(produ.nombre,"cantidad :",produ.stock)
    input('Presione enter para continuar.')

def efectuarCompra(vendedor, cliente):
    if cliente.carrito.productos == []:
        return print("el carrito está vacio.")

    print('Procesando Pedido...')
    subtotal=0
    valorneto=0
    for produ in cliente.carrito.productos:
        producto = control_bodega.getProducto(produ.sku)
        subtotal+=produ.getValor_total() * produ.stock
        valorneto+=produ.valor_neto * produ.stock
        if control_bodega.validaStock(produ.stock, producto) is False:
            print('Compra Cancelada.')
            cliente.carrito.productos = []
            return print(f'Stock de {produ} Insuficiente.')
    
    pedido = classOrdenCompra.OrdenCompra(len(cliente.pedidos)+1, cliente.carrito.productos, subtotal)
    print('Procesando Pedido...')
    if vendedor.vender(cliente, pedido,valorneto):
        cliente.pedidos.append(pedido)
        control_bodega.guardar_datos()
        pedido.confirmar()
    else:
        print("El carrito está vacio.") 
        input('Presione enter para continuar.')
        pedido.cancelar()
    pedidos.append(pedido)
    guardar_pedidos()
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

def guardar_pedidos():
    def serializar_objeto(obj):
        if isinstance(obj, classOrdenCompra.OrdenCompra):
            producto_serializado = serializar_objeto(obj.productos)
            return {'id_compra': obj.id_ordencompra, 'productos': producto_serializado, 'despacho': obj.despacho, 'subtotal': obj.subtotal, 'total': obj.total, 'status': obj.status}
        elif isinstance(obj, Productos):
            return {'sku': obj.sku, 'nombre': obj.nombre, 'categoria': obj.categoria, 'proveedor': '', 'stock': obj.stock, 'valor_neto': obj.valor_neto, 'descuento': obj.descuento }
        raise TypeError(f'No se puede serializar el objeto: {obj}')

    with open('pedidos.json', 'w') as file:
        json.dump(pedidos, file, default=lambda o: o.__dict__, indent=4)

def cargar_pedidos():
    try:
        with open('pedidos.json', 'r') as file:
            data = json.load(file)
            ordenes = []
            for item in data:
                id_ordencompra = item['id_ordencompra']
                productos = []
                subtotal = item['subtotal']
                status = item['status']
                productos_data = item['productos']
                for product in productos_data:
                    if 'proveedor' in product:
                        proveedor_data = product['proveedor']
                        proveedor = proveedorClass(proveedor_data['rut'], proveedor_data['nombreLegal'], proveedor_data['razonSocial'], proveedor_data['direccion'], proveedor_data['pais'], proveedor_data['personaJuridica'])
                        producto = Productos(product['sku'], product['nombre'],product['categoria'], proveedor, product['stock'], product['valor_neto'])
                        productos.append(producto)
                order = classOrdenCompra.OrdenCompra(id_ordencompra, producto,subtotal, status)
                ordenes.append(order)
            return ordenes
    except:
        return []



#Funciones Basicas 
global Pedidos
pedidos = cargar_pedidos()
