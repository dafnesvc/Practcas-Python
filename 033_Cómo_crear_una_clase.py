#https://www.programacionfacil.org/cursos/python_basico/capitulo_37_clases_y_objetos_python.html

class Usuario:
	nombre = ''
	apellidos = ''

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario()

usuario001.nombre = 'Enrique'
usuario001.apellidos = 'Barros Fernández'

usuario001.imprime_datos()