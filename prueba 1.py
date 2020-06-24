x = int(input("da el primer numero: ")) #se pide al usuario que ingrese un numero a eleccion
y = int(input("da el segundo numero: ")) #se pide al usuario que ingrese un numero a eleccion
z = int(input("da el tercer numero: ")) #se pide al usuario que ingrese un numero a eleccion

a = min(x, y, z) #se invoca la funcion del minimo en python para determinar el minimo valor
c = max(x,y,z) #se invoca la funcion del maximo en python para determinar el maximo valor
b = (x + y + z) - a - c #se le resta a b el maximo y el minimo para determinar el valor de b

print('numeros en orden: {}, {} y {}'.format(a, b, c)) #función integrada format() devuelve una representación formateada de un valor dato controlado por el especificador de formato