a=[1,2,4,8,16,32,64]
i=0
for c in a:
    a[i]=c+1
    print(a[i])
    i+=1
b=["h", "o", "l", "a"]
for c in b:
    print(c)
a.append(128)
print(a)

b.extend(['P', 'e', 'r', 'e'])
print(b)

c = a + b
print(c)

c.insert(9,256)
print(c)


a=[1,2,3]
b=tuple(a)
for e in b: 
    print (e)
for i in range(len(b)):
    print(i)
for i,e in enumerate(b):
    print ("Posició:",i,"valor:",e)
x,y,z=b
print( "x=", x, "y=",y, "z=", z)