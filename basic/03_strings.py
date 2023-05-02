### Strings

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

### Formateo de strings ###

name = "Maria"
surname = "Porras"
age = 44

print("Mi nombre es: {} {} y mi edad es {} ". format(name, surname, age ) )

# Para escribir definiendo el tipo de formato, esto a su vez hace una validación: no permite
# escribir varibles que no cuplan con el tipo de formato especificado
# por ejemplo, si estoy especificando que age es un entero (%d) y defino age = 'Hola'
# dará error
print("Mi nombre es: %s %s y mi edad es %d " %(name, surname, age ) )  
print("Mi nombre es: %s %s y mi edad es %d " %(surname, name, age ) )  


# otra manera de escribir:
print(f"Mi nombre es: {name} {surname} y mi edad es {age} ")  

# Desempaquetado de caracteres
language = "Python"
a,b,c,d,e,f = language

print(a)
print(b)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
# print(language.count())  este no funciona, necesita un parámetro para contar repeticiones de letra en una cadena
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("py"))






