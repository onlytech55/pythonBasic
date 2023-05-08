### Higher order functions ###
### funciones que llaman funciones 
### las funciones son 

def sum_one(value):
    return value + 1 

def sum_two_values_and_add_one(first_value, second_value):
    return sum_one(first_value + second_value)
    #return first_value + second_value + 1

print(sum_two_values_and_add_one(5,2))

def sum_two_values_and_add(first_value, second_value, f):
    return f(first_value + second_value)

print(sum_two_values_and_add(5,2, sum_one))


def sum_five(value):
    return value + 5


print(sum_two_values_and_add(5,2, sum_one))
print(sum_two_values_and_add(5,2, sum_five))


### Closures ###
#una función que define una función y retorna una función

def sum_ten():
    def add(value):
        return value + 10 
    return add
    
add_closure = sum_ten()
print(add_closure(5))


def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add
    
add_closure = sum_ten(1)
print(add_closure(5))

print(sum_ten(5)(1))
print((sum_ten(5))(1))


### Built-in Higher Order Functions ###
# funciones de orden superior incluidas en el lenguaje

numbers = [2, 5, 10, 21, 55]

# Map
# un iterable es una lista
# ¿qué vamos a hacer con la lista?

def multiply_two(number):
    return number * 2

print(map(multiply_two, numbers))  #imprime el objeto
print(list(map(multiply_two, numbers)))   # imprime los valores

# si en lugar de una función usamos lambdas ?? --->
print(list(map(lambda number: number * 3, numbers))) 


# Filter
# print(numbers)
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))

#filter using lambda
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
# reduce is include in another "function package" called functools

from functools import reduce

def sum_two_values(first_value, second_value):

    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))

