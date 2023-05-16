
class OrdenCompra:
    def __init__(self, id_ordencompra, producto, despacho):
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.despacho = despacho
        
    def vender(self, orden_compra):
        self.valor_neto = orden_compra.producto.precio
        self.impuesto = self.valor_neto * 0.19
        self.despacho = 5000 if orden_compra.despacho else 0
        self.valor_total = self.valor_neto + self.impuesto + self.despacho
        return self.valor_total