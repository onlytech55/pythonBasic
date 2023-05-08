### Lambdas ###
# funciones anónimas, functions without name!

sum_two_values = lambda first_value, second_value : first_value + second_value 
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

# usando una lambda dentro de una function
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4))


