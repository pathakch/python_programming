def nameCheck(name):
    if len(name) < 2:
        print("checking or name length")
        return 'invalid name'
    elif name.isspace():
        print("checking if name is a space")
        return 'invalid name'
    elif name.isalpha():
        print("checking if name is an alphabet")
        return 'name is valid'
    elif name.replace(' ','').isalpha():
        print('checking for full name')
        return 'name is valid'
    else:
        print("failed all checks")
        return 'invalid name'
    
print(nameCheck('chandan123'))
"""
Output :-->
invalid name

Explanation : we have commented all the 'print' statements so we are not able to 
know that which parts of code is giving this message 'invalid name' in output
now we will use 'print' statement(uncomment) to know this 
""" 
print(nameCheck('chandan123'))
"""
Output :-->
failed all checks
invalid name

Explanation :-->>
Here we can see that output 'invalid name' is coming after last block 'else' execution
this is the use of print statments 
"""

