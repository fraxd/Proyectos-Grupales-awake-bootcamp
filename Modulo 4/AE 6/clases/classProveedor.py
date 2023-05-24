import pickle

class proveedor():
    rut = str  # Basicamente es numero de rut sin puntos, Solo con -
    nombreLegal = str
    razonSocial = str
    direccion = str
    pais = str
    personaJuridica = bool  # True = Persona Juridica | False = Persona Natural

    def __init__(self, rut, nombreLegal, razonSocial, pais, personaJuridica, direccion=''):
        self.rut = rut
        self.nombreLegal = nombreLegal
        self.razonSocial = razonSocial
        self.pais = pais
        self.personaJuridica = personaJuridica
        self.direccion = direccion

    def set_tipo_persona(self, tipo):  # TRUE ES juridica y False es Natural
        self.personaJuridica = tipo

class ProveedorConLogin(proveedor):
    def __init__(self, rut, nombreLegal, razonSocial, pais, personaJuridica, direccion='', nombre_usuario='', password=''):
        super().__init__(rut, nombreLegal, razonSocial, pais, personaJuridica, direccion)
        self.nombre_usuario = nombre_usuario
        self.password = password

def login(nombre_usuario, password):
    try:
        with open('proveedores.pickle', 'rb') as file:
            proveedores_existentes = pickle.load(file)
    except:
        print('No existe archivo de proveedores, cargando lista por defecto.')
        proveedores_existentes = []
    for proveedor in proveedores_existentes:
        if proveedor.nombre_usuario == nombre_usuario and proveedor.password == password:
            print("Login exitoso.")
            return proveedor

def saveData(listProveedores):
    with open("proveedores.pickle", "wb") as file:
        pickle.dump(listProveedores, file)
        
def ver_proveedores(self):        
    try:
        with open('proveedores.pickle', 'rb') as file:
            proveedores_existentes = pickle.load(file)
        
        for proveedor in proveedores_existentes:
            print("Proveedor:")
            print("RUT:", proveedor.rut)
            print("Nombre Legal:", proveedor.nombreLegal)
            print("Razón Social:", proveedor.razonSocial)
            print("País:", proveedor.pais)
            print("Persona Jurídica:", proveedor.personaJuridica)
            print("Dirección:", proveedor.direccion)
            print()  # Agregar línea en blanco para separar proveedores
    except FileNotFoundError:
        print("No se encontró el archivo de proveedores.")
    except EOFError:
        print("El archivo de proveedores está vacío.")

def proveedor_Default():
    dimarsa = ProveedorConLogin('77777777-k', 'Dimarsa S.A.',
                            'Dimarsa S.A', 'Chile', True, 'Por ahi 123', 'dimarsa', 'adidas')
    mallChino = ProveedorConLogin('888888888-k', 'Chino Originals S.A.',
                            'Chino Originals S.A', 'Chile', True, 'por aca #321', 'chino', 'adibas')
    return [dimarsa,mallChino]