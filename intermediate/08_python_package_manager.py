### Python Package Manager ###

# pip
# pip install pip
# pip --version

# beautiful para webscrapping  --> alguien lo men
# mencionó en el en el curso https://www.youtube.com/watch?v=TbcEqkabAWU
# en el time: 6 horas 45 min prox

import numpy   # pip install numpy

print(numpy.version.version)
# esta libreria es mas completa y permite mas operaciones y más rápida
numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip install pandas
import pandas   

# pip list
# pip uninstall pandas
# pip show numpy 

# pip install requests
import requests

# esta libreria es para hacer peticiones a api
url = "https://pokeapi.co/api/v2/pokemon?limit=151"
response = requests.get(url)
print(response)
print(response.status_code)
print(response.json())

# Arithmetics package
# un paquete es un conjunto de módulos
# el paquete es packages
# el módulo es arithmetics (dentro de packages)
from packages import arithmetics
print(arithmetics.sum_two_values(1,4))



