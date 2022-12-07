def gran(z,e):
    if(z>e):
        print(z, "es major que" ,e)
        a=z
    elif(e>z):
        print(e, "es major que", z)
    else:
        print(e,"y", z,"son el mateix")
    return a
a=int(input("Numero1: "))
b=int(input("Numero 2: "))
c=gran(a,b)
print("El major de", a, "i", b, "és", c)