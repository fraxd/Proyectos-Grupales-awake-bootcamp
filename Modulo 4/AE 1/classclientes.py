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

clientes = [juanperez, ignaciomiranda, sofiaaraya, anasanchez, carlosgomez]

# Imprimir nombre y apellido de los clientes
for cliente in clientes:
    print(f"Nombre: {cliente.nombre}, Apellido: {cliente.apellido}, Saldo:{cliente.mostrar_saldo()}")