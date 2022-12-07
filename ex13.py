def longitud(valor):
    
    if type(valor) is not list and type(valor) is not str:
        return -1

    contador = 0

    for elemento in valor:
        contador += 1
    return contador



cadena = "Hola"
print("Longitud de cadena:", longitud(cadena))
cadena = ""
print("Longitud de cadena:", longitud(cadena))
lista = ["Panic in Detroid", "Let me go", "Shattered"]
print("Longitud de lista:", longitud(lista))