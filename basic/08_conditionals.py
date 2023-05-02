### Conditionals

my_condition = False

if my_condition : 
    print("Se ejecuta la condición del if")

my_condition = 5 * 2

if my_condition  == 10 : 
    print("Se ejecuta la condición del segundo if")


if my_condition  > 10 : 
    print("Es mayor que 10")
else :
    print("Es menor o igual a 10")

my_condition = 5 * 3

# nota: el elif es considerado como si estuviese dentro del if donde inicia el ciclo condicional    
if my_condition  > 10 and my_condition < 20: 
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else :
    print("Es menor o igual a 10 o mayor o igual que 20")

print ("La ejecución continúa")



my_string = "Mi cadena de texto"

if my_string:
    print("Mi cadena de texto no es vacía")

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

    