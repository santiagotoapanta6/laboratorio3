import math
r = int(input("ingrese el el radio del circulo : "))

def area():
	a = (r * r) * math.pi
	print (round(a,2))
calculo = area()
print (calculo)