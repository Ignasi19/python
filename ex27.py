def llegir_llista():
    ll=[]
    for i in range(4):
      v = []
      v.append(input("Introdueix el nom: "))
      v.append(input("l'any de naixament "))
      ll.append(v)

anyactual = input("Any actual:")
b = []
for i in range (4):
    aux = []
    aux.append(input("nom"))
    aux.append(input("Any"))
    aux.append(anyactual-aux[1])
   b.append(aux)
