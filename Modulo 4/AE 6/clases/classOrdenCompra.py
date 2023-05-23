class OrdenCompra:
    id_ordencompra = int
    productos = []
    despacho = bool
    subtotal = int
    total = int
    status = str

    def __init__(self, id_ordencompra, producto,subtotal):
        self.status = 'Pendiente'
        self.id_ordencompra = id_ordencompra
        self.productos = producto
        self.subtotal = int(subtotal)
        if self.subtotal >= 50000:  #Despacho gratis sobre 50k
            self.despacho = False
            self.total = self.subtotal
        else:
            self.despacho = True
            self.total = int(self.subtotal + 5000)

    def confirmar(self):
        self.status = 'Confirmada'
    
    def cancelar(self):
        self.status = 'cancelada'

