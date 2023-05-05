class Clientes():
    idcliente = str
    nombre = str
    apellido = str
    correo = str
    fechaderegistro = str
    __saldo = int
    
    def __init__(self, idclientes, nombre, apellido, correo, fechaderegistro, saldo):
        self.idclientes = idclientes
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fechaderegistro = fechaderegistro
        self.__saldo = saldo
        
        
    def agregar_saldo(self,saldo):
        self.__saldo += saldo
        
    def mostrar_saldo (self):
        return self.__saldo
    
juanperez = Clientes(idcliente ='juanperez', nombre = 'juan', apellido = 'perez', correo = 'juanitoxBellakito@gmail.com', fechaderegistro = '02/02/2020', saldo = 100000)   
#4 mas

# 'id_clientes' : 1,
#         'nombre' : 'Juan perez',
#         'email' : 'juanitoxBellakito@gmail.com',
#         'compras' : []
#     },
#     {
#         'id_clientes' : 2,
#         'nombre' : 'Ignacio Miranda',
#         'email' : 'nachito1313@gmail.com',
#         'compras' : []
#     },
#     {
#         'id_clientes' : 3,
#         'nombre' : 'Sofia araya',
#         'email' : 'sofiaAraya@gmail.com',
#         'compras' : []

class Productos() :
    sku = str
    nombre = str
    categoria = str
    proveedor = str
    stock = str
    valor_neto = int
    __impuesto = 1.19
    
    
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto):
        
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto

zapatillanike = Productos('001', 'Nike Revolution 6', 'zapatillas','dimarsa','20', '64990')
#5 mas instancias

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

class Vendedor():
    run = str
    nombre = str
    apellido = str
    seccion = str
    __Comision = 0
    
def __init__(self, run, nombre, apellido, seccion):
        
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion

vendedor1 = ('17888111-1', 'Pablo', 'Picasso', 'Zapatillas')
#asi 4 instancias mas

  
    
    
        
    
   
    
    

        
    
        
    