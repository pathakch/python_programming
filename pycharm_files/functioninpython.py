#!/usr/bin/env python
# coding: utf-8

# #### Note  :--->>> :
#     'print' and 'return' is not the same thing 
#      print only show the output on screen ,we can't store the output coming from print in a variable meaning 
#      this output is not getteing stored anywhere in computer memory
#      But
#      output coming from 'return' is getting stored somewhere in computer memory we can store this output in a variable 
#      and use later
#      
#      1.def add(x,y):
#          print(x+y)
#        
#      2.def add(x,y):
#          return x+y

# ### Variable Scope :
#      There are two scope of variables :
#      1.Global scope 
#      2.Local scope
#      
# #### Note :->>>
#      1.python functions create local scope 
#      2.Loops and if statements do not craete local scope 

# ### Global Scope of a variable :
#      Check Below :-->>

# In[12]:


a=100
def f1():
    print(a)

def f2():
    print(a)
f1()
f2()


# ### Local Scope of a variable:
#      Check Below :-->>

# In[9]:


def f1():
    a=50
    print(a)
def f2():
    a=100
    print(a)

f1()
f2()


# ### Global and Local Variable :
#      function can't change the value of global variable
#      In below code w ecan see that the value of global variable a=100 is not changed instead we are changing 
#      the value of a as 20 and a=30 but locally in function
#      Check Below :-->>

# In[10]:


a=100

def f1():
    a=20
    print(a)

def f2():
    a=30
    print(a)
    
f1()
f2()
print(a)    


# ### Changing Global Variable :
#      We can change value of global variable using 'global variable_name' inside function
#      Check below :-->>

# In[15]:


a=250

def f1():
    global a
    a=100
    print(a)
    
def f2():
    
    print(a)
    
f1()
f2()
print(a)


# ### Exception of above Rules :
#     if global vriable is list or dictionaries then without putting keyword 'global variable_name'
#     we can change the piece of list or dictionary inside the function
#     
#     Check Below:-->>
#     

# In[19]:


a=[1,2,3,4]

def f1():
    a[2]=100    ## without putting "global variable_name" global piece of list has been changed 
    print(a)
def f2():
    print(a)
def f3():
    a=[1000,2000,3000]
    print(a)

print("original list : ",a)    
f1()
f2()
f3()


# ### Function parameters and arguments:
#      parameters are those which we define while defining function ex def add(x,y) here x and y are parameters 
#      Argumets  are those which we give while calling functions ex add(2,3) here 2 and 3 are arguments 
#      There are many types of arguments                             

# In[2]:


def about(name,age,likes): # this(name,age,likes) is parameters of function
    sentence="Meet {} He is {} years old and he likes {}".format(name,age,likes)
    return sentence


# In[24]:


about("chandan",25,"python") ## This ("chandan",25,"pyhton") is called positional arguments it should be in the same order of function


# In[25]:


about(age=25,name="chandan",likes="python") ## This is called "keyword arguments" we can put it in any order


# #### Default parameters:
#      Default parameters should be at last in function definition
#      Check Below :-->>

# In[29]:


def about(name,age,likes="football"): ## Here likes is default parameter as "football"
    sentence="Meet {} He is {} and he likes {}".format(name,age,likes)
    return sentence

print(about("chandan",25))  ##Since we have given only two argumets but in function definition 
                             #we have given one parameter as default
                             # so it will take third argument from there 

print(about("Pathak",age=20))


# ### packing and Unpacking using 
#                                    (*args) and (**kwargs)
#      (*args) this is for multiple positional arguments
#      (**kwargs) this is for multiple keyword arguments

# ## Unpacking of arguments:

# In[34]:


print(1,2,3,4)


# In[35]:


number=[1,2,3,4]   # here number is list type when we print it ,its getting printed as list (packed version)
print(number)  
print(*number)     # output of this code is unpacked version we can see in output ,because 'number' is of list type and 
                   #it's an iterable so when we have any type o iterable like list,string we can get 
                   #it printed as separate arguments inside a function using "*"


# In[37]:


print(*"abc")  # here string "abc" is an iterable and we can break it in separate arguments using '*'

print("abc") # this code will not give separate arguments because we didn't use "*" so it will be considered as single argument.


# ## Packing arguments in function:
# 

# In[38]:


def add(*numbers):
    total=0
    for number in numbers:
        total=total+number
    return total    


# In[46]:


print(add(1,2,3,4,5)) # beauty of above function "add" is it can take any number of arguments and add them 

print(add(30,40,50,60,70))


# In[ ]:





# In[ ]:





# ## keyword arguments :

# In[49]:


def about(name,age,likes):
    sentence="meet {} he is {} and he likes {}".format(name,age,likes)
    return sentence


# In[51]:


student={"name":"chandan","age":25,"likes":"python"}


# In[58]:


about(**student)  ## using "**" we can unpack dictionary type of arguments ,check output 


# In[57]:


about(name="chandan",age=25,likes="python") # same output is coming from above code also


# In[10]:


new_dict={"name":"cp","age":90,"game":"tic tao toe"}
print(new_dict)
print(new_dict.items())

print(type(new_dict.items()))

for key,value in new_dict.items():
    print (key,":",value)


# ### using "**" in arguments 

# In[11]:


def info(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))


# In[13]:


info(chandan="male",pathak="female",sohan="male",rohini="female")  ## here we can pass any number of arguments since in function we have used (**kwargs)


# In[19]:


info(**new_dict)                 
# """Conclusion : we need to put ** in both places in function parameter 
# as well as while calling this function in arguments too
# in function 'info' ** has been given in parameters section and 
# while calling in this cell code we have given ** before parameters also
# now check Output Below"""


# ### Tic Tac Toe Game :

# In[17]:


board=["  " for i in range(9)]
# board
def print_board():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])
    
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    
def player_move(icon):
    if icon=="x":
        number=1
    elif icon=="o":
        number=2
    print("Your turn player {}".format(number))
    
    choice=int(input("Enter your number from 0 to 9").strip())
    if board[choice-1]=="  ":
        board[choice-1]=icon
    else:
        print("This place is already taken")

        
def is_victory(icon):
    if ((board[0]==icon and board[1]==icon and board[2]==icon) or        (board[3]==icon and board[4]==icon and board[5]==icon) or        (board[6]==icon and board[7]==icon and board[8]==icon) or        (board[0]==icon and board[3]==icon and board[6]==icon) or        (board[1]==icon and board[4]==icon and board[7]==icon) or        (board[2]==icon and board[5]==icon and board[8]==icon) or        (board[0]==icon and board[4]==icon and board[8]==icon) or        (board[2]==icon and board[4]==icon and board[6]==icon)):
        return True
    else:
        return False
def is_draw():
    if "  " not in board:
        return True
    else:
        False
    
while True:
    print_board()
    player_move("x")
    print_board()
    if is_victory("x"):
        print("X wins !! Congratulations")
        break
    elif is_draw():
        print("Game is draw")
        break
    player_move("o")
    print_board()
    if is_victory("o"):
        print("O wins!! Congratulations")
        break
    elif is_draw():
        print("Game is draw")
        break
    


# In[75]:


print_board()


# In[ ]:




