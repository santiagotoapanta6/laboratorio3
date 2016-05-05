x = int(input("ingrese un numero a sumar, por favor : "))
y = int(input("ingrese un numero a sumar, por favor : "))
def suma():
     return x + y
calculo = suma()
print (calculo)

a = int(input("ingrese un numero a restar, por favor : "))
b = int(input("ingrese un numero, por favor : "))
def resta():
     return a - b
calculo = resta()
print (calculo)

c = int(input("ingrese un numero a multiplicar, por favor : "))
d = int(input("ingrese un numero a multiplicar, por favor : "))
def multiplicacion():
     return c * d
calculo = multiplicacion()
print (calculo)

e = int(input("ingrese el dividendo, por favor : "))
f = int(input("ingrese el divisor, por favor : "))
def division():     
     return e / f
     if f == 0:
     	print ('error')
calculo = division()
print (calculo)