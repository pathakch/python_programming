"""
classes = real world entity or object
attributes : - properties of the class , in Car class -windows,doors,enginetype etc
Methods :->> actions of the class.
"""
"""
# This is the better way of writing class
'__init__' is a constructor 
'window' will be passed at run time but in 'self.windows' `windows` is an attribute of class.
both can be of different name.
why 'self' is used ?? 
ANS:->> using self we can call any attributes of Car class.
Works of constructor : ---> As soon as we create an object of Car class , 
all the default attributes will be assigned accordingly 
for example 
car1 = Car(4,4,'petrol') in this case , constructor will assign 
windows=4
doors=4
enginetype=petrol
"""

class Car:
    #Constructor
    def __init__(self,window,door,enginetype):
        self.darwaja = window
        self.doors = door
        self.enginetype = 'petrol'

    def self_driving1(self):
        # why we are writing 'self' here bcz we can use all those attributes 
        # of Car class in this method also
        print("The car type is {} engine ".format(self.enginetype))
        # in the above print statement we are using attribute 'enginetype' which is assigned earlier

        """
           we can give another parameter also in method 'self_driving'
           let's say we want it to be 'electric' car in 'self_driving' case 
           we can use it like below
        """     
    def self_driving2(self,engine):
        print("The car type is {} engine ".format(engine))        

car1 = Car(4,4,'petrol')      
print("The number of windows of the Car is : ", car1.darwaja) 
"""
output :->>
The number of windows of the Car is :  4
"""

"""
while clalling class method 'self_driving1' no need to pass any parameter since we have not 
defined any additional parameters in this function , And 'self' is written in function argument
so this function will take the parameter from constructor 
""" 
car1.self_driving1()  
"""
Output :-->>
The car type is petrol engine
"""

"""
In class method 'self_driving2' one extra argument'engine' is defined other than self
that's why we need to pass that argument while calling the function that's why 'electric'
is passed as 'engine'.
"""
car1.self_driving2('electric') 
"""
Output :-->>
The car type is electric engine
"""
        