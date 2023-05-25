import os
import clases.classvendedores as clasesVendedores
import clases.classproductos as classProductos
import clases.classCarrito as classCarrito
import clases.excepciones as excepcion
import copy
#Funcion Borrar Pantalla
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

#Funcion para iniciar sesion
def login():
    global list_vendedores
    global vendedor_Actual
    borrarPantalla()
    print('\\\\\ MOLL CHINO /////')
    print('\\\\ Best Precios ////')
    print('** Inicio Sesion ** ')
    while True:
        rut = input('Ingrese Rut Vendedor: ')
        password= input('Ingrese Password: ')
        if validarLogin(rut,password):
            menuPrincipal()
            break
        else: 
            print('Datos Erroneos, volver a intentar.')

#Funcion de login
def validarLogin(rut, password):
    global vendedor_Actual
    for vend in list_vendedores:
        if vend.rut == rut and vend.password == password:
            vendedor_Actual = vend
            return True
    return False

# Imprimir listado de productos
def printProductos():
    global list_productos
    borrarPantalla()
    print('Listado de productos')
    print(' SKU | NOMBRE | VALOR NETO | STOCK')
    for produc in list_productos:
        print(f'{produc.sku} | {produc.nombre} | ${produc.valor_neto} | {produc.stock} Unidades')

#Vender
def vender():
    while True:
        borrarPantalla()
        try:
            printProductos()
            print('\n-*- CARRITO -*-')
            for produc in carrito.productos:
                print(f'Nombre: {produc.nombre} - Cantidad: {produc.stock}')
            sku = int(input('Ingrese el Sku del producto: '))
            for prod in list_productos:
                if int(prod.sku) == sku:
                    cant = int(input('Indique la cantidad: '))
                    if cant <= prod.stock:
                        newProducto = copy.copy(prod)
                        newProducto.stock = cant
                        carrito.productos.append(newProducto)
                        print('Producto agregado.')
                        op = input('¿Desea agregar algo mas? si / no ')
                        if op == 'si' or op == 'Si' or op == 'SI' or op == 'sI':
                            break
                        else:
                            generarVenta()
                            return
                    elif prod.stock > cant :
                        raise excepcion.stockInsuficient
            raise excepcion.SkuNotFound(sku)
        except excepcion.stockInsuficient as e:
            print(f'Error: {e}')

        except excepcion.SkuNotFound as e:
            print(f'Error: {e}')

def generarVenta():
    global list_productos
    borrarPantalla()
    print('Carrito')
    total = 0
    for produc in carrito.productos:
        monto = int(produc.getValor_total() * produc.stock)
        total += monto
        print(f'Nombre: {produc.nombre} - Cantidad: {produc.stock} - subtotal: {monto}')
    print(f'Total: {total}')
    op = input('¿Desea confirmar compra? si / no ')
    if op == 'si' or op == 'Si' or op == 'SI' or op == 'sI':
        vendedor_Actual.calcularComision(monto) #Añade la comision al vendedor
        clasesVendedores.saveVendedores(list_vendedores) # Guarda los datos en Json
        list_productos = classProductos.generarVenta(list_productos, carrito.productos) 
        input('Pedido Finalizado.\nGracias por su compra.\nVuelva Pronto\n Presione enter para continuar:')
    else:
        input('Pedido Cancelado. Carrito Vaciado. \nPresione enter para continuar: ')
    carrito.productos = []

# Menu Princiapl
def menuPrincipal():
    while True:
        borrarPantalla()
        print('\\\\\ MOLL CHINO /////')
        print('\\\\ Best Precios ////')
        print('1.- Generar Venta')
        print('2.- Agregar Producto')
        print('3.- Modificar Producto')
        print('4.- Eliminar Producto')
        print('5.- Listado de productos')
        print('9.- Salir\n')
        print('0.- Cambiar Contraseña')
        try:
            op = int(input('Indique el numero de opcion: '))
        except:
            print('La opcion ingresada no es valida. Recuerda ingresar un nuevo entero.')
        if op == 1:
            vender()
        elif op ==2:
            global list_productos
            list_productos = classProductos.agregarProducto(list_productos)
        elif op == 3:
            printProductos()
            list_productos = classProductos.modificarProducto(list_productos)
        elif op == 4:
            printProductos()
            list_productos = classProductos.eliminarProducto(list_productos)
        elif op == 5:
            printProductos()
            input('Presione enter para continuar: ')
        elif op == 0:
            clasesVendedores.cambiarContraseña(vendedor_Actual, list_vendedores)

## START -----------------
list_vendedores = clasesVendedores.load_vendedores()
vendedor_Actual = None
list_productos = classProductos.load_Productos()
carrito = classCarrito.Carrito([])
login()
