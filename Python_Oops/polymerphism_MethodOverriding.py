"""
====================================================================================================
******************************************* Method Overriding **************************************
====================================================================================================
Method Overriding in Python is an OOPs concept closely related to inheritance. 
When a child class method overrides(or, provides it's own implementation: means apply its own 
definition) the parent class method of the same name, parameters and return type, it is known 
as method overriding.

============================== Features & Advantages of method Overriding ===========================
1. Method Overriding is derived from the concept of object oriented programming
2. Method Overriding allows us to change the implementation of a function in the child class which is 
   defined in the parent class.
3. Method Overriding is a part of the inheritance mechanism
4. Method Overriding avoids duplication of code
5. Method Overriding also enhances the code adding some additional properties.

============================================== Prerequisites==========================================
1. Method overriding cannot be done within a class. So,we need to derive a child class from a parent class. 
   Hence Inheritance is mandatory.
2. The method must have the same name as in the parent class
3. The method must have the same number of parameters as in the parent class.

"""

# Creating parent class 'Shape'
class Shape:
    data1 = 'abc'

    # Method 1.
    def no_of_sides(self):
        print("\nI am parent class method 'no_of_sides' from parent class 'Shape'\n")
    # Method 2.
    def two_dimensional(self):
        print("I am a parent class method named 'two_dimensional' \n")  

class Square(Shape):
    data2 = 'xyz'

    # Method 1.
    def no_of_sides(self):
        print("I am child class method 'no_of_sides' I am overriding the parent class method'no_of_sides'\n")

    # Method 2.
    def color(self):
        print("I am a child class method 'color' , I provide colors to the objects\n")

#================================
# Creating parent class's object
parent_class_obj = Shape()

# Creating child class's object
child_class_obj = Square()
''''''
#============================
# calling parent class method 
#============================
# calling parent class method 'no_of_sides' from parent class object.
parent_class_obj.no_of_sides()
'''
Output :-->>
I am parent class method 'no_of_sides' from parent class 'Shape'
'''
parent_class_obj.two_dimensional()
'''
Output :-->
I am a parent class method named 'two_dimensional'
'''
# get parent class data from parent class object.
print("This is parent class data :",parent_class_obj.data1)
'''
Output :-->
This is parent class data : abc
'''
#============================
# calling child class methods 
#============================
# calling child class method 'no_of_sides' (which has been overriden) from child class method.
child_class_obj.no_of_sides()
'''
Output :-->>
I am child class method 'no_of_sides' I am overriding the parent class method'no_of_sides'

========== Explanation ============
We can see here that parent class method 'no_of_sides' has been overriden in child class 
means it's been modified inside the child class (in this case unction contains only print statement 
and that print statement has been changed means modified)
'''
# calling parent class method 'two_dimensional()' from child class object.
child_class_obj.two_dimensional()
'''
Output :-->>
I am a parent class method named 'two_dimensional'

========== Explanation ============
This child class object is accessing parent class's method 'two_dimensional'
'''
# calling child class method 'color()' from child class object.
child_class_obj.color()
'''
Output :-->>
I am a child class method 'color' , I provide colors to the objects
'''
# get parent class data from child class's object
print("This is parent class data which has been initialized in parent class\
 and also accessible in child class : ",child_class_obj.data1)
'''
Output :-->
This is parent class data which has been initialized in parent class 
and also accessible in child class :  abc
'''
# get child class data from child class object
print("This is child class data which has been initialized in child class : ",child_class_obj.data2)
'''
Output :-->
This is child class data which has been initialized in child class :  xyz
'''






