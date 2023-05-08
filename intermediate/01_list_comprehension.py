### List Comprehension ###

my_original_list = [35, 24, 62, 52, 30, 30, 17]

my_list = [i for i in my_original_list]
print(my_list)

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

# creando una lista en un rango dado
my_list = [i for i in range(8)]
print(my_list)

# definiendo un rango
my_range = range(8)

#creando una lista con el rango definido
print(list(my_range))


# creando una lista en un rango dado, operando sobre el i
my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i + 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(num):
    return num + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)


# fibonacci con list ??
# CLARO QUE YES!!!

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)

# for x in range(10):
#     print(fib(x))
my_list = [fib(i) for i in range(10)]
print(my_list)

