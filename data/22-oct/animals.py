class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__} - {self.name}'


    def talk(self):
        raise NotImplementedError

class Dog(Animal):

    def talk(self):
        print('Woof')


class GermanSheperd(Dog):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def talk(self):
        print('Ich sprache Deutsch')


class Cat(Animal):

    def talk(self):
        print('Miao')

    def move(self):
        print("I'm jumping")

class Bizarre(GermanSheperd, Cat):
    pass

