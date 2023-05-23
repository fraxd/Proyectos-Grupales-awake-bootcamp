from clases.class_tienda import tienda
import control_bodega


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

    def vender(self, cliente, pedido,valor_neto):
        if cliente.generarCobro(valor_neto):
            self.comisiones = int(valor_neto*0.01) ## 0.5%
            listaprodu=control_bodega.getProductoLista()
            print('Compra Aprobada')
            for prod in pedido.productos:
                for produ in listaprodu:
                    if produ.sku == prod.sku:
                        produ.generarVenta(prod.stock)
            self.print_pedido(pedido)
            return True
        else:
            print('Saldo Insuficiente \nCompra Cancelada')
            return False
    

    def print_pedido(self, pedido):
        for product in pedido.productos:
            print(f'Pedido N°: {pedido.id_ordencompra}')
            print(f'Producto: {product.nombre}')
            print(f'Cantidad:{product.stock}')
            precio = int(product.getValor_total()*product.stock)
            print(f'Valor neto: ${precio}')
            if pedido.despacho is False:
                print('Despacho: Gratis')
            else:
                print('Despacho: $5.000')
            
        print(f'Valor Total: ${pedido.total}')
