class Sucursal():
    nombre : str
    direccion : str
    stock : int
    productos: list

    def validarStock(self):
        if self.stock<50:
            return False
    def anadirProductos(self,object):
        self.productos.append(object)
        return self.productos
    