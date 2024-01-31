### Error Types ###

# SyntaxError
# print "¡Hola comunidad!" # Descomentar para Error
from math import pi
import math
#print "¡Hola comunidad!" # Error
print("¡Hola comunidad!")

# NameError
language = "Spanish" # Comentar para el Error
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[-1])
print(my_list[4])
#print(my_list[5]) #Descomentar para el Error

# ModuleNotFoundError
# import maths # Descomentar para Error

# AttributeError
# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Edu", "Apellido": "Maldonado", "Edad": 24, 1:"Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError
# print(my_list["0"]) # Descomentar para el Error
print(my_list[0])
print(my_list[False]) # False se traduce a un 0, desaconsejable 


# ValueError
# my_int = int("10 años") # Descomentar para Error
my_int = int("10") 
print(type(my_int))

# ZeroDivisionError
#print(4/0) #Descomentar para Error
print(4/2)