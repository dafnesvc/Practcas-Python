def funcion1():
	global num1
	num1 = 10

funcion1()

print(num1)

#Las funciones anidadas en Python
def funcion2():
	pass
def funcion3():
	print('String en la función anidada.')

funcion2()