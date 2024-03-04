#https://www.programacionfacil.org/cursos/python_basico/capitulo_27_bucle_while_python_1.html
#Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.
print('\nEjercicio 1.')
x = 0 

while x < 15:
    print("X =", x)
    x += 5  

#Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
print('\nEjercicio 2.')
x = 0 

while x > -100:
    print("X =", x)
    x -= 20

'''Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta 
frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'''
print('\nEjercicio 3.')
x = 10

while x >= 0:
    print(f'El valor del bucle es {x}')
    x -= 1 
