### Functions

def my_function ():
    print("Esto es una función")

my_function()

def sum_two_values (first_value, secod_value):
    print(first_value + secod_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values(1.4, 5.2)
sum_two_values("5", "7")


def sum_two_values_with_return (first_value, secod_value):
    my_sum = (first_value + secod_value)
    return my_sum

my_result = sum_two_values_with_return(10, 5)

print(my_result)

# Probemos qué pasa cuando la función no tiene return
my_result = sum_two_values(10, 5)
print(my_result)   # imprime none ya que la función no retorna ningún valor

def print_name(name, surname):
    print(f"{name} {surname}")  # con f accede a los valores de las variable

print_name(surname = "Porras", name = "Virginia")
print_name("Virginia", "Porras")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")  

print_name_with_default("Virginia", "Porras", "mavir78")
print_name_with_default("Virginia", "Porras")

def print_texts(text):
    print(text)

print_texts("Hola")

# En caso de que se pasen múltiples textos 
# pero solo se esté declarando uno en la entrada de la
# función, entonces podemos agregar * 
# esto se interpreta como que de ese tipo de dato se
# pueden pasar todos los que desee sin necesidad de 
# declararlos individualmente

def print_texts(*text):
    print(text)   # Imprime ('Hola',)

print_texts("Hola")
print_texts("Hola", "Python", "mavir78")


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())  

print_upper_texts("Hola")
print_upper_texts("Hola", "Python", "mavir78")
