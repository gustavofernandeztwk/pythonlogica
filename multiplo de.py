numero=int(input("ingrese valor: "))
mult4=numero%4
if mult4==0:
    print("el valor es multiplo de 4")
    print("es multiplo de 2")
elif mult4!=0:
    mult2=numero%2
    if mult2==0:
        print("el valor es multiplo de 2")
    else:
        print("el valor no es multiplo de 2")


print("********************")

numero=int(input("Ingrese el valor a evaluar: "))
if numero%4==0 and numero%2==0:
    print("El valor es múltiplo de 4 y de 2")
elif numero%2==0:
    print("El valor es multiplo de 2")
else:
    print("El valor no es multiplo de 2 ni de 4")
