"""
************************************************ Polymorphism ***********************************
************************************************              ***********************************   
Polymorphism means different form of same thing (method/function) we can understand it 
with the help of below exampple:
********************************
print(4+5):
Output : 9
********************************
print('4'+'5')
Output : 45
********************************
Thus this 'print' function is working on polymorphism concept (an example of polymorphism)
Form 1: when we pass integer 4 and 5 in 'print' function it gives output as 9 (sum of integer)
Form 2: When we pass strings '4' and '5' in 'print' function it gives '45' (concatenation of two strings)
********************************
These are the main concepts of polymorphism :-->>
1. Method Overloading : A function can be called with different number of arguments
2. Method Overriding : Multiple functions with same name and same number of parameters

"""
"""
*************************************** Method Overloading****************************** :
Method overloading is a means by which you can call the same method in different ways, 
i.e. with different parameters based on the number of arguments or their different datatypes

There are multiple methods of implementing 'Method overloading' in python
============================================================
Method 1 : using 'None' in function argument:-->>> but, this is not the most efficient way of 
implementing 'Method Overloading' in python.

inside class 'VIP' one function is created with two arguments 'x' and 'y'
this function will work in all three scenarios defined in 'if/else' condition
Here 'None' is default input means if we do not pass any parameters while calling this function
'x' and 'y' will take 'None' as input.
"""
class VIP:
    def vsp(self,x=None,y=None):
        if x == None and y == None:
            print("scenario of polymorphism : in this condition no argument is passed")
        elif x != None and y == None:
            print('square of number is : ',(x*x))  
        elif x != None and y != None:
            print("Addition of x and y is :",(x+y))

# calling the function 'vsp' without any parameters
obj1 = VIP()
obj1.vsp()
"""
Output :-->>
scenario of polymorphism : in this condition no argument is passed
"""
# calling the function 'vsp' with one parameter 'x'
obj2 = VIP()
obj2.vsp(5)
"""
Output :-->>
square of number is :  25
"""
# calling the function 'vsp' with two parameters 'x' and 'y'
obj3 = VIP()
obj3.vsp(4,5)
"""
Output :-->
Addition of x and y is : 9
"""
"""
****************************************************************
Explanation : 
we can see that function 'vsp' is working in all three scenarios 
1.scenario: if we do not pass any argument 
2.scenario: if we pass one argument
3.scenario: when we pass two arguments
it returns output based on the parameters passed
****************************************************************
"""
#=============================================================
# Method 2. Using '*args' in arguments while defining the function:-->> Not most efficient method
class Addition:
    def add(self,datatype,*args):

        if datatype == 'int':
            answer = 0
        elif datatype == 'str':
            answer = ''
        for i in (args):
            answer = answer+i
        print("sum is : ",answer)

# Creating an object of 'VIP' class.
obj4 = Addition()
# calling this function for integer input
obj4.add('int',2,3,4)
"""
Output :-->
sum is :  9
"""   

# Calling function 'add' for string inputs
obj4.add('str','Hello',' ','World','...!!')
"""
Output :-->>
sum is :  Hello World...!!
"""
#=================================================================
"""
********************************* Most efficient way of method Overloading in python ********************

The most efficient way to overload a method in python is by applying 
multiple dispatch decorator
"""  
#====================================
from multipledispatch import dispatch
#====================================
class Efficient_Add:
    @dispatch(int,int)
    def add(self,a,b):
        print("sum of two integers {},{} is : {}".format(a,b,(a+b)))

    @dispatch(int,int,int)
    def add(self,a,b,c):
        print("sum of three integers {},{},{} is : {}".format(a,b,c,a+b+c))   

    @dispatch(str,str)
    def add(self,a,b):
        print("concatenation of two strings {},{} is : {}".format(a,b,a+b))

# Creating an object of 'Efficient_Add' class
obj5 = Efficient_Add()

# Calling function 'add' with two integer inputs
obj5.add(2,3)     

# Calling function 'add' with three integer inputs
obj5.add(2,3,4)

# Calling function 'add' with two string inputs
obj5.add("Hello","World")



