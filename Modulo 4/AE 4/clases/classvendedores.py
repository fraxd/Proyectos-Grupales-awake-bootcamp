class Vendedor():
    run = str
    nombre = str
    apellido = str
    seccion = str
    comisiones = int
    
    def __init__(self, run, nombre, apellido, seccion):
            
            self.run = run
            self.nombre = nombre
            self.apellido = apellido
            self.seccion = seccion
    
    def getRun(self):
        return self.run

    def vender(self, cliente, pedido):
        valor_neto = pedido.producto.getValor_neto()
        if cliente.generarCobro(valor_neto):
            self.comisiones = int(valor_neto*0.005) ## 0.5%
            pedido.producto.generarVenta(pedido.cantidad)
            print('Compra Aprobada')
            self.print_pedido(pedido)
            return True
        else:
            print('Saldo Insuficiente \nCompra Cancelada')
            return False
    

    def print_pedido(self, pedido):
        total_neto = pedido.producto.getValor_neto()
        print(f'Pedido N°: {pedido.id_ordencompra}')
        print(f'Producto: {pedido.producto.nombre}')
        print(f'Cantidad:{pedido.cantidad}')
        print(f'Valor neto: ${total_neto}')
        if pedido.despacho is False:
            print('Despacho: Gratis')
        else:
            print('Despacho: $5.000')
        print(f'Valor Total: ${pedido.total}')
