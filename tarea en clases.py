#crear una funcion para calcular el area de un cuadrado, rectangulo y triangulo
def areacuadrado(lado1, lado2):
    resultado = (lado1 * lado2)
    return resultado


def arearectangulo(largo, ancho):
    resultado = (largo * ancho)
    return resultado


def areatriangulo(base, altura):
    resultado = ((base * altura)/2)
    return resultado

print(" ")
print("1. cuadrado")
print("2. rectangulo")
print("3. triangulo")
opcion = int(input("Seleccionar una operacion a realizar: "))
if opcion == 1:
    lado1 = int(input("lado 1"))
    lado2 = int(input("lado 2"))
    print("el area es ", lado1 * lado2)
elif opcion == 2:
    largo = int(input("largo"))
    ancho = int(input("ancho"))
    print("el area es ", largo * ancho)
elif opcion == 3:
    base = int(input("base"))
    altura = int(input("altura"))
    print("el area es ", (base * altura) / 2)