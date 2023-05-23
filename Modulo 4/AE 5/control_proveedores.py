
import os
from clases.classSucursal import Sucursal
from clases.classProveedor import ProveedorConLogin

global Sucursal_actual
Sucursal_actual = Sucursal()

def menu_proveedores():
    while True:
        print("\n--- Menú Proveedores ---")
        print("1. Ver datos del proveedor")
        print("2. Modificar datos del proveedor")
        print("3. Modificar contraseña del proveedor")
        print("4. Regresar al Menú principal")

        opcion = input("\nIngresa el número de opción: ")