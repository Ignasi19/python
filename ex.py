def llegir_llista(a):
    l=[]
    for i in range(10): #hacemos un bucle de 10 elementos, 10 recorridos.
        l.append(input()) #append -> afegeix al  final de la llista #input -> Llegim del teclat
    return l

#programa principal
x = llegir_llista()
suma = 0
for e in x:
    If e [0]=="M":
        numM+=1
print ("Hay ", NumM ," Palabras que empiezan por M")