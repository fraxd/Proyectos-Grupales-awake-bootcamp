from classproductos import Productos
from class_tienda import tienda
from classProveedor import proveedor

# class Sucursal(Bodega):
class Sucursal(tienda):
    nombre = str
    productos = list

    def __init__(self, nombre):
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

    def validarStock(self):
        if self.Stock<50:
            return False
    def anadirProductos(self,object):
        self.productos.append(object)
        return self.productos
    
    def print_provedores(self):
        for prov in self.provedores:
            print(prov.nombreLegal)
    
    def solicitar_reposicion(self):
        if self.Stock < 50:
            print("Solicitando y reponiendo productos...")
            if self.descontarStock(300):
                self.Stock += 300
                print("Productos repuestos en la sucursal.")
            else:
                print("No hay suficiente stock en la bodega para reponer.")
                
    def cargarStock(self):
        zapatillanike = Productos('001', 'Nike Revolution 6', 'zapatillas',self.provedores[0],'50', '64990')
        zapatillanaike = Productos('001', 'Naike Revolution 6', 'zapatillas',self.provedores[1],'50', '24990')
        poleranike = Productos('002', 'Nike Sportswear', 'poleras', self.provedores[0],'50', '19990')
        zapatosnike = Productos('003', 'Nike Air Max 90', 'zapatos',self.provedores[0],'50', '79990')
        poleronnike = Productos('004', 'Nike poleron', 'poleron',self.provedores[0],'50', '29990')
        chaquetanike = Productos('005', 'Nike chaqueta', 'chaqueta',self.provedores[0],'50', '39990')
        guantesnike = Productos('006', 'Nike Sportswear', 'guantes',self.provedores[0],'50', '9990')

        return [zapatillanike, zapatillanaike, poleranike, zapatosnike, poleronnike, chaquetanike, ]        


def cargarProvedores():
    dimarsa = proveedor('77777777-k','Dimarsa S.A.', 'Dimarsa S.A', 'Chile', True)
    mallChino = proveedor('888888888-k','Chino Originals S.A.', 'Chino Originals S.A', 'Chile', True)
    return [dimarsa, mallChino]