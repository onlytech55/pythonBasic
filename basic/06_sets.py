### Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))   # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))    #  acá ya es set... si está lleno cambia?!

print(len(my_other_set))

my_other_set.add("MoureDev")
print(my_other_set)   # Un set no es una estructura ordenada

my_other_set.add("MoureDev")  # Un set no admite elementos repetidos
print(my_other_set)   

# Buscar elemento dentro de un set
print("Moure" in my_other_set)
print("Mouri" in my_other_set)

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set)   NameError: name 'my_other_set' is not defined

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)

print(type(my_list))
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)

print(my_new_set) 
print(my_set)
print(my_new_set.union(my_set).union({"Javascript", "C#"}))

print(my_new_set.difference(my_set))

print(my_new_set.issubset("Python"))



