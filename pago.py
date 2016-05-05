x = int(input("ingrese el valor de la cena a comer : "))
def pago():
	a = (x * 12)/100
	print (a)
	return x + a
calculo = pago()
print (calculo)