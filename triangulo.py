import math
a = int(input("ingrese el primer lador del triangulo : "))
b = int(input("ingrese el segundo lador del triangulo : "))
c = int(input("ingrese el tercer lador del triangulo : "))

def area_perim():
	s = (a + b + c)/2
	t = s * (s - a) * (s - b) * (s-c)
	v = math.sqrt(t)
	print (round(v,2))
calculo = area_perim()
print (calculo)