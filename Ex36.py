def llegir_numero():
    return(int(input("Introdueix nun valor: ")))
def llegir_numero_float():
    return (float(input("Introdueix un valor real: ")))
def calcular_prestec (q,i,a):
    return(q * (1 + i/100) **a)

q=llegir_numero()
i=llegir_numero()
a=llegir_numero()
c=calcular_prestec(q,i,a)
print("Si solicita {} a un interés aunal del {} a {} anys, al final pagaré {} euros" .format(q,i,a,c))