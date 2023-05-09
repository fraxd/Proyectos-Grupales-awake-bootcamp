class Clientes():
    idcliente = int
    nombre = str
    apellido = str
    correo = str
    fechaderegistro = str
    __saldo = 10000
    
    def __init__(self, idclientes, nombre, apellido, correo, fechaderegistro):
        self.idcliente = idclientes
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fechaderegistro = fechaderegistro
        self.__saldo = 10000
        
    property 
    def agregar_saldo(self,saldo):
        self.__saldo += saldo
    property
    def mostrar_saldo(self):
        return self.__saldo
    
    def generarCobro(self, valorNeto):
        if valorNeto <= self.__saldo:
            self.__saldo -= valorNeto
            return True
        else:
            return False
    
juanperez = Clientes('1', 'Juan', 'Pérez', 'juanitoxBellakito@gmail.com', '02/02/2020')
ignaciomiranda = Clientes('2', 'Ignacio', 'Miranda', 'nachito1313@gmail.com', '03/03/2020')
sofiaaraya = Clientes('3', 'Sofia','Araya', 'sofiaAraya@gmail.com', '04/04/2020')
anasanchez = Clientes("4", "Ana", "Sánchez", "anaSanchez@mail.com", "2022-01-03")
carlosgomez = Clientes("5", "Carlos", "Gómez", "carlosGomez@mail.com", "2022-01-03")


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

#clientes = [juanperez, ignaciomiranda, sofiaaraya, anasanchez, carlosgomez]

# Imprimir nombre y apellido de los clientes
#for cliente in clientes:
#    print(f"Nombre: {cliente.nombre}, Apellido: {cliente.apellido}, Saldo:{mostrar_saldo(cliente)}")