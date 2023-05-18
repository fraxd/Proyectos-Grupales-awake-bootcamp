import clases.classproductos as classproductos
class OrdenCompra:
    id_ordencompra = int
    producto = classproductos.Productos
    cantidad = int
    despacho = bool
    subtotal = int
    total = int
    status = str

    def __init__(self, id_ordencompra, producto, cantidad,):
        self.status = 'Pendiente'
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = int(producto.getValor_total() * cantidad)
        if self.subtotal >= 50000:  #Despacho gratis sobre 50k
            self.despacho = False
            self.total = self.subtotal
        else:
            self.despacho = True
            self.total = self.subtotal + 5000


