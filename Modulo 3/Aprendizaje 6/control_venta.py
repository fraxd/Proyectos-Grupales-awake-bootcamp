clientes = [
    {
        'id_clientes' : 1,
        'nombre' : 'Juan perez',
        'email' : 'juanitoxBellakito@gmail.com',
        'compras' : []
    },
    {
        'id_clientes' : 2,
        'nombre' : 'Ignacio Miranda',
        'email' : 'nachito1313@gmail.com',
        'compras' : []
    },
    {
        'id_clientes' : 3,
        'nombre' : 'Sofia araya',
        'email' : 'sofiaAraya@gmail.com',
        'compras' : []
    },
    
]



def menu_venta():
    print('best menu')




def printNumeroClientes():
    print(' Actualmente hay registrados',len(clientes),'Clientes.')

def compras():
    while True:
        try:
            id = int(input('Indique N° de cliente: ')) #Se asume que el n° cliente existe.
            break
        except: 
            print('Debes ingresar un numero entero.')
    while True:
        try:
            id_producto = int(input('Indique Id Producto: '))
            break
        except:
            print('Debe Ingresar un numero entero.')

printNumeroClientes()