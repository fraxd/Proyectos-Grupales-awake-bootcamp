import os
import pickle
import clases.classProveedor as classProveedor

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def cargar_proveedores_usuarios():
    try:
        with open('proveedores.pickle', 'rb') as file:
            return pickle.load(file)
    except:
        print('No existe archivo Proveedores, se procede a cargar por defecto.')
        return classProveedor.proveedor_Default()

def menu_proveedores():
    while True:
        print("\n--- Menú Proveedores ---")
        print("1. Ver datos del proveedor")
        print("2. Modificar contraseña del proveedor")
        print("9. Regresar al Menú principal")
        
        opcion = int(input("\n Indique su opción: "))
        
        match opcion:
            
            case 1:
                borrarPantalla()
                print("Datos del proveedor:")
                print(f"Nombre: {proveedor_selected.nombreLegal}")
                print(f"Rut: {proveedor_selected.rut}")
                print(f"Pais: {proveedor_selected.pais}")
                input("Presione Enter para continuar.")
            
            case 2:
                borrarPantalla()
                cambiarPassword()
                break
            case 9:
                break     
            case _:
                print("Opción no válida.")
                input("Presione Enter para continuar.")

def validar_login(userName, password):
    global proveedor_selected
    for proveedor in list_proveedores:
        if proveedor.nombre_usuario == userName and proveedor.password == password:
            print("Login exitoso.")
            proveedor_selected = proveedor
            return True
    return False    

def cambiarPassword():
    print(f'Cambiando contraseña para {proveedor_selected.nombre_usuario}')
    while True:
        password = input('Ingrese nueva contraseña: ')
        confirmPassword = input(' Re ingrese nueva contraseña: ')
        if(confirmPassword == password):
            proveedor_selected.password = password
            for i in range(len(list_proveedores)):
                if list_proveedores[i].nombre_usuario == proveedor_selected.nombre_usuario:
                    list_proveedores[i] = proveedor_selected
            print('Contraseña actualizada. Se procede a realizar guardado en "bd".')
            input('Presione enter para continuar')
            classProveedor.saveData(list_proveedores)
            break
        else:
            print('Las contraseñas no coinciden.')
## Inicio
global list_proveedores
list_proveedores = cargar_proveedores_usuarios()
global proveedor_selected
