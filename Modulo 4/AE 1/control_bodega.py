import os
from classproductos import Productos

zapatillanike = Productos('001', 'Nike Revolution 6', 'zapatillas','dimarsa','20', '64990')
poleranike = Productos('002', 'Nike Sportswear', 'poleras','dimarsa','10', '19990')
zapatosnike = Productos('003', 'Nike Air Max 90', 'zapatos','dimarsa','15', '79990')
poleronnike = Productos('004', 'Nike Sportswear', 'poleron','dimarsa','3', '29990')
chaquetanike = Productos('005', 'Nike Sportswear', 'chaqueta','dimarsa','5', '39990')
guantesnike = Productos('006', 'Nike Sportswear', 'guantes','dimarsa','4', '9990')

productos=[zapatillanike,poleranike,zapatosnike,poleronnike,chaquetanike,guantesnike]


def start():
    print('Stock Inicial establecido.')

def menu_bodega():
    while True:
        print('\nTe lo vendo | Bodega System 2.0 \n')
        print('1.- Agregar Nuevo Producto')
        print('2.- Actualizar Stock producto')
        print('3.- Ver stock actual global')
        print('4.- Ver stock actual especifico')
        print('5.- Ver todos los productos')
        print('6.- Revisar productos son sobrestock')
        print('9.- Regresar Menu principal')

        opcion = int(input('\n Indique su opcion: '))

        match opcion:
            case 1:
                borrarPantalla()
                nombre_producto = input('Ingrese nombre nuevo producto: ')
                while True:
                    try:
                        stock_producto = int(input('Ingrese stock producto: '))
                        break
                    except:
                        print('Debe ingresar un numero entero.')
                newProduct(nombre_producto, stock_producto)
            case 2:
                borrarPantalla()
                stockGlobal()
                while True:
                    nombre_producto = input('\n Indique el nombre del producto a editar: ')
                    while True:
                        try:
                            nuevo_stock = int(input('Ingrese nuevo Stock: '))
                            break
                        except:
                            print('Recuerda Ingresar un valor numerico.')
                    if updateStock(nombre_producto, nuevo_stock):
                        break
            #opcion 3: Ver stock actual global
            case 3:
                borrarPantalla()
                stockGlobal()
            # Opcion 4: Ver stock actual especifico
            case 4:
                borrarPantalla()
                while True:
                    nombre_producto = input('Indique producto a actualizar stock: ')
                    if stockEspecifico(nombre_producto):
                        break
            # Opcion 5: Ver todos los productos'
            case 5:
                borrarPantalla()
                productosGlobal()

            #opcion 6:  Revisar productos son sobrestock        
            case 6:
                borrarPantalla()
                while True:
                    try:
                        sobre_stock = int(input('Ingrese valor de sobrestock a buscar: '))
                        break
                    except:
                        print('Error, Debe ingresar un numero entero. \n')
                sobreStock(sobre_stock)
            
            # Opcion 9: Salir
            case 9:
                break



## Agregar nuevos productos a la "base de datos"
def newProduct(nombre_producto, stock):
    id=len(productos)+1
    newProdu=Productos(id,nombre_producto,"","",stock,"")
    productos.append(newProdu)
    mostrarProducto(newProdu)
    print('Producto Agregado Correctamente.')
    return True

def updateStock(nombre_producto, stock):
        # Se busca el producto por nombre 
    producto=getProductoByName(nombre_producto)
    if producto:
        producto.stock = stock
        print('Stock Actualizado')
        return True
    else:
        print('Por algun motivo no encontramos el producto.')
        return False

#Mostrar y retornar las unidades disponibles por producto.
def stockGlobal():
    print('Stock de todos nuestros productos:')
    for producto in productos:
        print('Producto:',producto.nombre, 'Stock: ', producto.stock)        
    return productos

#Mostrar y retornar las unidades disponibles de un producto en particular.
def stockEspecifico(nombre_producto):
    producto=getProductoByName(nombre_producto)
    if producto:
        print('Nombre: ',producto.nombre, 'Stock: ', producto.stock)
        return producto.stock
    print('Producto no encontrado.')
    return False


#Mostrar y retornar todos los productos de la tienda.
def productosGlobal():
    nombre_productos = []
    print('Listado de Productos: ')
    for producto in productos:
        nombre_productos.append(producto.nombre)
        print('-',producto.nombre)
    return nombre_productos

#Mostrar y retornar los productos que tienen más de un número de unidades (el usuario puede escoger el número de unidades).
def sobreStock(sobre_stock):
    sobre_stock_productos = []
    for producto in productos:
        if(int(producto.stock)>sobre_stock):
            sobre_stock_productos.append(producto)
            print(mostrarProducto(producto))
    return sobre_stock_productos

def getProducto(id_producto):
    for producto in productos:
        if int(producto.sku) == id_producto:
            return producto
    return False

def getProductoByName(nombre_producto):
    for producto in productos:
        if producto.nombre == nombre_producto:
            return producto
    return False

def validaStock(pedido, product):
    if int(product.stock)>= pedido:
        print(product.stock)
        return True
    return False

def mostrarProducto(produ):
    print("ID :",produ.sku,"Nombre :",produ.nombre,"Categoría :",produ.categoria,"Proveedor :",produ.proveedor,"Stock :",produ.stock,"Precio :",produ.valor_neto)

## Limpiar pantalla
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")