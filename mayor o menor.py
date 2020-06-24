#mayor, menor o igual a cero (0)
x = int(input("ingrese numero: "))
if x<0: print("menor a 0")
elif x>0: print("mayor a 0")
else: print("cero")

print("**************")

if x == 0:
    print("es igual a cero")
else:
    if x > 0:
        print(x, "es mayor a cero")
    else:
        print(x,"es menor a cero")