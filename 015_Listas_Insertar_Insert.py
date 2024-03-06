#Dafne Villanueva 21310176
#Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert(). Tendrás que posicionar 'magenta' en la posición 
#siguiente a la de 'lila' y 'turquesa' en la penúltima posición. Deberás hacer esto utilizando posiciones de lista negativas.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] # A la variable "colores" se le asigna una lista utilizando la "," con datos tipo string
colores.insert(-4,'magenta')#El método insert() funciona con dos parámetros, primero el número de posición donde quieres posicionar el elemento y después, el elemento a añadir
colores.insert(-1,'turquesa')
  print(colores)#El print imprimirá una nueva lista con los nuevos valores agregados "magenta y turquesa"
