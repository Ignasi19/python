def llegir_numero():
    return(int(input("   ")))
def escriure_serie(a):
    suma=0
    for i in range(a,1,-4):
        suma +=i*2
        print("La suma dels quadrats separats ente si de {} és {}" .format(a, suma))

a=llegir_numero()
escriure_serie(a)