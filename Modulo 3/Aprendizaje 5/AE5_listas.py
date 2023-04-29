
clientes = [
    {
        "nombre" : "Alexis" , 
        "edad" : 25 , 
        "id" : "54mtmtrg9df" 
    },
    {
        "nombre" : "Ana" , 
        "edad" : 18 , 
        "id" : "f9f335g" 
    },  
    {
        "nombre" : "Bera" , 
        "edad" : 33 , 
        "id" : "sgk5k339"
    },  
    {
        "nombre" : "Beni" , 
        "edad" : 19 , 
        "id" : "f3i4ntgjdf9" 
    },
    {
        "nombre" : "Camila" , 
        "edad" : 45 , 
        "id" : "dfk5443m3"      
    },  
    {
        "nombre" : "Carlos" , 
        "edad" : 41 , 
        "id" : ""   
    },
    {
        "nombre" : "Dani" , 
        "edad" : 33 , 
        "id" : "4i392gm" 
    },  
    {
        "nombre" : "Mara" , 
        "edad" : 38 , 
        "id" : "k45m439g"   
    },
    {
        "nombre" : "Trinidad" , 
        "edad" : 43 , 
        "id" : "54m34mrg"
    }, 
    {
        "nombre" : "Carlota" , 
        "edad" : 26 , 
        "id" : "dm54m3349t"
    }         
]

productos = [
    {
        "nombre": "Apple 11",
        "precio": 4000000,
        "id_producto": 'A001',
        'color': "negro"
    },
    {
        "nombre": "Asus Laptop E410",
        "precio": 800000,
        "id_producto": "A023",
        'color': "plateado"   
    },
    {
        "nombre": "Tablet lenovo",
        "precio": 150000,
        "id_producto": "A084",
        'color': "blanco"
    },
    {
        "nombre": "Airpods",
        "precio": 270000,
        "id_producto": "A101",
        'color': "negro"
    },
    {
        "nombre": "Xiaomi Speaker",
        "precio": 91000,
        "id_producto": "A204",
        'color': "plateado"
    }
]


# ALTERNATIVA 1 PARA FORMAR LISTA DE COMPRA DE CLIENTES, Y VAYA AGREGANDO
lista_comprasclientes = []
for cliente_key, cliente_value in clientes.items():
    for producto_key, producto_value in productos.items():
        lista_comprasclientes.append((cliente_value, producto_value))
print(lista_comprasclientes)


#  ALTERNATIVA 2: COMPRA DE CLIENTES EN BASE A INGRESAR CANTIDAD DE PRODUCTOS 
# cantidad = int(input("Ingrese la cantidad de suscripciones spotify que compra: "))
# # for cantidad in productos:
# #     productos["precio"]* cantidad
# #     print(cantidad)
 
# # compras_clientes = {
# #     [
# #     clientes["alexis"], productos[0]["precio"] * cantidad
# #     clientes["alexis"], productos[1]["precio"] * cantidad
# #     clientes["alexis"], productos[2]["precio"] * cantidad
# #     clientes["alexis"], productos[3]["precio"] * cantidad
# #     clientes["alexis"], productos[4]["precio"] * cantidad
# #     [
# #     clientes["Ana"], productos(0)["precio"] * cantidad
# #     ],
# #     [
# #     clientes["Bera"], productos() * cantidad
# #     ],
# #     [
# #     clientes["Beni"], productos() * cantidad
# #     ],
# #     [
# #     clientes["Camila"], productos() * cantidad
# #     ],
# #     [
# #     clientes["Carlos"], productos() * cantidad
# #     ],
# #     [
# #     clientes["Dani"], productos() * cantidad
# #     ],
# #     [
# #     clientes["Mara"], productos() * cantidad
# #     ],
# #     [
# #     clientes["Trinidad"], productos() * cantidad
# #     ],
# #     [
# #     clientes["Carlota"], productos() * cantidad
# #     ], 
# # }
