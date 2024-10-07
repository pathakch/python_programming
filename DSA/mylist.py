'''
In this class we will create our own list mylist like a python list and it will have 
all the functions which a python list has
A python list has all the below functions and we will create these functions for our own list
This concept is based on Dynamic Array -- because python list is a dynamic array so we wanted to create
our own list and check the concept how python list is of variable length and heterogenuous
To create our own list we need one module `ctypes`-- what is this module  search on google --it provides 
c language compatible data types inside python why we used it because we will create MyList using C 's array
we do not use python list and make our own list we will use C's array and create our own list MyList class 
here point to be noted is our MyList is a class which is dynamic array ultimately  so our goal is to create 
a dynamic array like python's list.

1. create list [D]
2.Len[D]
3.append[D]
4.print[D]
5.indexing[D]
6.pop[D]
7.clear
8.find
9.insert
'''
import ctypes

class MyList:
    def __init__(self):
        '''
         here size represents how many maximum items we can store in this array, 
        initially we will start with sie =1 then it will increase gradually 
        if required like python's list but intially it should be at least 1.'''
        self.size = 1  
        self.n = 0 # represents how many items are there currently inside the array, initially its zero

        #create a C type array with size = self.size
        '''
        we will create a function create_array which will create an C's static array using ctypes module 
        Note : below code is like we are declaring an attribute A of class MyList like other two attributes
        size and n '''
        self.A = self.create_array(self.size) 

    def create_array(self,capacity):
        '''
        This is not python code, it's C's code so not very much understable.
        and create a C type array (fixed or static array, and also a referential array) with size capacity'''
        return (capacity*ctypes.py_object)()
    
    #Adding length feature or our own list 
    def __len__(self):
        '''we will create a magic method __Len__() , this method is same like python's list len() 
        method that's why we have taken the same name , and it will simply return the number of 
        items present in the array at that time
        '''
        return self.n
    
    # adding append functionality in our own list
    def append(self,item):
        if self.size == self.n: # if array is full means , agar size utna hi hai jitna number of element then it's full to humein isi size double kar k isme pahle wali values copy karni padegi.
            #resize
            self.resize((self.size)*2)
        #append
        self.A[self.n] = item  #we will assign nth element as n 
        self.n = self.n + 1  #since we have added one element so the value of n will increase by because n is the number of values in array currently.
    # resize
    def resize(self, new_capacity):
        '''
        we will create a new array of double size of existing array and copy the values of existing array 
        into new one
        will call create_array function to create new array of size as new_capacity
        '''
        B = self.create_array(new_capacity)
        self.size = new_capacity
        # copying previous values to new array, loop will run n times because
        # number of element in existing array were n only
        for i in range(self.n):
            B[i] = self.A[i]
        # pahle wale array A ko ab B represent kar rha hai toh humein btana hoga ki ab B is A hai 
        self.A = B
    # adding print feature in our list
    def __str__(self):
        '''
        __str__ method is in built method of python it can be modified or can be called as it is 
        Actually jab bhi hum aisa likhte hai class_object.__str__() it return object memory format or kuchh aisa 
        the object <__main__.Classname object at 0x0000013BFF5FFB50> or say 
        The python __str__ method returns the string representation of the object
        or we can write like this also class_object to bhi humko aisa hi 
        kuchh output milta hai <__main__.Classname object at 0x0000013BFF5FFB50>
        or agar hum likhte hai  print(Object_Name) toh bhi kuchh aisa hi output dekhne ko milta hai 
        Also, jab bhi hum `print()` ko calll karte hai toh ye __str__ method hi execute hota hai automatically 
        ye tha iska default behaviour jo humne upar dekha hai 
        Ab humko is __str__ function ko apne hisab se change bhi kar skate hai and jo kuchh bhi 
        chahe krwa sakte hai wo bhi jaise hi `print` likha jayega ye method call ho jayega 
        Aisa hum our bhi alag magic methods k sath kar sakte hai'''
        
        # [1,2,3,4] python ka list aisa hi dikhta hai toh humara bhi list aisa hi dikhna chaiye after printing
        result = ''
        for i in range(self.n): # loop will run only n times because n hi elements hai abhi array A mein.
            result = result + str(self.A[i]) + ',' 
        return '[' + result[0:-1] + ']' # python ka list square bracket m ata hai toh humara bhi [] bracket m hi ayega. lekin last wala comma htana parega otherwise it will come like this [1,2,3,4,], result ek string hai mujhe result ka sab kuchh chaiye except last item toh slicing lagaya gya hai to avoid last element

    # adding indexing functionality to our array mylist
    # for this we will create a magic method getitem which will take index number and return element of that index
    def __getitem__(self,index):
        '''this is also a magic method like __str__ and we are modifying it for our purpose
        ye wala method kaise triger hota hai ??? AAns - jaise hi object k aage paranthese m index dalte hai like
        object_name(4) , toh ye triger ho jata hai. or jo bhi us index par hoga wo return kar dega.
        '''
        if 0 <= index <=self.n:
            return self.A[index]   # simply we can return element at index position, and ye kaam karega kyo ki C ka array bhi aise element return karta hai   
        else:
            return 'index out of range'
        
    # adding pop() unctionality in our array 
    def pop(self):
        if self.n == 0:
            return 'Empty list'
        self.n = self.n - 1
        return self.A[self.n-1]   
    # adding `clear` functionality in mylist array
    def clear(self):
        self.n = 0  
        self.size = 1  

    # adding find functionality 
    def index(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'Value Error - Not in list'
    
    #adding insert functionality in `mylist`
    def insert(self,idx,item):
        '''
        This is function for our mylist like python list has same function and it will insert an element
        at a specific index mentioned , Python list bhi same aise hi kaam karta hai
        yahan pahle check karte hai ki array m jagah hai ki nahi 
        condition 1. agar jagah hai toh just shifting karo shifting k liye ulta loop chlana hoga , 
        from n toh the idx+1 - refer notbook for logic
        condition 2. Agar jagah nahi toh size double karo and then continue above logic '''
        if self.size == self.n:
            self.resize(self.size*2)
        for i in range(self.n, idx,-1):
            self.A[i] = self.A[i-1]
        self.A[idx] = item
        self.n = self.n + 1



a = MyList()
a.append(24)
a.append(8000)
a.append('hello')
a.insert(1,3000)

# print(len(a))

# print(a.pop())
# print(len(a))

# print(a)
# print(a[1])
# a.clear()
print(a)
# print(a.index('hello'))        