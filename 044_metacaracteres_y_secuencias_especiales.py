#https://www.programacionfacil.org/cursos/python_basico/capitulo_50_secuencias_especiales_metacaracteres_sets_python.html
import re

#Punto (.) - Coincide con cualquier carácter excepto nueva línea:
pattern = re.compile(r"gr.y")
result = pattern.search("grey")
if result:
    print("Coincide")

#Asterisco (*) - Coincide con cero o más repeticiones del carácter anterior:
pattern = re.compile(r"ab*c")
result = pattern.match("ac")
if result:
    print("Coincide")

#Signo de más (+) - Coincide con una o más repeticiones del carácter anterior:
pattern = re.compile(r"ab+c")
result = pattern.match("abc")
if result:
    print("Coincide")

#Interrogación (?) - Coincide con cero o una repetición del carácter anterior:
pattern = re.compile(r"ab?c")
result = pattern.match("ac")
if result:
    print("Coincide")

#Corchetes [] - Coincide con cualquier carácter dentro de los corchetes:
pattern = re.compile(r"[aeiou]")
result = pattern.search("apple")
if result:
    print("Coincide")


