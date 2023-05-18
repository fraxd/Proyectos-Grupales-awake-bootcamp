from clases.classProveedor import proveedor
from clases.classBodega import Bodega
class tienda:
    def __init__(self):
        self.nombre_tienda = 'TeloVendo'
        self.provedores = cargarProvedores()
        self.bodega_principal = Bodega()

def cargarProvedores():
        dimarsa = proveedor('77777777-k', 'Dimarsa S.A.',
                            'Dimarsa S.A', 'Chile', True)
        mallChino = proveedor('888888888-k', 'Chino Originals S.A.',
                            'Chino Originals S.A', 'Chile', True)
        return [dimarsa, mallChino]