""" 
************************************************************************************************
Ques: Can we write multiple constructors in python ?? 
ANs : We can not create multiple constructors(__init__ function) in python 
      because if we make multiple constructors then python will consider the 
      last constructor as final bcz last constructor will override all the previous 
      constructors.
      In other programming language like Java and Dot net we can create multiple constructors but, 
      not in python.
      we will see it with one example :-->>>> Check below
**************************************************************************************************      
"""
class Animal:

    #creating first constructor
    def __init__(self,name,species):
        self.name = name
        self.species = species

    #creating second constructor
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age

    #creating a method just like that,its not important to create it to understand above question    
    def make_sound(self,sound):
        return "The animal is {} and it makes sound {}".format(self.name,sound)       

# creating an object of Animal class:
# this object is created keeping first constructor in mind
# that's why only two attributes(name='dog' and species='mammalas') have been passed while making object

#dog = Animal("dog","mammalas") 
#print(dog) 

"""
Traceback (most recent call last):
  File "c:/Users/ckp43_000/python_programming/python_programming/Python_Oops/constructors.py", line 33, in <module>
    dog = Animal("dog","mammalas")
TypeError: __init__() missing 1 required positional argument: 'age'
"""
"""
Explanation:-->>>
when we execute this program(line number 35) , we get above error message which indicates 
that class 'Animal' is considering the second constructor and thats why it's asking for 
third argument/attribute which is 'age' which is defined in second constructor. It means second 
constructor is overriding the first constructor.
"""
# creating object of Animal class keeping second constructor in mind and passing three attributes 
# while making object
dog2 = Animal("dog","mammalas",20)
print(dog2)
sound = dog2.make_sound("woof woof")
print(sound) 
"""
Output :-->>
PS C:\Users\ckp43_000\python_programming\python_programming\Python_Oops> & C:/Anaconda3/envs/new_pychrm/python.exe c:/Users/ckp43_000/python_programming/python_programming/Python_Oops/constructors.py
<__main__.Animal object at 0x0000006122C312C8>
The animal is dog and it makes sound woof woof
"""
"""
Explanation :--->>>
creating object of Animal class keeping second constructor in mind 
and that's why passing total three attributes(name,species,age) while making object
and we got the output as expecteed, it means class Animal is considering 
the second constructor as final constructor"""


