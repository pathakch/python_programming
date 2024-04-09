 
#***********************************  *****************************************
#=================================== Inheritance (Is-A relationship)==============================
"""
What are the things a child class can inherit from its parent class ???...
Answer :-- >> These are the three things whicha can be inherited from parent class by child class.
1. Data members.
2. Member functions or say Methods
3. Constructors
---------------------
NOTE : -->> private members cant be inherited by child class from parent class.
---------------------
"""
#******************************************************************************
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
    # like we can access any of the attributes 'windows' or 'doors' or 'enginetype' writting 
    # 'self.windows' or 'self.doors' or 'self.enginetype'.
    def driving(self,mode):
        print("This is a {} car".format(mode))

# creating a child class 'Audiq7' which is inheriting from parent class 'Car'
class Audiq7(Car):
    # since child class 'Audiq7' is inheriting from parent class 'Car' while creating its constructor
    # we need to pass all the attributes(windows,doors,enginetype) of parent class also along with its own 
    # attribute(horsepower)
    def __init__(self,windows,doors,enginetype,horsepower):
        """
        To access all the attributes of parent class we need 'super().' keyword. Using this keyword we can call any 
        data members or methods of Parent class inside the child class, it does not mean that we can call them outside of 
        child class meaning child_object.super().data_member -- this will not work.
        Thats why to call the constructor of parent class inside child class 'super().' is required we can see below.
        NOTE:-->> Here we can see that Parent constructor is being called inside child constructor so what will happen
        when we create an object of child class by doing this <audi1 = Audiq7(2,2,'audi type engine',200)>.
        First child class constructor will be invoked then this child class constructor will call parent class
        constructor since we have done this (super().__init__(windows,doors,enginetype)) and then control will go to 
        parent class constructor and set these three values windows = 2, doors = 2 and enginetype = audi type engine and then 
        control will come to child's constructor and set this one value horsepower = 200 -- This is how it works.
        For Example :  we can access all the data members of parent class and child class by child's class object.
        Like this 1. audi1.windows or audi1.enginetype or audi1.horsepower
        Matlab -- aadha initialization child constructor se krwa rhe hai and aadha initialization parent constructor se 
        karwa rhe hai using super(). keyword and calling parent constructor -- This is smart coding.
        """
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
car1.driving("self_driving")
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
Explanation :-->> Since 'car1' is an object of parent class that's why it has only those class attributes
(windows,doors and enginetype)and class methods(driving) which have been defined in parent class "Car" 
And 'audi1' is an object of child class "Audiq7" that's why it has child class attributes(horsepower) 
and methods(drift) as well as parent class attributes(windows,doors and enginetype) and methods(driving)
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
#############################################################################################################
class User:
    def login(self):
        print("login")

    def register(self):
        print("register")

"""
Student is inheriting from User it means , object of Student class can access everything of User class 
-- this is the meaning of inheritance on high level.
"""
class Student(User):
    def enroll(self):
        print("Enrolled")

    def review(self):
        print("Review")

stu1 = Student()

# Student is inheriting from User it means , object of Student class can access everything of User class 
stu1.login()
stu1.review()
stu1.enroll()
stu1.register()
"""
Output : 
login
Review
Enrolled
register
"""

