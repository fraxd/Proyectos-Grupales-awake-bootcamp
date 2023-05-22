from clases.classProveedor import proveedor
from clases.classproductos import Productos
import json

class tienda:
    def __init__(self):
        self.nombre_tienda = 'TeloVendo'
        self.provedores = cargarProvedores()
        self.productos = self.cargarStock()

    def guardar_productos(self): 
        def serializar_objeto(obj):
            if isinstance(obj, Productos):
                proveedor_serializado = serializar_objeto(obj.proveedor)  # Serializar el objeto Proveedor
                return {'sku': obj.sku, 'nombre': obj.nombre, 'categoria': obj.categoria, 'provedoor': obj.proveedor, 'stock': obj.stock, 'valor_neto': obj.valor_neto, '__impuesto': obj.getImpuesto(), 'descuento': obj.descuento}
            elif isinstance(obj, proveedor):
                return {'nombreLegal': obj.nombreLegal,'razonSocial': obj.razonSocial, 'direccion': obj.direccion, 'pais': obj.pais, 'personaJuridica': obj.personaJuridica}
            raise TypeError(f'No se puede serializar el objeto: {obj}')

        with open('productos.json', 'w') as file:
            json.dump(self.productos, file, default=serializar_objeto, indent=4)


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