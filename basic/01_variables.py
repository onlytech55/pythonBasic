#Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5 
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables
print(my_int_variable, my_string_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)


# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea
name, surname, alias, age = "Virginia", "Porras", "mavir", 44

# útil cuando una función retorna dos o mas variables, 
"""
Sin embargo no es nada aconsejable hacer esto....
"""
print("Mi nombre es: ", name, surname, "Edad: ", age, "Alias: ", alias)


# inputs, útiles si se ejecuta un script en consola y se solicita un parámetro
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# ¿Se puede forzar el tipo?
"""
Probando si se puede forzar el tipo de dato, se ve que no es posible
ya que se ha probado todas éstas maneras detalladas a continuación
y siempre cambia el tipo de dato
"""
address: str = "Mi dirección"
address = True
address = 5
address= 1.2
print(type(address))