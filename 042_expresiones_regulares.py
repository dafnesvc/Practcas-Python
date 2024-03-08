#https://www.programacionfacil.org/cursos/python_basico/capitulo_47_expresiones_regulares_search_python.html
import re

texto = "Bienvenidos a Programación fácil"
busqueda = re.search("i", texto)
print(busqueda)

texto = "Bienvenidos a Programación fácil"
busqueda = re.search("Bienvenidos", texto)
print(busqueda)