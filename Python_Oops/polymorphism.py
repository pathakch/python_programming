"""
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
inside class 'VIP' one function is created with two arguments 'x' and 'y'
this function will work in all three scenarios defined in 'if/else' condition
whenever we need to overlaod a function we need to pass this 'None' this is the correct way 
of method overlaoding.
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
*******************************************************************************************
Explanation : 
we can see that function 'vsp' is working in all three scenarios 
and returns output based on the parameters passed
*******************************************************************************************
"""

