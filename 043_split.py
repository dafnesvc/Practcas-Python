import re


print("\nsplit:")
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto)
print(busqueda)

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split("es", texto)
print(busqueda)

# maxspli
print("\nmaxsplit:")
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto, 4)
print(busqueda)

# metodo sub()
print("\nMetodo sub:")
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto)
print(busqueda)

#Limitar los resultados de sub con count
print("\nLimitar los resultados de sub con count")
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto, 4)
print(busqueda)