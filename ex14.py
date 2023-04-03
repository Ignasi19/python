def caracter(a):
    if (a=="a" or a=="e" or a=="i" or a=="o" or a=="u"):
        return True
    else:
        return False

a=input("Introdueix un caracter: ")
print("La funció ens indica si és vocal o consonant",(a))
