print("Hacer llamada desde mi casa")
opcion = input("Contestan llamada? [S/N] ")
if opcion.upper() == "S":
    opcion = input("Preguntar ¿Quisiera compartir una merienda conmigo? [S/N] ")
    if opcion.upper() == "S":
        print("Cenar juntos")
        print("Empezar una amistad")
    elif opcion.upper() == "N":
        opcion = input("Preguntar ¿Disfrutarias de una bebida caliente? [S/N] ")
        if opcion.upper() == "S":
            print("Seleccionar el tipo de bebida que tomaran")
            bebida = input("Te, cafe o cocoa: ")
            if bebida.lower() == "te":
                print("Tomar té")
                print("Iniciar una amistad")
            elif bebida.lower() == "cocoa":
                print("Tomar cocoa")
                print("Iniciar una amistad")
            elif bebida.lower() == "cafe":
                print("Tomar cafe")
                print("Iniciar una amistad")
        elif opcion.upper() == "N":
            print("Rebatir")
            opcion = input("Alguna actividad recreacional? (dile uno de tus intereses) [S/N] ")
            if opcion.upper() == "S":
                print("por que no hacemos eso juntos?")
                print("compartir interes")
                print("iniciar una amistad")
