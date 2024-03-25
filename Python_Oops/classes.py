"""
classes    :->> Real world entity or object, It has two things 1. Attributes 2. Methods.
Attributes :->> properties of the class , in Car class -windows,doors,enginetype etc
Methods    :->> actions of the class.
"""
"""
Difference between Methods and Functions : 
--------------------------------------------
Method   : Method is any function which is written inside the class, We can not call it function We call it methods
Function : Function is any normal function
--------------------------------------------
Question : What is Constructor
Answer   : Constructor is a function (block of code) which is executed/called automatically when we initialize or instantiate an object of the class,
Things to remember about Constructor : 
1. We write such types of code inside constructor which do not need user permission to be executed like -- connecting to the internet, connecting to the database 
   Assume an application -- when a user opens that application in mobile/laptop it should directly connect to the internet so that user can work on it so here we write this connection code inside the constructor of the class of that application.
For example : 
creating a class to demonstrate it:
----------------------------
   class Greeting():
       def __init__(self):
          Print("Hi Namaste")
        
        def other_fn(self):
           pass
----------------------------
As soon as we instantiate/create an object of 'Greeting' class , its constructor will be executed and print 'Hi Namaste' 
like 
greeting_obj = Greeting() ('Hi Namaste' will be printed right below)
--------------------------------------------------------------------------------
Question : What is 'self' and the significance of it ??
Answer   : 'self' is the object of class we are working with currently 
            Meaning : lets create a class 'Atm'
            -------------------------------------------
            class Atm:
                    def __init__(self, bank, balance)
                        self.balance = balance
                        self.bank = bank
                    def other_fn_1(self):
                        pass
                    def other_fn_2():
                        pass
            --------------------------------------------
let's create an object called sbi of 'Atm' class. 
sbi = Atm()
This will help to understand below functionality of the class.
--------------------------------------------------------------
when we print(id(sbi)) and print(id(self))

print(id(sbi))  = '1234'
print(id(self)) = '1234'
these both are on same address it means the current object of a class is 'self'

In above class 'other_fn_2' is created without 'self', so when we create an object of 'Atm' class and try to access 'other_fn_2' we will get an error -> 'other_fn_2' takes 0 arguments but 1 is passed
why we got this error while we have not passed any argument while calling 'other_fn_2' because 
----------- Significance of 'self'--------------
There is a rule in class that nothing can be accessed of a class without any object of the class, not even one function of the class
can call other function of the same class inside the class.
So, to access anything of a class 'self' is required.
One method of a class can call any method of the class with the help of 'self' only 
OR
One method of the class can access any attribute of class with the help of 'self' only. 
-------------------------------------------

"""
"""
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
        