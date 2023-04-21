# definir un listado de 5 productos con su respectivo valor unitario. 
# ● Deberán crear un archivo .py el cual deberá solicitar ingresar una cantidad por cada producto (definido de la lista). 
# ● Se deberá mostrar en pantalla el total de la suma del pedido el que corresponde al valor neto. 
# ● Se deberá mostrar en pantalla el total del IVA (19%) del total de pedido ingresado. 
# ● Se deberá mostrar en pantalla el total final del pedido (la suma del valor neto + IVA)

suscripcion_spotify= 10000
cantidad_productos = int(input("Ingrese la cantidad de suscripciones spotify que compra: "))
total_spotify = cantidad_productos * suscripcion_spotify 

suscripcion_netflix= 7990
cantidad_productos = int(input("Ingrese la cantidad de suscripciones netflix que compra: "))
total_netflix = cantidad_productos * suscripcion_netflix 

juego_steam= 20000
cantidad_productos = int(input("Ingrese la cantidad de juegos steam que compra: "))
total_steam = cantidad_productos * juego_steam 

libro_amazon= 10000
cantidad_productos = int(input("Ingrese la cantidad de libros que compra: "))
total_amazon = cantidad_productos * libro_amazon 

cancion_itunes= 1000
cantidad_productos = int(input("Ingrese la cantidad de canciones por itunes que compra: "))
total_itunes = cantidad_productos * cancion_itunes 

total_valor_neto= total_spotify + total_netflix + total_steam + total_amazon + total_itunes
print("El total valor neto del pedido es:", total_valor_neto)

total_IVA= (19 * total_valor_neto) // 100
print("El total valor IVA del pedido es:", total_IVA)

total_compra= total_valor_neto + total_IVA
print("El total valor del pedido es:", total_compra)