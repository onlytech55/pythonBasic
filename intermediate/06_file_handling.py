###  File Handling  ###

import os

# .txt file
#ruta = "C:\python\intermediate\my_file.txt"
ruta = "intermediate\my_file.txt"
# r+ :Leer y escribir
# w+ : Leer y escribir, lo sobreescribe 
# probando el encoding porque no lee bien "años"
# txt_file = open(ruta, "r+", encoding="latin1")
txt_file = open(ruta, "r+")
# txt_file = open(ruta, "w+")


# print(txt_file.read())
# print(txt_file.read(20))  # Lee los primeros 20 caracteres
# print(txt_file.readline())
# print(txt_file.readline())
# print(txt_file.readlines())

# Leyendo una a una las líneas del file
for line in txt_file.readlines():
    print(line)
    # print(line.encode('utf-8').decode())

# Escribiendo en el file
# txt_file.write("\nAunque también me gustaría aprender Node.js")
# txt_file.close()

# creando el archivo desde acá:
# removemos el archivo ya existente
# os.remove(ruta)
# En caso de remover el fichero, 
# crearlo con las líneas 'originales'
# txt_file.write("\nNombre: Maria")
# txt_file.write("\nApellido: Porras")
# txt_file.write("\n44 Años")
# txt_file.write("\nLenguajes de programación: Php, Python")
# txt_file.write("\nAunque también me gustaría aprender Node.js")
# txt_file.close()

# una vez cerrado el file, se abre con

# with open(ruta, "a") as my_other_file:
    # my_other_file.write("\nY VB.Net")

#  .json file

import json
ruta_json = "intermediate\my_file.json"

json_file = open(ruta_json, "w+")

json_test = {
    "name" : "Virginia",
    "surname" : "Porras",
    "age" : 44,
    "language" : ["Python", "Php", "Java"], 
    "website" : "none", 
}

# forma correcta de escribirlo
json.dump(json_test, json_file, indent=2)

json_file.close()

# Leyendo una a una las líneas del file

with open(ruta_json) as my_json_file:
    for line in my_json_file.readlines():
        print(line)

json_dict = json.load(open(ruta_json))

print(json_dict)
print(type(json_dict))

# Dado que es un diccionario, obtener un campo en específico
print(json_dict["name"])


# .csv file
import csv 

csv_file = open("intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file, delimiter=",")
cabecera = ["name", "surname", "age", "language"]
csv_writer.writerow(cabecera)
data = ["Virginia", "Porras", 44, "Python"]
csv_writer.writerow(data)

csv_file.close()


# para leerlo
ruta_csv = "intermediate/my_file.csv"
with open(ruta_csv) as my_csv_file:
    for line in my_csv_file.readlines():
        print(line)




#.xlsx file
# import xlrd  # Debe instalarse el módulo

# .xml file
import xml