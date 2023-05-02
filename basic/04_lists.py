### Listas

my_lists = list()
my_other_list = []

print(len(my_lists))

my_lists = [35, 24, 62, 52, 30, 30, 17]

print(my_lists)
print(len(my_lists))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_lists))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
#print(my_other_list[4])   IndexError: list index out of range
#print(my_other_list[-5])  IndexError: list index out of range

print(my_other_list.count("Brais"))
print(my_lists.count(30))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_lists + my_other_list)
# print(my_lists - my_other_list)  TypeError: unsupported operand type(s) for -: 'list' and 'list'

my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_lists.remove(30)
print(my_lists)

print(my_lists.pop())
print(my_lists)

my_pop_element = my_lists.pop(2)
print(my_pop_element)
print(my_lists)

del my_lists[2]
print(my_lists)

my_new_list = my_lists.copy()
print(my_new_list)
my_new_list.reverse() #primero se debe ejecutar el reverse y luego imprimirlo
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])
print(my_new_list[1:3])





#si le cambio el tipo de dato a la lista, el lenguaje lo acepta,
#pues python no está fuertemente tipado
my_lists = "Hola Python"
print(my_lists)
print(type(my_lists))










