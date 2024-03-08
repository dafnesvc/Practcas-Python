#https://www.programacionfacil.org/cursos/python_basico/capitulo_36_kwargs_python.html

def colores (**kwargs):
	print("Este es el color " + kwargs['color1'] + '.')

colores(color1='rojo', color2='azul')