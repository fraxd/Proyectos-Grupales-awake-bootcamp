import clases.classproductos as classproductos
class OrdenCompra:
    id_ordencompra = int
    producto = classproductos.Productos
    id_cliente = int
    ind_vendedor = int
    cantidad = int
    despacho = int
    subtotal = int
    total = int
    nombre_sucursal = str

    def __init__(self, id_ordencompra, id_cliente, id_vendedor, producto, cantidad,nombre_sucursal):
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.cantidad = cantidad
        self.id_cliente = id_cliente
        self.ind_vendedor = id_vendedor
        self.subtotal = producto.getValor_total() * cantidad
        if self.subtotal >= 50000:  #Despacho gratis sobre 50k
            self.despacho = 0
        else:
            self.despacho = 5000
        self.total = self.subtotal + self.despacho
        self.nombre_sucursal = nombre_sucursal


    def print_pedido(self):
        print(f'Pedido N°: {self.id}')
        print(f'Producto: {self.producto}')
        print(f'Cantidad:{self.cantidad}')
        print(f'Id Cliente: {self.id_cliente}')
        print(f'')
