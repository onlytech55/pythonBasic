### Type hints ###

# En principio, python tiene variables dinámica
# la variable puede cambiar su tipo:
my_string_variable = "My string variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

# type hints indica que los tipos se pueden especificar con FastApi
my_typed_variable: str = "My typed string variable"
print(my_typed_variable)
print(type(my_typed_variable))

# pero no se puede obligar a que sea necesariamente del tipo indicado
my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))