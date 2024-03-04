#21310176 Dafne Sarahi Villanueva Ceja.
#Concatena dos strings en una variable. Puedes comprobar el resultado con un print().#
string="Hello"+"Bye" #la varible string concatena datos tipo string mediante +
  print(string) #print imprime como resultado la conatenación que se encuentra en la variable string

#Concatena dos variables con strings en una tercera variable.
var1="Hola" #var1 almacena dato tipo string
var2=" Adiós" #var2 almacena dato tipo string 
var3=var1+var2 #var3 almacena la concatenacion entre las variables var1 y var2
  print(var3) #imprime el resultado de la concatenación guardada en var3 "Hola Adiós"

#Concatena una variable con string y un string directamente en un print().
v4="Bonjour" #se le asigna un valor tipo string a la variable v4
  print(v4+' '+"hi") #El print imprimirá la concatenación de v4 y "hi" por lo que dará "Bonjour hi"


#Escribe tu nombre y apellidos separados en variables. Después concatena estas variables dentro de otra.
#No te olvides de concatenar los espacios entre el nombre y cada apellido. Finalmente, imprime el resultado.
nom="Dafne" #variable nom almacena dato tipo string "Dafne"
apellido_p="Villanueva" #variable apellido_p almacena dato tipo string 
apellido_m="Ceja"  #variable apellido_m almacena dato tipo string 
nom_compl=nom+' '+apellido_p+ ' '+apellido_m #variable nom_compl almacena la concatenacion de las variables "nom" "Apellido_p" "apellido_m"
  print(nom_compl)#imprime la variable nom_compl con todos los datos concatenados "Dafne Villaneueva Ceja"

#Concatena dos números, no los sumes.
num1="2"#se almacena dato tipo string en variable num1 esto con el fin de que no se sumen los datos usando tipo int
num2="3"
print(num1+num2) #se hace la concatencaión de los datos de las variables num1 y num2
