def gran_de_tres(z,x,y):
    a=z
    if(x>y):
        if(x>z): # x>y and x>z
            a=x
        elif (z>x):# x>y and z > x => z és el major
            a=z
        else: #Aqui x = z > y => x,z són els majors
            a=x 
    elif (y>x): # y>x
        if (y>z): #y>x and y>z => z es el major
            a=y
        elif(z>y): #y
            a=z
        else: #Aqui y > x and z=y ==>z, y són els majors
            a = y
    else: # x=y
        if (x>z):
            a = x
        elif (z>x):
            a=z
        else:
            a = x
a=int(input("Numero1: "))
b=int(input("Numero 2: "))
c=gran_de_tres(a,b)
print("El major de", a, "i", b, "és", c)