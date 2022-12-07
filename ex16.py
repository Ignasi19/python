def invertir(a):
   
   llista=list(a)
   a = llista[::-1]
   # b = str(a)
   return a

a = ("Serfi chino")
b = invertir(a)
for i in b:
    print(i)