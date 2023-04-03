def calculem_aleatoris():
    b=[]
    for i in range(4):
        b.append(random.randint(0,9))
    return b
def llegir_n_usuari():
    b=[]
    for i in range(4):
        b.append(int(input("Introdueix un numero")))
    return b
import random
a=calculem_aleatoris()
stop=0
while stop !=1:
    b=llegir_n_usuari()
    if (a,b)==1:
        stop =1
    else: 
        stop=0
def comparar(a,b):
    x,y,z=0
    for i in range(4):
        if a [i]==b[i]:
            a+=1
        elif b[i] in a:
            b+=1
        else:
            c+=1
        if a==4:
            print("___")
            return 1
        elif a>0 and y>0:
            print("___")
            return 0
        elif a==0 and y>0:
            print("____")
            return 0
        elif a>0 and y==0:
            print("___")
            return 0
        else:
            print(  )
            return 0