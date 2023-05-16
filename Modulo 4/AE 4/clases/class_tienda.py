from clases.classProveedor import proveedor

class tienda:
    nombre_tienda = str
    provedores = list

    def __init__(self,nombre):
        self.nombre = nombre
        self.provedores = []

