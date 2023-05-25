from clases.classUsuario import usuario
import json
import os

class Vendedor(usuario):
    __sueldo_base = int
    comisiones = int
    
    def __init__(self, rut, nombre, apellido, email, password, sueldo_base, comisiones):
        super().__init__(rut, nombre, apellido, email, password)        
        self.__sueldo_base =sueldo_base
        self.comisiones = comisiones

    def getRut(self):
        return self.rut

    def getSueldoBase(self):
        return self.__sueldo_base
    
    def setSueldoBase(self, sueldo):
        if sueldo >= 0:
            self.__sueldo_base = sueldo
        else:
            print('El sueldo debe ser mayor a 0')

    def calcularComision(self,monto):
        self.comisiones += int(monto * 0.05) # Comision del 5%

# cargar vendedores desde json
def load_vendedores():
    # Obtener la ubicación del archivo .py actual
    ubicacion_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la ruta completa del archivo JSON
    ruta_json = os.path.join(ubicacion_actual, 'vendedores.json')
    vendedores = []
    try:
        with open(ruta_json, 'r') as archivo:
            data = json.load(archivo)
            for vendedor_data in data:
                vendedor = Vendedor(
                    vendedor_data['rut'],
                    vendedor_data['nombre'],
                    vendedor_data['apellido'],
                    vendedor_data['email'],
                    vendedor_data['password'],
                    vendedor_data['sueldo_base'],
                    vendedor_data['comisiones']
                )
                vendedores.append(vendedor)
    except:
        print('Error: No se encontro el archivo. Se procede a carga de vendedor temporal.')
        vendedor1 = Vendedor('11111111-1','Temporal', 'Temporal', 'a@a.a','temporal',0,0)
        vendedores.append(vendedor1)
    return vendedores

def saveVendedores(list_vendedores):
    # Obtener la ubicación del archivo .py actual
    ubicacion_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la ruta completa del archivo JSON
    ruta_json = os.path.join(ubicacion_actual, 'vendedores.json')
    data = []
    for vendedor in list_vendedores:
        vendedor_data = {
            'rut': vendedor.rut,
            'nombre': vendedor.nombre,
            'apellido': vendedor.apellido,
            'email': vendedor.email,
            'password': vendedor.password,
            'sueldo_base': vendedor.getSueldoBase(),
            'comisiones': vendedor.comisiones
        }
        data.append(vendedor_data)
    try:
        with open(ruta_json, 'w') as archivo:
            json.dump(data, archivo, indent=4)
    except Exception as e:
        print(f'Error al guardar archivo. {e}')

def cambiarContraseña(vendedor_Actual, list_vendedores):
    while True:
        print(f'CAMBIO DE CONTRASEÑA PARA {vendedor_Actual.nombre}')
        password = input('Ingrese nueva Contraseña: ')
        confirmPassword = input('Re ingrese nueva Contraseña: ')
        if password == confirmPassword:
            vendedor_Actual.password = password
            for i in range(len(list_vendedores)):
                if list_vendedores[i].rut == vendedor_Actual.rut:
                    list_vendedores[i] = vendedor_Actual
            saveVendedores(list_vendedores)
            input('Contraseña Actualizada. Presione enter para continuar. ')
            break
        else:
            print('Error: Contraseña no coinciden.\n')


