class Vendedor():
    run = str
    nombre = str
    apellido = str
    seccion = str
    direccion = str
    __comisiones = int(0)

    def __init__(self, run, nombre, apellido, seccion, direccion = ''):
            
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.direccion = direccion
    
    def getRun(self):
        return self.run

    def vender(self, cliente, producto, cant_Solicitada):
        valor_neto = producto.getValor_neto()
        if cliente.generarCobro(valor_neto):
            self.__comisiones += int(valor_neto*0.005) ## 0.5%
            producto.generarVenta(cant_Solicitada)
            print('Compra Aprobada')
        else:
            print('Saldo Insuficiente \nCompra Cancelada')
        


