class Productos():
    sku = int
    nombre = str
    categoria = str
    proveedor = object
    stock = str
    valor_neto = int
    __impuesto = 1.19
    descuento = int 
    
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto):
        
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.descuento = 0
    
    def actualizarPrecio(self, nuevo_precio: int):
        self.valor_neto = nuevo_precio
    
    def actualizarPrecio(self, nuevo_precio: str): ## Porcentaje
        porcentaje  = nuevo_precio.split('%')
        porcentaje_int = int(porcentaje(0))/100 + 1
        self.valor_neto = self.valor_neto * porcentaje_int 

    def generarVenta(self, cant_pedida):
        self.stock -= cant_pedida

    def getValor_neto(self):
        return self.valor_neto
    
    def activarDescuento(self, porcentaje):
        self.descuento = porcentaje
        porcentaje = 100 -  porcentaje
        self.valor_neto = self.valor_neto * ( porcentaje / 100)
        return self.valor_neto
    
    def desactivarDescuento(self):
        porcentaje = 100 - self.descuento
        self.descuento = 0
        self.valor_neto = self.valor_neto * 100 / porcentaje
        return self.valor_neto




zapatillanike = Productos('001', 'Nike Revolution 6', 'zapatillas','dimarsa',20, 64990)
poleranike = Productos('002', 'Nike Sportswear', 'poleras','dimarsa','10', '19990')
zapatosnike = Productos('003', 'Nike Air Max 90', 'zapatos','dimarsa','15', '79990')
poleronnike = Productos('004', 'Nike Sportswear', 'poleron','dimarsa','3', '29990')
chaquetanike = Productos('005', 'Nike Sportswear', 'chaqueta','dimarsa','5', '39990')
guantesnike = Productos('006', 'Nike Sportswear', 'guantes','dimarsa','4', '9990')


        # 'id_producto': 2,
        # 'producto': 'Poleras',
        # 'stock': '10'

        # 'id_producto': 3,
        # 'producto': 'Zapatos',
        # 'stock': '15'

        # 'id_producto': 4,
        # 'producto': 'Poleron',
        # 'stock': '3'

        # 'id_producto': 5,
        # 'producto': 'Chaqueta',
        # 'stock': '5'



    
