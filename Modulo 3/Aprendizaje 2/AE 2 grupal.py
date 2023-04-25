
mensaje_motivador = "Francisco: weno pa la pega, Pablo: Pongale Weno, Rafael: Arriba los corazones, Patricio: Dale una hora mas metiendo mano, Franco: ponte a trabajar wn"

while True:
    mensaje_motivador = mensaje_motivador.upper()
    print('En mayusculas: ', mensaje_motivador)
    lista_motivadora= mensaje_motivador.split()

    #buscador de compañero en la lista
    ## print(lista_motivadora.index("PATRICIO:"))

    print('El string tiene ', len(lista_motivadora))
    tupla_motivadora = tuple(lista_motivadora)
    print(tupla_motivadora)
    print('Ingrese Nuevo Mensaje Motivador:')
    mensaje_motivador = input()
