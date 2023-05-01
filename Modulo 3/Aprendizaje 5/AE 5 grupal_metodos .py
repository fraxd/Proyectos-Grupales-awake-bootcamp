import random
import time
from AE5_listas import clientes
from AE5_listas import productos

#Agregar Cliente
clientes.append({
    "nombre" : "Kevin" , 
    "edad" : 32 , 
    "id" : "nmksie532"
})

# Agregar Producto
productos.append({
    "nombre": "Reactor Nuclear ",
    "precio": 10000000,
    "id_producto": 'Z666',
    'color': "negro"
})

# Muestra lista de clientes 
for cliente in clientes:
    print("*" , "nombre cliente:", cliente["nombre"])
    print("--", "número id:",cliente["id"])

# Muestra lista de productos
for producto in productos:
    print("*" , "producto", producto["nombre"])
    print("--", "id:",producto["id_producto"])
    

# Eliminar Cliente Al azar
## si se recorre con un for con un random se puede elegir cualquiera no es necesario
## El random elegira un numero al azar del 0 hasta el largo de la lista, el numero elegido se elimina.
i = 0
delNumber = random.randint(0,len(cliente))
print(delNumber)
for cliente in clientes:
    if(i== delNumber):
        print('Cliente Eliminaod: ',cliente['nombre'])
        clientes.remove(cliente)
        break
    i= i+1

# Elimina Producto al azar
## Mismo metedo que el aterior
i = 0
delNumber = random.randint(0,len(productos))
print(delNumber)
for producto in productos:
    if(i== delNumber):
        print('Cliente Eliminaod: ',producto['nombre'])
        productos.remove(producto)
        break
    i= i+1

# Imprimir todas las claves usuarioscon delay 2 segundos
print('Claves Usuarios')
for cliente in clientes:
    for clave in cliente.keys():
        time.sleep(2)
        print(clave)
    break ## Se asume que con 1 vez basta ...

# Imprime todos los valores de usuarios
print('Valores Usuarios')
for cliente in clientes:
    for valor in cliente.values():
        time.sleep(3)
        print(valor)

# Imprimir todas las claves usuarioscon delay 2 segundos
print('Claves productos')
for producto in productos:
    for clave in producto.keys():
        time.sleep(2)
        print(clave)
    break ## Se asume que con 1 vez basta ...

# Imprime todos los valores de usuarios
print('Valores Productos')
for producto in productos:
    for valor in producto.values():
        time.sleep(3)
        print(valor)


