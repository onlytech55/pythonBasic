### Regular expressions ###

# build, understand and tester regular expression on line::::
# https://regex101.com/


import re 

# re.match --> match busca solo al principio de la cadena
# re.search --> busca la coincidencia en la longitud total de la cadena

my_string = "Esta es la lección número 7: Lección sobre Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
span = match.span() 
# desempaquetamos los valores de incio y fin obtenido con match.span
start, end = match.span()
# imprimir la cadena encontrada
print(my_string[start:end])

# print(span)
# print(match.

match = re.match("Esta es la lección", my_other_string, re.I)
print(match)
# en caso de que no encuentre nada
# if match != None:  # ---> vale igual que if not(match == None):

if not(match == None):
    # desempaquetamos los valores de incio y fin obtenido con match.span
    start, end = match.span()
    # imprimir la cadena encontrada
    print(my_string[start:end])


match = re.match("Esta no es la lección", my_other_string)
print(match)
# en caso de que no encuentre nada
# if match != None:  # ---> vale igual que if not(match == None):

if match != None:
    span = match.span() 

    # desempaquetamos los valores de incio y fin obtenido con match.span
    start, end = match.span()
    # imprimir la cadena encontrada
    print(my_other_string[start:end])


# print(re.match(" Expresiones Regulares", my_string))

# search
search = re.search("Expresiones Regulares", my_string, re.I) 
print(search)
start,end = search.span()
print(my_string[start:end]) 

# find
# re.I ---> ignore case:: busca mayúsculas y minúsculas
findall = re.findall("lección", my_string, re.I)
print(findall)

# split
print(re.split(" ", my_string))
print(re.split(":", my_string))

# sub

print(re.sub("Expresiones", "expresiones", my_string))
print(re.sub("lección", "LECCIóN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# para cambiar todas las ocurrencias de lección
print(re.sub("lección|Lección", "LECCIóN", my_string))
# o lo que es lo mismo
print(re.sub("[l|L]ección", "LECCIóN", my_string))



# Patterns 
pattern = r'[lL]ección'
print(re.findall(pattern, my_string))

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))
# retorna ['7']


pattern = r'\D'
print(re.findall(pattern, my_string))   # retorna todas las letras

pattern  = r'[l].'
print(re.findall(pattern, my_string)) 

pattern  = r'[l].*'
print(re.findall(pattern, my_string)) 

# email validation regular 
def is_valid_email(email):
    # pattern = r'^[A-Za-z0-9+.-_]*[A-Za-z0-9]+@[A-Za-z0-9-]+\.[A-Z|a-z]+$'
    pattern = r'^[a-zA-Z0-9_.+_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    print(re.match(pattern, email))
    print(re.search(pattern, email))
    print(re.findall(pattern, email))

email = 'mavir78@gmail.com'
is_valid_email(email)

email = 'mavir78@gmail'
is_valid_email(email)

email = 'mavir78.com'
is_valid_email(email)

email = 'mavir78@gmail.com.mx'
is_valid_email(email)










