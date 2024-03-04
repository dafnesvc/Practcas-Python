#https://www.programacionfacil.org/cursos/python_basico/capitulo_32_bucle_for_diccionarios_python.html

#Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

for x in teclado1:
	print(x, '=', teclado1[x] + '.')