def menu():
    print("""
        menu
        1. Dibuix1
        2. Dibuix2
        3. Sortir
    """)
    opcio=input("seleccioni el dibuix que vulgui:")
    return opcio
def crear_punts(a):
    match a:
        case "1":
            print("""  .  
                      . .
                     .   .
                      . .
                       . """)
        case "2":
            print("""
         .
         . . 
         . . .
         . . . .
         . . . . .
""")
opcio=2
while(opcio !=0):
    opcio = menu()
    crear_punts(opcio)
print("Adeu, ja hem acabat")                       