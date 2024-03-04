#https://www.programacionfacil.org/cursos/python_basico/capitulo_35_args_argumentos_python.html
print('Ejercicios del capítulo 35')
#¿Cuántos argumentos se utilizan en cada una de estas llamadas?

def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')

#Completa el siguiente fragmento de código:
print('\n')
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo', 'azul')


#Crea una función que realice la suma de cinco números utilizando solo *args. Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().
print('\n')
def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco números es:', resultado)

suma(5, 7, 45, 8657, 3, 4)

print('\n')
