class Person:
    def __init__(self, name, age=0):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @age.setter
    def age(self, age):
        self.__age = age



beni = Person(27)
beni.age = 29
print(beni.age)


