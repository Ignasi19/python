def anho(a):
    if a%4==0 and (a%400>0 or a%100==0):
        print ("Es anho de traspaso")
    else:
        print("No es anho de traspaso")
#PP
b=input("Introduce un anho")
anho(int(b))