stock=40 #- Definir el stock de un producto en una variable.
print("Bienvenido(a) a 'Te lo vendo'")
while stock>0: #- El programa debe verificar que existan unidades disponibles.

    ss=input("Ingrese comando (stock/unidades) :")

    if ss=="stock": #- Definir una forma de solicitar el stock disponible del producto por consola.
            print("stock actual "+str(stock)+".")

    if ss=="unidades": #- Definir una forma de solicitar unidades del producto por consola. Este número de productos se almacenarán en una nueva variable llamada ‘Productos seleccionados’.  
        productos_seleccionados=int(input("Ingrese unidades a comprar : ")) 
        
        if productos_seleccionados>stock: #- Si el valor ingresado es superior al stock disponible, este debe entregar un mensaje indicando que no es posible realizar esta acción debido a que no hay stock suficiente.
            
            print("Stock insuficiente: No es posible realizar esta acción.") 
        
        else:

            if productos_seleccionados>20:  #- No se pueden solicitar más de 20 unidades en un mismo pedido.

                print("No se pueden solicitar más de 20 unidades.") 
            
            else:

                if productos_seleccionados>12 and stock>productos_seleccionados:  #- Verificar que el stock posibilite entregar una unidad extra.

                    productos_seleccionados=productos_seleccionados+1 #- Al verificar las unidades disponibles, el programa entregará una unidad extra cuando se seleccionen más de 12 unidades.   
                    
                    print("unidades entregadas(más un extra por docena.) : "+str(productos_seleccionados)) 

                elif productos_seleccionados>12 and stock==productos_seleccionados: #- Si no hay suficiente stock se entregan las unidades justas.

                    print("unidades entregadas(sin extra por falta de stock.) : "+str(productos_seleccionados)) 
                else:

                    print("unidades entregadas "+str(productos_seleccionados))

                stock=stock-productos_seleccionados #- Los productos reubicados serán descontados del stock inicial.

print("No queda stock.")




