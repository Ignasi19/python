def llegir():
    llista=[]
    a='a'
    while a!='.':
        a=input("Introdueix un número: ")
        if a!='.':
            llista.append (int(a))
    return tuple(llista)

def mostrar_majors_que(a, num):
    for e in a:
        if e>num:
            print(e)

x=llegir()
i=input("Introdueixi el numero que vol comparar: ")
mostrar_majors_que(x,int(i))