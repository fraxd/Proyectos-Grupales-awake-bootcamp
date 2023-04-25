import random
import time
producto1= 120
producto2= 150
provee1=3
provee2=3
while True:
    print("Stock actual producto 1 :"+str(producto1))
    print("Stock actual producto 2 :"+str(producto2))
    for i in range(10):
        if producto1<100 and provee1>0:
            provee1=provee1-1
            producto1=producto1+50
            print("Enhorabuena los proveedores enviaron 50 'productos 1' más!!! ")
        if producto2<100 and provee2>0:
            provee2=provee2-1
            producto2=producto2+50
            print("Enhorabuena los proveedores enviaron 50 'productos 2' más!!! ")
        n=random.randint(1, 10)
        time.sleep(3)
        p=random.randint(1,2)
        if p==1:
            print("Alguien ha comprado 'producto 1' "+str(n)+" veces!!")
            producto1=producto1-n
        elif p==2:
            print("Alguien ha comprado 'producto 2' "+str(n)+" veces!!")
            producto2=producto2-n
        
    