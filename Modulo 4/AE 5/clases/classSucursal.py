from .classproductos import Productos
from .class_tienda import tienda

# class Sucursal(Bodega):


class Sucursal(tienda):
    nombre = str

    def __init__(self, nombre = ''):
        super().__init__()
        self.nombre = nombre
        

    # def __init__(self) -> None:
    #     super().__init__()
    #     self.nombre = str
    #     self.direccion = str
    #     self.stock = int
    #     self.productos = list

    def setNombre(self, nombre_sucursal):
        self.nombre = nombre_sucursal

    def validarStock(self):
        if self.Stock < 50:
            return False

    def anadirProductos(self, object):
        self.productos.append(object)
        return self.productos

    def print_provedores(self):
        for prov in self.provedores:
            print(prov.nombreLegal)

    def newProduct(self, nombre_producto, stock):
        id = len(self.productos)+1
        newProdu = Productos(id,nombre_producto, "", "", stock, "")
        self.productos.append(newProdu)
        self.mostrarProducto(newProdu)
        print('Producto Agregado Correctamente.')
        return True

    def stockGlobal(self):
        print('Stock de todos nuestros productos:')
        for producto in self.productos:
            print('Producto:', producto.nombre, 'Stock: ', producto.stock)

    def productosGlobal(self):
        nombre_productos = []
        print('Listado de Productos: ')
        for producto in self.productos:
            nombre_productos.append(producto.nombre)
            print('-', producto.nombre)
        return nombre_productos

    def mostrarProducto(self,produ):
        print("ID :", produ.sku, "Nombre :", produ.nombre, "Categoría :", produ.categoria,
            "Proveedor :", produ.proveedor, "Stock :", produ.stock, "Precio :", produ.valor_neto)

    # Mostrar y retornar los productos que tienen más de un número de unidades (el usuario puede escoger el número de unidades).
    def sobreStock(self, sobre_stock):
        sobre_stock_productos = []
        for producto in self.productos:
            if (int(producto.stock) > sobre_stock):
                sobre_stock_productos.append(producto)
                print(self.mostrarProducto(producto))
        return sobre_stock_productos

    def getProducto(self, id_producto):
        for producto in self.productos:
            if int(producto.sku) == id_producto:
                return producto
        return False

    def getProductoByName(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                return producto
        return False

    def updateStockByname(self, nombre_producto, stock):
        for i in range(len(self.productos)):
            if self.productos[i].nombre == nombre_producto:
                self.productos[i].stock = stock
                return True
        return False

    def solicitar_reposicion(self):
        if self.Stock < 50:
            print("Solicitando y reponiendo productos...")
            if self.descontarStock(300):
                self.Stock += 300
                print("Productos repuestos en la sucursal.")
            else:
                print("No hay suficiente stock en la bodega para reponer.")



