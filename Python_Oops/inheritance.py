
#*********************************** Inheritance *****************************************#
# Creating a class named 'Car' -->> Parent class
class Car:

    # creating constructor:
    def __init__(self,window,door,enginetype):
        self.windows = window
        self.doors = door
        self.enginetype = enginetype
    
    # creating a class method
    # Important to Note : ->> Here passing 'self' parameter(while creating this function) is mendatory 
    # otherwise ,error occurs
    # and 'self' will help to access all the attributes defined in constructor inside this function
    # like we can access any of the attributes 'windows' or 'doors' or 'enginetype'
    def driving(self,mode):
        print("This is a {} car".format(mode))

# creating a child class 'Audiq7' which is inheriting from parent class 'Car'
class Audiq7(Car):
    # since child class 'Audiq7' is inheriting from parent class 'Car' while creating its constructor
    # we need to pass all the attributes(windows,doors,enginetype) of parent class also along with its own 
    # attribute(horsepower)
    def __init__(self,windows,doors,enginetype,horsepower):

        # to access all the attributes of parent class we need to call the constructor of parent class 
        # inside this class with the help of 'super().__init__()'
        super().__init__(windows,doors,enginetype)
        
        # initializing child class's attribute(horsepower)
        self.horsepower = horsepower

    # creating child class's own method 
    def drift(self,action):
        print("This car is {} ".format(action))    

########################################################################################

# creating object of parent class 'Car'
car1 = Car(4,5,'petrol')
print("Car1 specifications are \nwindows:{}\ndoors:{}\nenginetype:{}".format
      (car1.windows,car1.doors,car1.enginetype))
"""
Output :-->>
Car1 specifications are
windows:4
doors:5
enginetype:petrol
"""

# calling parent class method 'driving'
#car1.driving("self_driving")
"""
Output :-->>
This is a self_driving car
"""
##########################################################################################

# creating child's class 'Audiq7' object
# we need to pass all the attributes of parent class also while creating child class object
audi1 = Audiq7(2,2,'audi type engine',200)
print("\nAudi car specification is \nwindows:{}\ndoors:{}\nenginetype:{}\nhorsepower:{}"
      .format(audi1.windows,audi1.doors,audi1.enginetype,audi1.horsepower))
"""
Output :-->>
Audi car specification is
windows:2
doors:2
enginetype:audi type engine
horsepower:200
"""
# calling child class's method 'drift'
audi1.drift("self_drifting")
"""
Output :-->>
This car is self_drifting
"""

# Since child class will inherit the methods of parent class
# calling parent class's method inside the child class
audi1.driving("not_self_driving")
"""
Output :-->>
This is a not_self_driving car
"""
############################################################################################
"""
Difference between parent class and child class attributes and method explanined below with output
Explanation :-->>
"""
print(dir(car1))
"""
Output :-->>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'doors', 'driving', 'enginetype', 'windows']
"""
print(dir(audi1))
"""
Output :-->>
 ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__gt__','__hash__', '__init__', '__init_subclass__', 
'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
 'doors', 'drift', 'driving', 'enginetype', 'horsepower', 'windows']
"""

