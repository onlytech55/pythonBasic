### Classes

# Una clase si se define con los nombre Camel Case
# en lugar del snake case que se usa en las variables

class MyEmptyPerson:
    pass   # Debe llevar esto si la clase es vacía

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname) :
        self.name = name
        self.surname = surname

my_person = Person("Virginia", "Porras")
print(my_person.name)

print(f"{my_person.name} {my_person.surname}")


class FullPerson:
    def __init__(self, name, surname, alias = "Sin alias") :
        self.full_name = f"{name} {surname} ({alias})"

    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = FullPerson("Virginia", "Porras")
print(my_person.full_name)

my_person.walk()

my_other_person = FullPerson("Antonio", "Pérez", "antoper")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

# Haciendo las propiedades privadas
# para no modificar los valores
class Persona:
    def __init__(self, name, surname, alias = "Sin alias") :
        self.full_name = f"{name} {surname} ({alias})"  # propiedad pública
        self.__name = name   # el nombre se hace privado y no se podrá modificar
        self.__surname = surname

    def get_name(self) :
        return self.__name

    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = Persona("Virginia", "Porras")
print(my_person.full_name)

print(my_person.get_name())
