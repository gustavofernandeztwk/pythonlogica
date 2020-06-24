#profesor le envio el codigo de los dos ejercicios, no pude subirlo a github porque intente in no pude
#espero me disculpe, necesitamos ver en clases como usar github, saludos



print("hacer una llamada telefonica")
opcion = input("contestar llamada [S/N]")
if opcion.upper() == "S":
    opcion = input("quieres merendar conmigo [S/N]")
if opcion.upper() == "N":
    opcion = input("disfrutarias de una bebida caliente [S/N]")
    if opcion.upper() == "S":
        print(" ")
        print("1. te")
        print("2. cafe")
        print("3. cocoa")
        opcion = int(input("Seleccionar un actividad a realizar: "))
if opcion == 1:
    print("empezar una amistad")
elif opcion == 2:
    print("empezar una amistad")
elif opcion == 3:
    print("empezar una amistad")
elif opcion.upper() == "S":
    print("empezar una amistad")

************
#realizar las 4 operaciones basicas (+,-,*,/)
#para ello solicitar el ingreso de dos numeros
numero = int(input("ingrese numero: "))
numero2 = int(input("ingrese numero: "))

print("resultado suma =", numero+numero2)
print("resultado resta, =", numero-numero2)
print("resultado multiplicacion, =", numero*numero2)
print("resultado division, =", numero/numero2)