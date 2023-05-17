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

    def vender(self, cliente, producto, cant_Solicitada):
        valor_neto = producto.getValor_neto()
        if cliente.generarCobro(valor_neto):
            self.comisiones = int(valor_neto*0.005) ## 0.5%
            producto.generarVenta(cant_Solicitada)
            print('Compra Aprobada')
        else:
            print('Saldo Insuficiente \nCompra Cancelada')
        