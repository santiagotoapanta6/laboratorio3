a = float(input("ingrese su estatura en pulgadas : "))
b = float(input("ingrese su peso en libras : "))

def masa_corporal():
	p = round(b * 703,2)
	q = round(p / a,2)
	s = q / a
	print (round(s,1))

calculo = masa_corporal()
print (masa_corporal)

if s < 18.5:
    print('por debajo del peso')
elif s <= 24.9:
	print('saludable')
elif s <= 29.9:
	print('sobrepeso')
elif s <= 39.9:
	print('obeso')
elif s > 40:
	print('obesidad extrema')