### Exception handling

numberOne = 5
numberTwo = 1
numberTwo = "1"

#try except 

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")


#try except else 
# else y finally son opcionales en la estructura
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:   # opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # opcional
    # Se ejecuta siempre haya ocurrido o no un error
    print("La ejecución continúa")

# con el type error

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")


# Capturando la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except ValueError as e:
    print(e)

except Exception as errorcillo :
    print(errorcillo)
