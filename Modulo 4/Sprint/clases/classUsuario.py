class usuario:
    rut = str # Rut con -
    nombre = str
    apellido = str
    email = str
    password = str

    def __init__(self, rut, nombre, apellido, email, password):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def presentarse(self):
        print('Hola! soy {self.nombre} {self.apellido}')