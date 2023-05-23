
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
                print(f"Nombre: {proveedor_actual.nombre}")
                print(f"Rut: {proveedor_actual.rut}")
                print(f"Contraseña: {proveedor_actual.contraseña}")
                print(f"Productos: {proveedor_actual.productos}")
                input("Presione Enter para continuar.")
            
            case 2:
                borrarPantalla()
                while True:
                    nueva_contraseña = input("Ingrese la nueva contraseña: ")
                    if len(nueva_contraseña) >= 8:
                        break
                    else:
                        print("La contraseña debe tener al menos 8 caracteres.")
                proveedor_actual.contraseña = nueva_contraseña
                print("Contraseña modificada exitosamente.")
                input("Presione Enter para continuar.")
            
            case 9:
                break
            
            case _:
                print("Opción no válida.")
                input("Presione Enter para continuar.")
