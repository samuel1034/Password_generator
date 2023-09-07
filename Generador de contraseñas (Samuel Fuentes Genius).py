import random

letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numeros = [1,2,3,4,5,6,7,8,9,10]
simbolos = ["¡","!","@","#","$","%","&","/","(",")","=","*","+","¿","?","-","_","{","}"]


print (" Bienvenidos al generador de contraseñas");
numero_letras = int (input ("¿Cuantas letras?"))
numero_numeros = int (input("¿Cuantos numeros?"))
numero_simbolos = int (input("¿Cuantos simbolos?"))

lista = []

for letra in range (1, numero_letras + 1):
    valor = random.choice(letras)
    lista.append(valor)

for numero in range (1, numero_numeros + 1):
     valor = random.choice(numeros)
     lista.append(valor)

for simbolo in range (1, numero_simbolos  + 1):
     valor = random.choice(simbolos)
     lista.append(valor)

print (lista);
