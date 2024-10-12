class Animal:
    def __init__(self, colour, size, legs):
        self.colour = colour
        self._size = size # private attribute
        self.__legs = legs # protected attribute

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

    # This method can be created but when we try to run this method with object of 
    # Dog class it will throw an error because it tries to access protected attribute of 
    # it's parent class
    def access_protected(self):
        print(f"This is protected attribute of Animal class : {self.__legs}")

    def sound(self):
        print(f"Sound of this animal is barking : {self.sound}")

dog1 = Dog('Woof','black',5,4)

# below code will give output as 5 means it can access private attribute of class although it's not 
#recommended
print(dog1._size) # output = 5

dog1.animal_size()
dog1.public_method()

'''below code will give error since it's a protected attribute of class and can not be accessed 
outside of class'''
print(dog1.__legs) #output : 'Dog' object has no attribute '__legs'. Did you mean: '__le__'?

''''
below method will throw an error since it can not access protected attribute `__legs` of 
class Animal
'''
dog1.access_protected() #output: 'Dog' object has no attribute '_Dog__legs'

#creating object of Animal class to check whether we can access protected attribute of class
#from outside of class or not. 
animal_obj = Animal('red', 10, 6) 

#we can not access it , will throw an error.
#trying to access protected attribute of class from it's own object, 
print(animal_obj.__legs) #output: AttributeError: 'Animal' object has no attribute '__legs'. Did you mean: '__le__'?

'''
But there is a way to access the protected attribute of class , but it's not recommended'''
print(animal_obj._Animal__legs) # output : 6

#************************* Summary ***********************
'''
1. Protected attribute of methods can not be accessed outsideof class, not even in it's 
child class
2. Private attribute and method can be accessed in it's child class and by object of the child class
'''
