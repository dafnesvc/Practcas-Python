#https://www.programacionfacil.org/cursos/python_basico/capitulo_48_expresiones_regulares_findall_python.html
import re

print("\nUsando findall()")
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.findall("e", texto)
print(busqueda, "\n")
