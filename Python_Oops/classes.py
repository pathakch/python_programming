"""
classes    :->> Real world entity or object, It has two things 1. Attributes 2. Methods.
Attributes :->> properties of the class , in Car class -windows,doors,enginetype etc
Methods    :->> actions of the class.
"""
"""
------------------------------------------------------------------------------------------
Standards For Naming convention in Class.
1. Class name should be in PascalCase or UpperCamelCase or StudlyCase(Example : BookClass)
2. Variable name or Methods name should be in snake_case.(example : book_name)
------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
Instance variable and Class variable or Static variable : 
---------------------------------------------------------
1. Instance variable : variable whose values will be different for each new object created of that class , 
For Example : In ATM class PIN and BALANCE should be isntance variable (pin and balance will be different for each customer coming to the ATM)
Instance variable are always defined inside the constructor.
2. Class Variable/ Static Variable : Variables Whose values will be same for every object of that class
For example : in BANK class IFSC code is class variable or Static variable, in COllege class degree should be class variable or static variable.
***********************************************************
Accessing of Instance variable and Class or Static variable
***********************************************************
We can understand these from Atm class

To access instance variables-->> 'self.variable_name'
To access Static or Class variable--->> 'ClassName.variable_name'

------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
Difference between reference variable and class object : 
--------------------------------------------------------
TO understand this let's say Car is a class
when we write this -->> Audi = Car() (Audi is a reference variable and Car() is an object here.)
People generally say that Audi is an object of Car class which is wrong.
-------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------
Difference between Methods and Functions : 
--------------------------------------------
Method   : Method is any function which is written inside the class, We can not call it function We call it methods and its accessed by only it's object 
not by object of any other class.
Function : Function is any normal function which is not a part of any class (means not written inside any class), and accessed by any object.
We can understand it with below example : --

creating a list L
L= [1,2,3,4]
print(f"original list is : {L} and Length of Original list : {len(L)}")
# adding one extra element in list 
L.append(5)
print(f"List after appending 5 : {L} and its length is : {len(L)}")

--- In above example we can see their are two functions 1. len(list) and other is list.append(5)
but, if these two are functions then why we are calling them in different manner -- because here len() is 
a function and append() is a method of list class(method written inside list class) 
but len() is a general functional its not a method of list class (len function can be used by string too) . 
And we know whenever we call method of any class we call it this way -- object_of_class.method_name()

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
Toh jab bhi hum kisi function ko call karte hai toh usko ek by default input dete hai our wo input hota hai us 
unction ko call karne wala object our us time par wo object hi self hota hai isliye self required har function ko call
karne k liye.
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

#------------------------
#----------------========== Pass by Reference==========-------------------
"""
Object of a class behaves like normal list,str,dictionary or any other datatype
We can check this with below example -- where we will pass an object of a class as input parameter
while calling a function and thi object will behave like normal input parameter 
like other datatype of python 
"""
# Creating a class
class Customer():
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# creating a normal function
def greet(customer):
    if customer.gender.upper() == 'MALE':
        print(f"\nHello {customer.name} sir !")
    elif customer.gender.upper() == 'FEMALE':
        print(f"\nHello {customer.name} ma'am !")

#creating an object of Customer class.
cust = Customer("Aarti","female")

#passing an object of a class as input parameter for a function.
greet(cust)
# Output : -->> Hello Aarti ma'am !


"""-----------------===================================-------------------------------
Even we can create an object of a class inside any other 
function and can return that object by that function
check below :-->
"""
class Customer():
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

def greet(customer):
    #printing name of first customer.
    print(f"\nCustomer name is {customer.name}\n")

    #creating an oject of Customer class inside this function.
    cust2 = Customer('Chandan','male')
    return cust2

#creating an object of Customer class.
cust = Customer("Aarti","female")
#passing an object of a class as input parameter for a function.
customer_2 = greet(cust)
print(f"This is the name of second customer : {customer_2.name}")
'''
# Output : 
Customer name is Aarti
This is the name of second customer : Chandan
'''
'''
---------------------------
Class Objects are mutable :
--------------------------- 
Class object are mutable, meaning we can change an attributes or data of a class object on the smae address, 
and chaning anything's value on the same address proves mutability of that thing.
To check this we can print id of the object before and after changing the data of that object.Id o that object should be same in both cases.
Check below-->>
'''
class Customer():
    # creating a constructor of class.
    def __init__(self,name):
        self.name = name

def greet(customer):
    print(f"Original Id of the object printing inside class is : {id(customer)}")
    # Changing the attribute of class -- means changing the name of customer
    customer.name = 'Chandan'
    print(f"Id of object after changing the attribute of object inside class is: {id(customer)}")

#creating an object of Customer class.
cust = Customer("Aarti")
print(f"Original id of object before changing the attribute:{id(cust)}")
#calling function passing object as input parameter.
greet(cust)
#printing id of object after changing attribute
print(f"Id of object :{id(cust)}")
"""
Output :--> 
Original id of object before changing the attribute:878442800016
Original Id of the object printing inside class is : 878442800016
Id of object after changing the attribute of object inside class is: 878442800016
Id of object :878442800016
"""