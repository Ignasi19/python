def llegir_paraula():
    return (input("Introdueixi una paraula"))
def comparar_paraules(a,b):
    if a == b:
        print("Són iguals, per tant rima")
    elif a[-3:]==b[-3:]:
        print("Rimen, perquè les tres darreres són iguals")
    elif a[-1:]==b[-1:]:
        print("Rimen pquíssim, perque la darrera lletra es igual")
    else:
        print("No rimen")