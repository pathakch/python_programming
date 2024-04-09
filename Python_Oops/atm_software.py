class Atm:
    """
    Creating static/Class variable -- its value will remain same for each objects created from this class, we can understand this with 
    this example, Lets say we are creating one serial number for each customer who use this Atm then we will do  something like this 
    for first customer we will do this 
    c1 = Atm() (first customer and its counter will be 1)
    c2 = Atm() (second customer and it's counter will be 2)
    c3 = Atm() (Third customer and it's counter will be 3) and so on
    """
    # Creating static variable
    __counter = 1

    def __init__(self):
        """
        == Access Modifier ==
        Adding 'Access modifier' __ to make these instance variables private
        otherwise some other junior developer will import my class and in his code he can set a redundant value in 
        pin or balance lets say for balance and that time my code will get crashed like If he creates an object 
        sbi=Atm() and then in his code he set balance equals to some string value like this sbi.balance = 'abcd' 
        so now balance is set as 'abcd' but it will fail at deposit function or in withdraw function due to str 
        and int issue (balance = balance+amount here one is int and another will be str--set
        by junior developer in his code) so it's necessary to make these variables private.
        Since pin and balace are private variables now if we will try to access sbi.balance and enter to check the 
        balance or access the balance or to set any other value for balance like doing this sbi.balance = 'abcd' 
        we will get this error 'AttributeError: 'Atm' object has no attribute '__balance'. Did you mean: '_Atm__balance'?'
        it means now we can not access this two variables in our further program doing like sbi.pin or sbi.balance 
        neither for read and nor for changing them.
        We can hide any methods also like variables (using same __method_name)
        ====== What exactly happens behind the scene when we add __ before any variables or methods.=========
        This exactly happens behind the scene when we add '__' ,python changes __pin as _Atm__pin, 
        so actually junior developer can still access these variables or methods using sbi._Atm__pin but not with sbi.pin
        but still junior developer can do sbi.balance = 'anyvalue' or sbi.__balance='anyvalue' to set balance to 'anyvalue'
        but this will not crash the code because our balance variable is pointing to _Atm__balance and this is being used 
        in code not these two (sbi.balance or sbi.__balance -- ye log bas do extra reference variables ban jayenge but 
        they are not being used by our functions so our code will not be crashed)
        POINT_TO_REMEMBER : Nothing is actually private in python (private attribute/methods can be accessed by writting <object_name._ClassName__Variablename> )
        """
        self.__pin = ''
        self.__balance = 0
        """Creating a serial number for each customer it will be unique and not be increamented by creating other objects of class , let's say 
        we are creating a customer at 6th number like this c6 = Atm(), now if we will check the sno of this customer by doing this c6.sno it will be 6
        at the same time Atm.counter value will also be same but if we will check sno no  of fourth customer doing this c4.sno then it will be 4 
        and if we will check like this c1.counter or c2.counter or c3.counter then these all will be equals to Atm.counter and this will depend that 
        which number of customer is created or accessed the Atm at last -- why its happening because we are increamenting counter value with 1 or each 
        customer visiting Atm but we are not increamenting sno of an object or customer , we are just assigning the current counter value as sno 
        for any newly created customer
        """
        # Assigning current counter value of class to the newly object being created
        self.sno = Atm.__counter #(No need to use 'self' to access static or class variable)
        # Increamenting counter value by 1 for each new object created or new customer visiting Atm
        # To access static or class variable 'self' is not required, we can access them by writing <class_name.static_variable_name>
        Atm.__counter = Atm.__counter + 1

        self.menu()

        """
        creating getter and setter method to  access the variables and to set some vaules if needed, since we have hiden these 
        variables and so junior developer can not access and set any values to these variables so we are giving him one 
        option to set these values if needed by these two functions getter and setter
        So the whole idea behind hiding these data from any other developer but giving them access to access these data
        and set some values for these data but fullfilling the conditions written in these two types of functions getter and 
        setter  -- this is the complete idea of Encapsulation.
        First hide the data and then give access but on some condition.-- and this way our data members are protected
        and can be used too by some other junior developer.
        So now any junior member can access these data members and set their values if needed like explained below
        sbi.get_pin() will show them the current value of pin and sbi.set_pin() will alow them to set any different pin
        but passing the condition written in this function , same will be applied for balance too.
        """
    def get_pin(self):
        return self.__pin
    def set_pin(self):
        new_pin = input("Enter new pin to set : ")
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin Changed")
        else:
            print("Not Allowed")
    def get_balance(self):
        return self.__balance
    def set_balance(self):
        new_balance = input("Enter new balance to set")
        if type(new_balance) == int:
            self.__balance = new_balance
            print("Balance set successfully")
        else:
            print("Not Allowed")
        """
        since we have made counter as private variable so that no junior developer who is using my class Atm can set the 
        value of counter wrongly, But at the same time we need to give junior developer accesss to this counter by getter and setter methods so that 
        if needed he can modify the value of counter in his program writing like 'object_name.set_counter(new_counter)'.
        Now since we are creating these getter and setter method to handle static/class variable so these unctions are called staticmethod and to denote them 
        we use this keyword '@staticmethod'.
        Things to Notice :-->> 'self' is not required in static method like other methods. why because we do not access static variables using self
        and these method use static variables only so why to use self in these methods. or say why to use object in these methods.
        (self is required in those methods which deals with instance variables because we access instance variables by self only.)
        Point To Remember :--->>> 
        1. static methods can be used by this way <ClassName.static_method_name> (not like other methods -- <object_name.method_name>)
        2. Meaning Objects are not required to use Static Method.(These methods can be accessed by class name).
        """        
    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new_counter):
        if type(new_counter)== int:
            Atm.__counter = new_counter
            print("New counter set successfully")

    def menu(self):
        user_input = input(""" 
            Hello,how would you like to proceed ?
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check __balance
            5. Enter 5 to exit 
            """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print("Bye! See you next time !")

    def create_pin(self):
        tmp_pin = input("Enter your pin : ")
        self.__pin = tmp_pin
        print("Pin set successfully")
    
    def deposit(self):
        if self.__pin:
            tmp_pin = input("Enter your pin : ")
            if tmp_pin == self.__pin:
                amount = int(input("Enter amount to deposit : "))
                self.__balance = self.__balance + amount
                print("Amount deposited successfully")
            else:
                print(f"wrong pin : {self.__pin} entered")
        else:
            print("First of all set your pin ")
    def withdraw(self):
        tmp_pin = input("Enter your Pin : ")
        if tmp_pin == self.__pin:
            if amount >= self.__balance:
                amount = input("Enter amount to withdraw : ")
                self.__balance = self.__balance - amount
            else:
                print(f"Insufficient balance")
        else:
            print(f"Wrong pin {self.__pin} entered")
    def check_balance(self):
        tmp_pin = input("Enter your Pin : ")
        if tmp_pin == self.__pin:
            print(f"This is your current balance : {self.__balance}")
        else:
            print(f"Wrong pin entered : {self.__pin}")
