import os
from classBodega import Bodega
class Sucursal(Bodega):
    def __init__(self) -> None:
        super().__init__()
        self.nombre = str
        self.direccion = str
        self.stock = int
        self.productos = list

    def validarStock(self):
        if self.Stock<50:
            return False
    def anadirProductos(self,object):
        self.productos.append(object)
        return self.productos
    
    def solicitar_reposicion(self):
        if self.Stock < 50:
            print("Solicitando y reponiendo productos...")
            if self.descontarStock(300):
                self.Stock += 300
                print("Productos repuestos en la sucursal.")
            else:
                print("No hay suficiente stock en la bodega para reponer.")