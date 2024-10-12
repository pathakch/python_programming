from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound():
        pass # no implementation in base class bcz this is an abstract method

    def breathe(self):
        print("Breathing.......")

# concrete class dog inhereting from Animal
class Dog(Animal):
    
    def sound(self):
        print("Barking.. Woof... Woof.... ")

# concrete class Cat inhereting from Animal
class Cat(Animal):
    def sound(self):
        print("Meowwing.... Meoww.. Meoww...")

dog = Dog()
cat = Cat()
'''
Below we can see that when we call dog class sound method it works as per it's impementation
when we call cat class sound method it works as per it's implementation'''

dog.sound()
cat.sound()
cat.breathe()
dog.breathe() 
