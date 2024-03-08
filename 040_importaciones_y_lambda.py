import math

#funcion normal
def area(radio):
	resultado = math.pi * radio * radio
	print(resultado)

area(2)

#funcion lamdba
area = lambda radio: (math.pi * radio * radio)

print(area(2))