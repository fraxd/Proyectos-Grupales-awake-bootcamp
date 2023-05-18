from clases.classProveedor import proveedor
from clases.classproductos import Productos

class tienda:
    def __init__(self):
        self.nombre_tienda = 'TeloVendo'
        self.provedores = cargarProvedores()
        self.productos = self.cargarStock()

    def cargarStock(self):
        zapatillanike = Productos(
            1, 'Nike Revolution 6', 'zapatillas', self.provedores[0], 52, 64990)
        zapatillanaike = Productos(
            2, 'Naike Revolution 6', 'zapatillas', self.provedores[1], 51, 24990)
        poleranike = Productos(
            3, 'Nike Sportswear','poleras', self.provedores[0], 58, 19990)
        zapatosnike = Productos(
            4, 'Nike Air Max 90','zapatos', self.provedores[0], 50, 79990)
        poleronnike = Productos(
            5, 'Nike poleron','poleron', self.provedores[0], 50, 29990)
        chaquetanike = Productos(
            6, 'Nike chaqueta', 'chaqueta', self.provedores[0], 50, 39990)
        guantesnike = Productos(
            7, 'Nike guantesWear','guantes', self.provedores[0], 50, 9990)

        return [zapatillanike, zapatillanaike, poleranike, zapatosnike, poleronnike, chaquetanike, guantesnike]
        

def cargarProvedores():
        dimarsa = proveedor('77777777-k', 'Dimarsa S.A.',
                            'Dimarsa S.A', 'Chile', True)
        mallChino = proveedor('888888888-k', 'Chino Originals S.A.',
                            'Chino Originals S.A', 'Chile', True)
        return [dimarsa, mallChino]