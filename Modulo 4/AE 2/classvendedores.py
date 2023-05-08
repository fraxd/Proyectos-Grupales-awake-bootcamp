class Vendedor():
    run = str
    nombre = str
    apellido = str
    seccion = str
    comisiones = int(0)

    def __init__(self, run, nombre, apellido, seccion):
            
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
    
    def getRun(self):
        return self.run

    def vender(self, cliente, producto, cant_Solicitada):
        producto.generarVenta(cant_Solicitada)
        self.comisiones += producto.getValor_neto()*0.005 ## 0.5%
        


