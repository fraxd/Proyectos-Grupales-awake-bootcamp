import json
import os
from clases.excepciones import SkuNotFound
from clases.classCarrito import Carrito

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

class Productos():
    sku = int
    nombre = str
    categoria = str
    stock = int
    valor_neto = int
    __impuesto = 1.19

    def __init__(self, sku, nombre, categoria, stock, valor_neto):

        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.stock = int(stock)
        self.valor_neto = valor_neto

    def actualizarPrecio(self, nuevo_precio: int):
        self.valor_neto = nuevo_precio

    def actualizarPrecio(self, nuevo_precio: str):  # Porcentaje
        porcentaje = nuevo_precio.split('%')
        porcentaje_int = int(porcentaje(0))/100 + 1
        self.valor_neto = self.valor_neto * porcentaje_int

    def generarVenta(self, cant_pedida):
        self.stock -= cant_pedida

    def getValor_neto(self):
        return self.valor_neto
    
    def getValor_total(self):
        return self.valor_neto*self.__impuesto

    def getImpuesto(self):
        return self.__impuesto
    
def load_Productos():
    # Obtener la ubicación del archivo .py actual
    ubicacion_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la ruta completa del archivo JSON
    ruta_json = os.path.join(ubicacion_actual, 'productos.json')
    productos = []
    try:
        with open(ruta_json, 'r') as archivo:
            data = json.load(archivo)
            for producto_data in data:
                product = Productos(
                    producto_data['sku'],
                    producto_data['nombre'],
                    producto_data['categoria'],
                    producto_data['stock'],
                    producto_data['valor_neto']
                )
                productos.append(product)
    except:
        print('Error: No se encontro el archivo de productos. ')

    return productos

def saveProductos(list_productos):
    # Obtener la ubicación del archivo .py actual
    ubicacion_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la ruta completa del archivo JSON
    ruta_json = os.path.join(ubicacion_actual, 'productos.json')
    data = []
    for producto in list_productos:
        producto_data = {
            'sku': producto.sku,
            'nombre': producto.nombre,
            'categoria': producto.categoria,
            'stock': producto.stock,
            'valor_neto': producto.valor_neto,
        }
        data.append(producto_data)
    try:
        with open(ruta_json, 'w') as archivo:
            json.dump(data, archivo, indent=4)
    except Exception as e:
        print(f'Error al guardar archivo. {e}')


#funciona para agregar nuevo producto
def agregarProducto(list_productos):
    borrarPantalla()
    print('Nuevo Producto\n')
    sku = input('Ingrese SKU del nuevo producto: ')
    nombre = input('Ingrese nombre del nuevo producto: ')
    categoria = input('Ingrese la categoria para el producto: ')
    try:
        stock = int(input('Indique el stock para el producto (en numeros): '))
        valor_neto = int(input('Indique el precio NETO para el producto (en numeros): '))
    except:
        input('Error - Debe ingresar numeros entero en la operacion. \n Presione enter para continuar.')
    nuevo_producto = Productos(sku,nombre, categoria, stock, valor_neto)
    list_productos.append(nuevo_producto)
    saveProductos(list_productos)
    input('Producto Agregado Correctamente. Presione enter para continuar.')
    return list_productos

#Funcion para modificar producto
def modificarProducto(list_productos):
    product = None
    indice = -1
    while True:
        try:
            sku = int(input('Ingrese el SKU del producto a editar: '))
            for i in range(len(list_productos)):
                if int(list_productos[i].sku) == sku:
                    product = list_productos[i]
                    indice = i
                    break
            if indice == -1:
                raise SkuNotFound
            print('Solamente modifique los campos que desea, SI DESEA MANTENER EL ATRIBUTO PRESIONE ENTER')
            nombre = input('Indique Nuevo Nombre: ')
            if nombre != '':
                product.nombre = nombre
            categoria = input('Indique Nueva Categoria: ')
            if categoria != '':
                product.categoria = categoria
            stock = input('Indique Nuevo stock: ')
            if stock != '':
                product.stock = stock
            valor_neto = input('Indique Nueva valor_neto: ')
            if valor_neto != '':
                product.valor_neto = valor_neto     
            print('\nLos nuevos datos son los siguientes:')
            print(f'Nombre: {product.nombre}')
            print(f'categoria: {product.categoria}')
            print(f'stock: {product.stock}')
            print(f'valor_neto: {product.valor_neto}')
            confirm = input('¿Esta seguro de los cambios? (SI / NO ): ')
            if confirm == 'si' or confirm == 'Si' or confirm == 'SI' or confirm == 'sI':
                list_productos[indice] = product
                saveProductos(list_productos)
                input('Actualizacion Lista, Presione enter para continuar')
                return list_productos
            else:
                input('Actualizacion Cancelada, Presione enter para continuar')

        except SkuNotFound as e:
            print(f'Error: {e}')
        except:
            print('El sku debe ser en formato numerico.')

# Eliminar producctos y actualizar JSON
def eliminarProducto(list_productos):
    while True:
        try:
            sku = int(input('Ingrese el SKU del producto a editar: '))
            for i in range(len(list_productos)):
                if int(list_productos[i].sku) == sku:
                    product = list_productos[i]
                    print(f'\nProducto Selecionado:')
                    print(f'nombre {product.nombre}')
                    op = input('¿Esta seguro en eliminar el producto? (si / no) ')
                    if op == 'si' or op == 'Si' or op == 'SI' or op == 'sI':
                        del list_productos[i]
                        saveProductos(list_productos)
                        input('Producto Eliminado. Presione enter para continuar ')
                    else:
                        input('Producto Eliminado. Presione enter para continuar ')
                    return list_productos
        except SkuNotFound as e:
            print(f'Error: {e}')

def generarVenta(list_productos, carrito):
    for producto in carrito:
        for i in range(len(list_productos)):
            if producto.sku == list_productos[i].sku:
                list_productos[i].stock -= producto.stock
                break
    saveProductos(list_productos)