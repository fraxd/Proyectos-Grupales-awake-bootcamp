import os
from clases.classSucursal import Sucursal




def menu_bodega(nombre_sucursal):
    Sucursal_actual = Sucursal(nombre_sucursal)
    while True:
        print('\nTe lo vendo | Bodega System 2.0 \n')
        print('1.- Agregar Nuevo Producto')
        print('2.- Actualizar Stock producto')
        print('3.- Ver stock actual global')
        print('4.- Ver stock actual especifico')
        print('5.- Ver todos los productos')
        print('6.- Revisar productos con sobrestock')
        print('7.- Ver todos los provedores')
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
                Sucursal_actual.newProduct(nombre_producto, stock_producto)
                
            case 2:
                borrarPantalla()
                Sucursal_actual.stockGlobal()
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
                Sucursal_actual.stockGlobal()
            # Opcion 4: Ver stock actual especifico
            case 4:
                borrarPantalla()
                while True:
                    nombre_producto = input('Indique producto a visualizar stock stock: ')
                    if stockEspecifico(nombre_producto):
                        break
            # Opcion 5: Ver todos los productos'
            case 5:
                borrarPantalla()
                Sucursal_actual.productosGlobal()

            #opcion 6:  Revisar productos son sobrestock        
            case 6:
                borrarPantalla()
                while True:
                    try:
                        sobre_stock = int(input('Ingrese valor de sobrestock a buscar: '))
                        break
                    except:
                        print('Error, Debe ingresar un numero entero. \n')
                Sucursal_actual.sobreStock(sobre_stock)
            
            case 7: 
                borrarPantalla()
                print('Listado de Proveedores')
                Sucursal_actual.print_provedores
            
            # Opcion 9: Salir
            case 9:
                break

    ## Agregar nuevos productos a la "base de datos"

    def updateStock(nombre_producto, stock):
            # Se busca el producto por nombre 
        producto=Sucursal_actual.getProductoByName(nombre_producto)
        if producto:
            producto.stock = stock
            print('Stock Actualizado')
            return True
        else:
            print('Por algun motivo no encontramos el producto.')
            return False

    #Mostrar y retornar las unidades disponibles por producto.


    #Mostrar y retornar las unidades disponibles de un producto en particular.
    def stockEspecifico(nombre_producto):
        producto=Sucursal_actual.getProductoByName(nombre_producto)
        if producto:
            print('Nombre: ',producto.nombre, 'Stock: ', producto.stock)
            return producto.stock
        print('Producto no encontrado.')
        return False

def validaStock(pedido, product):
    if int(product.stock)>= pedido:
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