### Operadores

### Operadores Aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)   # módulo
print(10 // 3)  # floor division --> divión con resultado aproximado
print(2 ** 3)   # exponencial
print(2 ** 3 + 3 - 7 / 1 // 4 )   # combinados


# Con cadenas de texto
print("Hola "+ "Python "+ " Aprendiendo")

# para tipos distintos hay que castear
print("Hola "+ str(5))

# pero no es igual que para multiplicar, que si está permitido
print("Hola " * 5)


### Operadores Comparativos ###
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print("########")
# Con string
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" == "Hola")
print("Hola" != "Python")

print("*********************")


### Operadores Lógicos ###
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4) )
print(not(3 > 4))

