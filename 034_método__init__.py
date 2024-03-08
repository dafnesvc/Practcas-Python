#https://www.programacionfacil.org/cursos/python_basico/capitulo_38_el_metodo_init.html

class Usuario:
	def __init__(self, nombre, apellidos):
		self.nombre = nombre
		self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Enrique', 'Barros Fernández')

usuario002 = Usuario('Javier', 'Gomila Reyes')