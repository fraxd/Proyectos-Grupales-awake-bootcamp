from .classproductos import Productos
from .class_tienda import tienda
from .classProveedor import proveedor

# class Sucursal(Bodega):


class Sucursal(tienda):
    nombre = str
    productos = list

    def __init__(self, nombre = ''):
        self.nombre_tienda = 'Te lo Vendo'
        self.nombre = nombre
        self.provedores = cargarProvedores()
        self.productos = self.cargarStock()

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
            "Proveedor :", produ.proveedor.nombreLegal, "Stock :", produ.stock, "Precio :", produ.valor_neto)

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

    def cargarStock(self):
        zapatillanike = Productos(
            1, 'Nike Revolution 6', 'zapatillas', self.provedores[0], 52, 64990)
        zapatillanaike = Productos(
            2, 'Naike Revolution 6', 'zapatillas', self.provedores[1], 51, 24990)
        poleranike = Productos(3, 'Nike Sportswear',
                            'poleras', self.provedores[0], 58, 19990)
        zapatosnike = Productos(4, 'Nike Air Max 90',
                                'zapatos', self.provedores[0], 50, 79990)
        poleronnike = Productos(5, 'Nike poleron',
                                'poleron', self.provedores[0], 50, 29990)
        chaquetanike = Productos(
            6, 'Nike chaqueta', 'chaqueta', self.provedores[0], 50, 39990)
        guantesnike = Productos('006', 'Nike guantesWear',
                                'guantes', self.provedores[0], 50, 9990)

        return [zapatillanike, zapatillanaike, poleranike, zapatosnike, poleronnike, chaquetanike, guantesnike]


def cargarProvedores():
    dimarsa = proveedor('77777777-k', 'Dimarsa S.A.',
                        'Dimarsa S.A', 'Chile', True)
    mallChino = proveedor('888888888-k', 'Chino Originals S.A.',
                        'Chino Originals S.A', 'Chile', True)
    return [dimarsa, mallChino]
