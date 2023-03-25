"""
**************************************************************************************************
================================== MRO: Method Resolution Order ================================== 
**************************************************************************************************
Method resolution order in Python is the order in which a python program resolves or searches for 
a class in case of multiple inheritance.

--->> It follows the depth-first search approach.: We will understand this 'depth-first search' method
with the help of below example.-->> 'Diamond Inheritance'
====================
Diamond Inheritance:
====================
 Diamond Inheritance refers to an ambiguity that arises when two classes -- B and C inherit from a superclass A
 and class D inherits from both class B and C. Now, suppose there is a method “demo” which is an overridden 
 method in one of Class B and Class C or both then the ambiguity arises which of the method “demo” Class D 
 should inherit.

"""
class A:
    def demo(self):
        print("This is class A")
class B(A):
    def demo(self):
        print("This is class B")
class C(A):
    def demo(self):
        print("This is class C")

#=================================================================================
# Scenario 1 : "class D_B_C(B,C)" -->>> first B and then C inside the paranthesis.
#=================================================================================
class D_B_C(B,C):
    def check(self):
        print("This is class D_B_C")

obj_D_B_C = D_B_C()
obj_D_B_C.demo()  
"""
Output :--> This is class B 

Explanation : While creating class 'D_B_C' we have given B first in order inside paranthesis
so the 'demo' function is coming from class 'B'
"""
#============================================================================
# Scenario 2 : 'class D_C_B(C,B)'-->>> first C and then B inside the paranthesis.
#============================================================================
class D_C_B(C,B):
    def check(self):
        print("This is class D_C_B")
obj_D_C_B = D_C_B()
obj_D_C_B.demo()  
"""
Output : -->> This is class C

Explanation : While creating class 'D_C_B' we have given C first in order inside paranthesis
so the 'demo' function is coming from class 'C'

"""   
#===========================================================================================
# Scenario 3 : 'class D_A_B_C(A,B,C)'-->> This is a violation of method 'depth-first-search'
#===========================================================================================
# Explanation : It is a clear violation, because D cannot start finding the method from A and eventually 
# go to B then C; Then definitely, we will get the error:
#=======================================================================================================

#================================
# Scenario 4 : 'D_B_C_A(B,C,A)'
#================================
class D_B_C_A(B,C,A):
    def check(self):
        print("This is class D_B_C_A")

obj_D_B_C_A = D_B_C_A()
obj_D_B_C_A.demo()
"""
Output : --> This is class B
"""
      

