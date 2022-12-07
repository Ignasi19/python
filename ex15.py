def sumar_llista(a):
    sumatori=0
    for i in a:
        sumatori+=i
    return i

def multiplicar_llista(llista):
    multiplicat=1
    for x in llista:
        multiplicat*=x
        return x


x=[1,2,3,4, 5, 7, 8, 15, 33]
print("El sumatori és: ", sumar_llista(x))
print("La multiplicació dels elements de la llista és: ", multiplicar_llista(x))