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
Answer   : Constructor is a function (block of code) which is executed/called automatically 
when we initialize or instantiate an object of the class,
Things to remember about Constructor : 
1. We write such types of code inside constructor which do not need user permission to be executed 
like -- connecting to the internet, connecting to the database 
   Assume an application -- when a user opens that application in mobile/laptop it should directly connect to the internet 
   so that user can work on it so here we write this connection code inside the constructor of the class of that application.
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
                    def other_fn_2(): (This is wrong -- created for understanding it's explained below)
                        pass
            --------------------------------------------
let's create an object called sbi of 'Atm' class. 
sbi = Atm()
This will help to understand below functionality of the class.
--------------------------------------------------------------
when we print(id(sbi)) and print(id(self))

print(id(sbi))  = '1234'
print(id(self)) = '1234'
These both are on same address it means the current object of a class is 'self'(matlab sbi hi self hai).

Next : -->> If we create another object 'hdfc' of class 'Atm' and we print(id(hdfc)) and print(id(self)), these both will be same
print(id(hdfc)) = '5678'
print(id(Atm))  = '5678'
Here both are same again  meaning the current object of class is self(matlab hdfc hi self hai).

but if we print(id(sbi)) this will be '1234' Now one question arise here then what is the self ??
because while working with sbi , address of self was '1234' and while working with 'hdfc' address of self is '5678' then what is self
Answer is very simple : while working with sbi , sbi was self and while working with hdfc , hdfc is self.
(So, jis object k sath hum kaam kar rhe hai currently wahi self hai.) 
 
----------- Significance of 'self'--------------
There is a rule in class that nothing can be accessed of a class without any object of the class, not even one function of the class
can call other function of the same class inside the class.
So, to access anything of a class 'self' is required.
One method of a class can call any method of the class with the help of 'self' only 
OR
One method of the class can access any attribute of class with the help of 'self' only. 
-------------------------------------------
Question : why self is required in each method created inside the class. ??
Answer   : To understand this we have created one function 'other_fn_2' without 'self' in 'Atm' class.
In above class 'other_fn_2' is created without 'self', so when we create an object of 'Atm' class and try to access 'other_fn_2' 
we will get an error -> 'other_fn_2' takes 0 positional arguments but 1 is given.
why we got this error while we have not passed any argument while calling 'other_fn_2' 
(we generally call any method of function like -- >> object_name.method name here it will be sbi.other_fn_2() this will throw an error 
error -->> 'other_fn_2' takes 0 positional arguments but 1 is given.)

Explanation : when we call any method of a class like this object_name.method_name() (object_name dot method_name) 
one argument input (the object itself) is passed as default (in this case sbi was passed in other_fn_2 and sbi hi self hai) and that's why
we got above error 'other_fn_2' takes 0 positional arguments but 1 is given.' even though we have not passed any argument while calling 
'other_fn_2'.(sbi was passed by default means self was by default)-- so self or say the object is calling other_fn_2 here.
Meaning inside class we can call any method or any data/attribute of class with the help of object only and object hi self hai so ultimatelly 
eveything will be accessed by self only. and thats why object or say sbi or say 'self' was passed by default while calling method other_fn_2.m

"""
"""
"""

class Car:
    #Constructor
    def __init__(self,window,door,enginetype):
        self.darwaja = window
        self.doors = door
        self.enginetype = enginetype

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
