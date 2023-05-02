### Modules

# en este caso el nombre del fichero no permite que se acceda a él
# import 10_functions no pueden comenzar por número

import module

module.sum(5, 3, 1)
module.printValue("Hola Python!")

# para importar una función concreta de un fichero

# from my_functions import sum_two_values


from module import sum, printValue

sum(5, 3, 1)
printValue("Hola Python!")


import math

print(math.pi)
print(math.pow(2, 8))


# empleado alias para propiedades específicas de un módulo
from math import pi as PI_VALUE

print(PI_VALUE)