import pickle
import os
class proveedor():
    rut = str  # Básicamente es número de rut sin puntos, solo con guiones
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
    def __init__(self, nombre_usuario='', password=''):
        super().__init__('', nombre_usuario, '', '', False, '')
        self.nombre_usuario = nombre_usuario
        self.password = password



    def login(self):
        file_path = 'Modulo 4/AE 5/clases/proveedores.pickle'
        
        if os.path.getsize(file_path) > 0:
            with open(file_path, 'rb') as file:
                proveedores_existentes = pickle.load(file)
        else:
            proveedores_existentes = []

        for proveedor in proveedores_existentes:
            if proveedor.nombre_usuario == self.nombre_usuario and proveedor.password == self.password:
                print("Login exitoso.")
                return
            
    def ver_proveedores(self):
        file_path = 'Modulo 4/AE 5/clases/proveedores.pickle'
        
        try:
            with open(file_path, 'rb') as file:
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