### Error Types ###

# SyntaxError

# print "¡Hola comunidad!" # Descomentar para error
print ("¡Hola comunidad!") 

# NameError
# print(name)   #NameError: name 'name' is not defined
name = "Armando Locuaz"   # Comentar para error
print(name)

# IndexError
my_list = ["Ana", "Camila", "Federica", "Justina", "Javiera"]
# print(my_list[8])   #  IndexError: list index out of range
print(my_list[4])

# ModuleNotFoundError
# import maths   # ModuleNotFoundError: No module named 'maths'

import math

# AttributeError
# print(math.PI)  # AttributeError: module 'math' has no attribute 'PI'
print(math.pi)

# KeyError
my_dict = {"Nombre":"Maria", "Apellido":"Porras", "Edad":44, 1:"Python"}
#  print(my_dict["Apell"])  #  KeyError: 'Apell'
print(my_dict["Apellido"]) 

# TypeError
# print(my_list["Nombre"])   # TypeError: list indices must be integers or slices, not str
print(my_list[2])

# ImportError
# from math import PI  # ImportError: cannot import name 'PI' from 'math' (unknown location)     
from math import pi 
print(pi)

# ValueError
# my_int = int("10 Años")   # ValueError: invalid literal for int() with base 10: '10 Años'
my_int = int("10") 
print(type(my_int))

# ZeroDivisionError
# print( 1 / 0)   # ZeroDivisionError: division by zero
print(8 / 5)


