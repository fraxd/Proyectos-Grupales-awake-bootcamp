class Productos():
    sku = int
    nombre = str
    categoria = str
    proveedor = object
    stock = int
    valor_neto = int
    __impuesto = 1.19
    descuento = int

    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto):

        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.descuento = 0

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

    def activarDescuento(self, porcentaje):
        self.descuento = porcentaje
        porcentaje = 100 - porcentaje
        self.valor_neto = self.valor_neto * (porcentaje / 100)
        return self.valor_neto

    def desactivarDescuento(self):
        porcentaje = 100 - self.descuento
        self.descuento = 0
        self.valor_neto = self.valor_neto * 100 / porcentaje
        return self.valor_neto
