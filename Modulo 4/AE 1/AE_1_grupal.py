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
    
juanperez = Clientes('juanperez', 'Juan', 'Pérez', 'juanitoxBellakito@gmail.com', '02/02/2020', 100000)
ignaciomiranda = Clientes('ignaciomiranda', 'Ignacio', 'Miranda', 'nachito1313@gmail.com', '03/03/2020', 80000)
sofiaaraya = Clientes('sofiaaraya', 'Sofia','Araya', 'sofiaAraya@gmail.com', '04/04/2020', 110000)
anasanchez = Clientes("anasanchez", "Ana", "Sánchez", "anaSanchez@mail.com", "2022-01-03", 100000)
carlosgomez = Clientes("carlosgomez", "Carlos", "Gómez", "carlosGomez@mail.com", "2022-01-03", 25000)


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

class Productos():
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

class Vendedor():
    run = str
    nombre = str
    apellido = str
    seccion = str
    
    def __init__(self, run, nombre, apellido, seccion):
            
            self.run = run
            self.nombre = nombre
            self.apellido = apellido
            self.seccion = seccion

vendedor1 = Vendedor('17888111-1', 'Pablo', 'Picasso', 'Zapatillas')
vendedor2 = Vendedor('18999666-9', 'Vincent', 'Vangoh', 'Poleras' )
vendedor3 = Vendedor("33333333-3", "Marcela", "Torres", "Zapatos")
vendedor4 = Vendedor("44444444-4", "Santiago", "Sánchez", "Poleron")
vendedor5 = Vendedor("55555555-5", "Lucía", "González", "Chaqueta")

clientes = [juanperez, ignaciomiranda, sofiaaraya, anasanchez, carlosgomez]

# Imprimir nombre y apellido de los clientes
for cliente in clientes:
    print(f"Nombre: {cliente.nombre}, Apellido: {cliente.apellido}")