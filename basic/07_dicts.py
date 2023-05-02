### Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}

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

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))
print(my_dict ["Nombre"])
print(my_dict.get("Lenguajes"))

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

#my_dict.fromkeys("Nombre", "Primer nombre")
my_dict.pop("Calle")
print(my_dict)

print("Moure" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())  # listado de cada item
print(my_dict.keys())
print(my_dict.values())

print(my_dict.fromkeys(("Nombre", 1)))
