class New_Animal:

    #creating constructor
    def __init__(self,*args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.species = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]    

dog3 = New_Animal('dog')
print(dog3.name)

dog4 = New_Animal('dog','mammalas')
print("name of animal is :",dog4.name,"\nAnd species of animal is :",dog4.species)