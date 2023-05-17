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

    property

    def agregar_saldo(self, saldo):
        self.__saldo += saldo
        return self.__saldo

    property

    def saldo(self):
        return self.__saldo

    def actualizar_saldo(self, saldo):
        self.__saldo = saldo
        return self.__saldo

    def generarCobro(self, valorNeto):
        if valorNeto <= self.__saldo:
            self.__saldo -= valorNeto
            return True
        else:
            return False        