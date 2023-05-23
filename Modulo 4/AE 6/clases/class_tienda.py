from clases.classProveedor import proveedor as proveedorClass
from clases.classproductos import Productos
import json

class tienda:
    def __init__(self):
        self.nombre_tienda = 'TeloVendo'
        self.provedores = cargarProvedores()
        self.productos = self.cargar_datos()

    # Funcion que guarda el stock en un JSON
    def guardar_productos(self): 
        def serializar_objeto(obj):
            if isinstance(obj, Productos):
                proveedor_serializado = serializar_objeto(obj.proveedor)  # Serializar el objeto Proveedor
                return {'sku': obj.sku, 'nombre': obj.nombre, 'categoria': obj.categoria, 'proveedor': obj.proveedor, 'stock': obj.stock, 'valor_neto': obj.valor_neto, '__impuesto': obj.getImpuesto(), 'descuento': obj.descuento}
            elif isinstance(obj, proveedorClass):
                return {'rut': obj.rut, 'nombreLegal': obj.nombreLegal,'razonSocial': obj.razonSocial, 'direccion': obj.direccion, 'pais': obj.pais, 'personaJuridica': obj.personaJuridica}
            raise TypeError(f'No se puede serializar el objeto: {obj}')

        with open('productos.json', 'w') as file:
            json.dump(self.productos, file, default=serializar_objeto, indent=4)

    #funcion que carga los datos del json y en caso contrario carga los datos basicos
    def cargar_datos(self):
        try:
            productos = []
            with open('productos.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    if 'proveedor' in item:
                        proveedor_data = item['proveedor']
                        proveedor = proveedorClass(proveedor_data['rut'], proveedor_data['nombreLegal'], proveedor_data['razonSocial'], proveedor_data['direccion'], proveedor_data['pais'], proveedor_data['personaJuridica'])


                        producto = Productos(item['sku'], item['nombre'],item['categoria'], proveedor, item['stock'], item['valor_neto'])
                        productos.append(producto)
            return productos
        except:
            print('No existe archivo de productos.json.  Se procede a cargar el stock inicial por defecto.')
            input('Presione enter para continuar: ')
            return self.cargarStock()


    def cargarStock(self):
        zapatillanike = Productos(
            1, 'Nike Revolution 6', 'zapatillas', self.provedores[0], 50, 64990)
        zapatillanaike = Productos(
            2, 'Naike Revolution 6', 'zapatillas', self.provedores[1], 50, 24990)
        poleranike = Productos(
            3, 'Nike Sportswear','poleras', self.provedores[0], 50, 19990)
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
        dimarsa = proveedorClass('77777777-k', 'Dimarsa S.A.',
                            'Dimarsa S.A', 'Chile', True)
        mallChino = proveedorClass('888888888-k', 'Chino Originals S.A.',
                            'Chino Originals S.A', 'Chile', True)
        return [dimarsa, mallChino]