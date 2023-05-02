### Loops

# While

my_condition = 0

while my_condition < 10 : 
    print(my_condition)
    my_condition += 2

# if my_condition == 10:
#     print("Mi condición es igual a 10")
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")



while my_condition < 20 : 
    my_condition += 1
    if my_condition == 15:
        print("Detiene la ejecución")
        break 
    
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17 ]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)


my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)


my_dict = {
    "Nombre":"Brais", 
    "Apellido":"Moure", 
    "Edad":35,
    "Lenguajes" : {
        "Python",
        "Swift",
        "Kotlin"
    },
    1:1.77
}

for element in my_dict:
    print(element)


# Para obtener los valores del dictionario
for element in list(my_dict.values()):
    print(element)
else:
    print("El bucle para el diccionario ha finalizado")

# Interrumpiendo el bucle

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
 
else:
    print("Fin del bucle")


for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
 
else:
    print("Fin del bucle continua")