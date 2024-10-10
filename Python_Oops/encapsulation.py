class Animal:
    def __init__(self, colour, size, legs):
        self.colour = colour
        self._size = size
        self.__legs = legs

    def get_size(self):
        print(f"This animal has {self.__legs} legs")

    def set_legs(self, legs_value):
        print(f"Setting legs of Animal as {legs_value}")
        self.__legs = legs_value
        print(f"This Animal legs has been changed to {self.__legs}")
    


class Dog(Animal):
    def __init__(self, sound, colour, size, legs):
        super().__init__(colour, size, legs)
        self.sound = sound

    #accessing protected attribute of Animal class withing it's sub class
    def animal_size(self):
        print(f"Size of this animal is : {self._size}")

    def access_private(self):
        print(f"This is protected attribute of Animal class : {self.__legs}")

    def sound(self):
        print(f"Sound of this animal is barking : {self.sound}")

dog1 = Dog('Woof','black',5,4)
# print(dog1._size)
# print(dog1.__legs)
# dog1.animal_size()
# dog1.public_method()
# dog1.access_private()

#creating object of Animal class.
animal_obj = Animal('red', 10, 6)

# print(animal_obj._Animal__legs)



