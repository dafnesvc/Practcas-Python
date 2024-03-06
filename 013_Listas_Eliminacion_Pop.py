#Dafne Villanueva 21310176
#Elimina de la siguiente lista los elementos 'azul' y 'blanco'. Solo puedes eliminarlos utilizando el método pop(). Además,
#tendrás que guardar esos dos colores en una nueva lista.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#se crea la variable colores con lista 
almacena_valor = [colores.pop(1),colores.pop(-2)] # se crea una nueva variable que guarda una lista con los colores que se eliminaran por el metodo .pop(lugar del dato)
print('El color eliminado y almacenado es:',almacena_valor)#imprime la nueva lista con los valores eliminados
