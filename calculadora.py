#realizar las 4 operaciones basicas (+,-,*,/)
#para ello solicitar el ingreso de dos numeros
numero = int(input("ingrese numero: "))
numero2 = int(input("ingrese numero: "))

print("resultado suma =", numero+numero2)
print("resultado resta, =", numero-numero2)
print("resultado multiplicacion, =", numero*numero2)
print("resultado division, =", numero/numero2)

print("************************")

primerValor = int(input("Ingrese el primer valor: "))
segundoValor = int(input("Ingrese el segundo valor: "))
print(" ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
opc = int(input("Seleccionar un operacion a realizar: "))
#opc = opcion

if opc == 1:
    print(primerValor, "+", segundoValor, "=", (primerValor + segundoValor))
elif opc == 2:
    print(primerValor, "-", segundoValor, "=", (primerValor - segundoValor))
elif opc == 3:
    print(primerValor, "*", segundoValor, "=", (primerValor * segundoValor))
elif opc == 4:
    if segundoValor == 0:
        print("No es posible dividir por 0")  # Revisar casos puntuales
    else:
        print(primerValor, "/", segundoValor, "=", (primerValor / segundoValor))
