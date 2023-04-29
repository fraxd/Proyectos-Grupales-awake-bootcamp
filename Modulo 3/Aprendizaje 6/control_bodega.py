import os

productos = [
    {
        'producto': 'Zapatillas',
        'stock': '20'
    },
    {
        'producto': 'Poleras',
        'stock': '10'
    },
    {
        'producto': 'Zapatos',
        'stock': '15'
    },
    {
        'producto': 'Poleron',
        'stock': '3'
    },
    {
        'producto': 'Chaqueta',
        'stock': '5'
    },
    {
        'producto': 'Guantes',
        'stock': '4'
    },
]

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



## Agregar nuevos productos a la "base de datos"
def newProduct(nombre_producto, stock):
    productos.append({
        'producto' : nombre_producto,
        'stock' : stock
    })
    print('Producto Agregado Correctamente.')
    return True

def updateStock(nombre_producto, stock):
    for producto in productos:
        # Se busca el producto por nombre 
        if producto['producto'] == nombre_producto:
            producto['stock'] = stock
            print('Stock Actualizado')
            return True
        else:
            print('Por algun motivo no encontramos el producto.')
            return False

#Mostrar y retornar las unidades disponibles por producto.
def stockGlobal():
    for producto in productos:
        print('Stock de todos nuestros productos:')
        print('Nombre: ',producto['producto'], 'Stock: ', producto['stock'])        
    return productos

#Mostrar y retornar las unidades disponibles de un producto en particular.
def stockEspecifico(nombre_producto):
    for producto in productos:
        if producto['producto'] == nombre_producto:
            print('Nombre: ',producto['producto'], 'Stock: ', producto['stock'])
            return producto['stock']
    print('Producto no encontrado.')
    return False


#Mostrar y retornar todos los productos de la tienda.
def productosGlobal():
    nombre_productos = []
    for producto in productos:
        nombre_productos.append(producto['producto'])
        print(producto['producto'])
    return nombre_productos

#Mostrar y retornar los productos que tienen más de un número de unidades (el usuario puede escoger el número de unidades).
def sobreStock(sobre_stock):
    sobre_stock_productos = []
    for producto in productos:
        if(producto['stock']>sobre_stock):
            sobre_stock_productos.append(producto)
            print(producto)
    return sobre_stock_productos




## Limpiar pantalla
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")