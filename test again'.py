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