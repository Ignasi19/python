# Definició de funcions auxiliars
def menu_principal():
    print(""" Calculadora
         Menú:
         1. Números enters
         2. Números reals
         3. Canvis de base
         0. Sortir
""")
    opcio=input("Seleccioni l'opció que vulgui: ")
    return opcio


#Funció del menú de numeros enters
def menu_enters():
    print("""
            Menú calculadora de números enters:
            1. Sumar
            2. Restar
            3. multiplicar
            4. Dividir
            5. Potència
            6. Mòdul
            0. Sortir
            """)
    opcio=input
    return opcio

# Funció del menú dels numeros reals
def menu_reals():
    print("""
            Menú calculadora numeros enters:
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potència
            0. Sortir
            """)
    opcio=input("seleccioni l'opció que vulgui: ")
    return opcio
#Funció del menú dels canvis de base
def menu_canvis_base():
    print("""
            1. Donat un binari passar a octal, decimal i hexadecimal.
            2. Donat un octal passar a binari, decimal i hexadecimal.
            3. Donat un decimal passar a binari, octal i hexadecimal.
            4. Donat un hexadecimal passar a binari, octal i decimal.
            0. Sortir
    """)
# funcions canvis de base
# Función que regresa el verdadero valor hexadecimal.
# Por ejemplo, si recibe un 15 devuelve f, y si recibe un número menor a 10, devuelve el número sin modificarlo
def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)


def hexadecimal_a_decimal(hexadecimal):
    # Convertir a minúsculas para hacer las cosas más simples
    hexadecimal = hexadecimal.lower()
    # La debemos recorrer del final al principio, así que la invertimos
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0
    for digito in hexadecimal:
        # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
        valor = obtener_valor_real(digito)
        elevado = 16 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal


def decimal_a_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal


def octal_a_decimal(octal):
    decimal = 0
    posicion = 0
    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
    octal = octal[::-1]
    for digito in octal:
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal


def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario


def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    # Invertir la cadena porque debemos recorrerla de derecha a izquierda
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal
# Programa principal de la calculadora
opcio=1
while(opcio!=0):
    opcio=menu_principal()
    match opcio:
            case "1":
                opcio2=menu_enters
                a = int (input("indiqui el primer operand: "))
                b = int (input("indiqui el segon operand: "))
                match opcio2:
                        case "1":
                            c=a+b
                            print ("La suma de ",a," més ",b," és",c)
                        case "2":
                            c=a-b
                            print("La resta de ",a," menys",b," és",c)
                        case "3":
                            c=a*b
                            print("la multiplicació de ",a," per ",b," és ",c)
                        case "4":
                            c=a/b
                            print("La divisió de ",a," per ",b," és ",c)
                        case "0":
                            print("Adeu")
                        case "5":
                            c=a ** b
                            print("La potencia de " , a, "elevat a " , b, " és " ,c)
                        case "6":
                            c = a % b
                            print
                        case other:
                            print("El mòdul de " , a, " elevat a ", b, " és ", c)
            case "2":     
                    print("""
                    Menú calculadora de números reals:
                    1. Sumar
                    2. Restar
                    3. multiplicar
                    4. Dividir
                    0. Sortir
                    """)
    a = input("indiqui el primer operand: ")
    b = input("indiqui el segon operand: ")

match opcio:
            case "1":
                c=float(a)+float(b)
                print ("La suma de ",a," més ",b," és",c)
            case "2":
                c=float(a)-float(b)
                print("La resta de ",a," menys",b," és",c)
            case "3":
                c=float(a)*float(b)
                print("la multiplicació de ",a," per ",b," és ",c)
            case "4":
                c=float(a)/int(b)
                print("La divisió de ",a," per ",b," és ",c)
            case "0":
                print("Adeu")
            case "other":
                    print("Opció no vàlida")
            case "3":

                print("""
                        Menú calculadora canvis de base:
                        1. Donat un binari passar a octal, decimal i hexadecimal.
                        2. Donat un octal passar a binari, decimal i hexadecimal.
                        3. Donat un decimal passar a binari, octal i hexadecimal.
                        4. Donat un hexadecimal passar a binari, octal i decimal.
                        0. Sortir
                        """)
match =input("Seleccioni l'opció que vulgui: ")
a = input("Indiqui el número a convertir: ")
match opcio2:
                case "1": # Binari a
                    b=int(a,base=8)
                    c=int(a,base=10)
                    d=int(a,base=16)
                    print("El número ",a," en octal= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "2": # Octal a
                    b=int(a,base=2)
                    c=int(a,base=10)
                    d=int(a,base=16)
                    print("El número ",a," en binari= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "3": # Decimal a
                    b=int(a,base=2)
                    c=int(a,base=8)
                    d=int(a,base=16)
                    print("El número ",a," en binari= ",b, " en octal= ",c," en hexadecimal= ", d)
                case "4": # Hexadecimal a
                    b=int(a,base=2)
                    c=int(a,base=8)
                    d=int(a,base=10)
                    print("El número ",a," en binari= ",b, " en octal= ",c," en decimal= ", d)
                case "0":
                    print("Adéu")
                case other:
                    print("Opció no vàlida!")
case :print("Adéu")