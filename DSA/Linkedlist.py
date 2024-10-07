'''
In this tutorial we will learn to create individual node and then learn to create complete likedlist
SO, basic idea and understanding and explaination is written in the hardcopy notebook 
'''
# Creating individual Node and then linking them to create linkedlist
class Node:
    def __init__(self, value):
        '''
        Since a node contains two part first part contains data and second part contains address of 
        next node , here we will create a node with value what will be passing and address part 
        will contain None since there will be no next node so '''
        self.data = value
        self.next = None
# create node one 
a = Node(2)
# print(a)  # o/p : <__main__.Node object at 0x0000000DDA635EE0>, SInce a is an object of a class so o/p is coming like this representing an object at given memory location 
# create 2nd node 
b = Node(3)
# craete third node 
c = Node(10)

#creating link between nodes manually (just for understanding we are creating link manually here, because it will not be created manually once we will craete LinkedList class then links will be created inside that class)
a.next = b  # (Here when we write print(b) it will print `<__main__.Node object at 0x0000000DDA635EE0>`  means its memory address of next node b and it will assigned to attribute `next` of first node a)
b.next = c  # (Here when we write print(c) it will print `<__main__.Node object at 0x0000000DDA935EE0>`  means its memory address of next node c and it will assigned to attribute `next` of first node b)
# And above code created a link between a,b and c. So now its a complete linkedlist with 3 nodes 
#**********************************************************************************************************************************************************************************************************************

'''
Starting linkedlist creation
There are total 4 operations mainly in LL
1. Insert 
    a. insert by head 
    b. insert by tail
    c. insert in middle
2. traverse
    print
3.delete
    a. Delete from head
    b. delete from tail (it is like pop of python list)
    c. delete a specific value (it is like remove of python's list)
    d. delete by index
4. Searching
    a. 
'''
class LinkedList:
    def __init__(self):
        #create empty LL , in empty LL head will be None always and everywhere 
        self.head = None # head is the first node
        self.n = 0 # n represents the number of nodes in LL 

    # creating length function for LL , length of LL is number of nodes in LL
    # for this one we create a magic method.
    def __len__(self):
        return self.n
    
    # creating insert functionality - by head
    def insert_head(self,value):

        #create new node
        new_node = Node(value)

        # create connection, since this is the first node being created so head will point to this node,means this node will become head.
        new_node.next = self.head

        #reassign head
        self.head = new_node 

        # Increasing size of LL, since we have added one node,initially there was zero node
        self.n = self.n + 1

    ''' Now we will learn traverse in LL,Traverse means printing data of each nodes in a LL
        see below function to understand, SO the concept here is , ek variable curr bnate hai 
        jo ki head ko represent karega initially , head pehla node hota hai  uske bad second iteration
        se curr represent karne lagega self.next ko , while loop chlana hai until curr != None, ye 
        curr None tab hoga jab ye last wale Node ko represent karne lagega, kyo ki last wala Node ka address 
        None ko represent karta hai'''
    # def traverse(self): # rather than traverse we will crreate magic method __str__() jo 
    def __str__(self):
        # yahan par current ek Node hai , jiske 2 attributes hai data and next (we can see that in Node class)
        curr = self.head # Head to ek Node ko hi represent karta hai (upar function m dekh sakte hai self.head = new_node), toh curr ek Node hai jo ki pehla Node ko represent kar rha hai LL m 

        result = ''

        while curr != None:
            result = result + str(curr.data) + '->'
            
            #loop increment 
            curr = curr.next # yahan par hum curr k address wale part ko next node k address ko represent krwa denge
        return result[:-2]
    ###################### Learning Append functionality into LL ########################
    '''we will learn inserting new node from tail  in LL, means append -- inserting from tail is called append
       Here the concept is sabse pahle hum 
       ek new_node bnayenge taking required value by using Node class
       Then, we will check if LL is empty if yes, toh jo bhi hum new node append karne wale hai wahi head ho 
       jayega , kyo ki empty list ka head toh None hota hai , toh jo bhi new node ayega wahi toh head banega 
       that's All.
       if LL is not empty then 
       then hum traverse kark last node tak jayenge and last node k next ko == new_node kar denge
       since append k pahle las node ka ddress wala part None ko represent kar rha tha , ab wo new_node k address
       ko represent karega.
    '''
    def append(self,value):
        #create new_node
        new_node = Node(value)
        if self.head == None: #checking if LL is empty or not
            self.head = new_node
            # increase length of LL by 1 , since 1 Node added 
            self.n = self.n + 1
            # yahan par agar humko kewal ek hi node add karna ho toh hum yahi return kar denge 
            # return karne se ye hoga ki niche wala code nahi chalega
            return                 
        curr = self.head 
        # traverse to last node means tail, 
        ''' ye last node tak chalega ,means last Node k ek pahle node par hi ruk jayega kyo ki tail ka next to None 
            hoga to wo is loop ko satifiy nahi karega and ruk jayega
        '''
        while curr.next != None:            
            # incrementing loop iterator (curr node will represent to next node) while condition tail k ek pahle 
            # node tak hi chalega, lekin is wale step m curr tail ko represent karne lagega , 
            # toh finally hum tail tak pahuch gaye hai jo ki hamara aim tha.
            curr = curr.next
        curr.next = new_node # tail k address wale part m new_node ka address dal dena hai, toh new_node tail ban jayega
        # increase length of LL by 1 , since 1 Node added 
        self.n = self.n + 1 

    '''Inserting new_node in between somewhere -- this is called insert_after do not know this term is generic 
       or only for this tutorial
    '''
    # below function is created by me -- on my concept purely
    # def insert_after(self,value,item): # this function is created by me completely.
    #     #create a new_node with required value
    #     new_node = Node(item)

    #     found = 'Y'
    #     curr = self.head
    #     while found == 'Y':
    #         if curr.data == value:
    #             found = 'N'
    #             before_node = curr
    #         curr = curr.next
    #     new_node.next = curr
    #     before_node.next = new_node
    #     self.n = self.n +1
    def insert_after(self, after, value):
        new_node = Node(value)

        curr = self.head # yahan curr pehle wale node ko represent kar rha hai.
        '''
        In below loop - this loop will run starting from head to tail, ye tail tak consider karega kyo ki 
        humne curr != None , ye loop tail k ek pahle tak k node  ko hi consider karega, matlab tail k ek pahle 
        tak chalega, phir niche humne curr ko ek increment kiya hai toh curr tail node ko represent karne 
        lagega jab ye loop complete hoga tab.
        agar humko tail k ek pahle tak consider karna hai toh curr.next != None hoga
        agar tail k 2 pahle tak ka node consider karna hai toh cur.next.next != None likhte hai
        Yahnan par humein kisi value k after ek new node insert karna hai, matlab loop us node ko bhi consider 
        karega isliye curr != None likha hai
        '''
        while curr != None:  # ye condition tail node k ek pahle tak chalega, tail node par ye condition false hoga
            if curr.data == after:
                break # yahan par loop break ho rha hai toh, curr usi node ko represent karega jiske bad new_node ko insert karna hai
            curr = curr.next # yahan par humne curr ko ek incement kiya hai toh last iteration k bad, curr will point to tail 
        
        """
        try catch block add karna pad rha hai kyo ki bina, iske else condition likhne par
        python error throw kar de rha hai, agar koi aisa element k badd node insert krwana ho jo element
        LL m ho hi nah toh humein likhna tha ki print( "Item not found") lekin is condition m 
        control pahle check kar rha tha [if condition curr.next != None] our yahi par error aa jata tha kyo ki 
        yahan par curr represent kar rha tha None wo kaise ?? kyo ki loop to pura tail tak chla hai is condition m
        wo element ko dhundhne k chakkar m and element nahi mila hai toh, loop break bhi nahi huwa hai
        and uske badd loop ko incement kar rhe hai hum aisa likhte huwe [cur = cur.next]
        toh yahan par curr ki value ho ja rhi hai None kyo ki curr.next (means tail.next) to None hota hai
        isliye curr None ko represent kar rha hai 
        """
        try:
            if curr.next != None: # means item mil gya hai bina loop k complete huwe hi, agar curr = None hota hai is loop m iska matlab loop pura chla hai and data {after} nahi mila hai
                new_node.next = curr.next
                curr.next = new_node
                self.n = self.n + 1 # since we have addedone element length is increased by one.
        except:
            print(f'\nItem {after} not found')

    ###################### Learning Deletion functionality into LL ########################
            # 1. clear -- means make LL empty
    def clear(self):
        self.n = 0 # LL ko empty bna ne k liye uske size ko 0 karna hoga means number of node ko 0 karna hoga.
        self.head = None # LL ko empty bna ne k liye head ko None karna hoga 

    def delete_head(self):
        '''
        first of all check whether LL is empty if yes then [return LL is empty] means if self.head = None, so LL is empty
        if LL is not empty then logic is below
        humko head ko delete karna hai matlab, deletion k bad head apne 
        aage wale node ko represent karega matlab aag wala node hi head ho jayega
        toh logic simple hai , head ko brabar kar do aage wale node k , par wo kaise 
        toh head = head ka address wala part wala (head k address wale part m hi aage wala node ka address hai)
        '''
        if self.head == None:
            print('Linkedlist is Empty')
            return
        self.head = self.head.next
        self.n = self.n - 1 # since we have deleted one node so size got reduced by one

    def pop(self): # pop will remove last node of LL
        
        # First of all we check if LL is Empty, if yes then return here bcz no need to pop anything in this condition
        if self.head == None:
            print("Linkedlist is Empty")
            return
        curr = self.head
        '''
        Check if LL has one node : in this condition how pop will work, in this condition pop will 
        remove that node one node (That's the head node) , so it will become delete head.(In this case no need to run any loop -- check below)
        '''
        if curr.next == None: # checking if LL has only one node
            return self.delete_head()
        
        # if LL has more than one node then need to run a loop -- Check below
        '''
        ye loop 3rd last element tak chalega matlab 3rd last node par bhi ye condtion true hoga and control 
        loop k andar jayega , phir andar m hum curr ko ek node se increase kar rhe hai toh wo curr 2nd 
        last node ko represent karne lagega
        '''
        while curr.next.next != None: 
            curr = curr.next # incrementing loop to its next node from its current node
        # jab loop complete ho jayega toh curr second last node ko point kar rha hoga 
        # toh uske next ko None bnana hoga 
        curr.next = None
        self.n = self.n - 1



ll_1 = LinkedList()
# print(ll_1) # it will print location of this object in memory

# inserting nodes to LinkedList ll_1
# ll_1.insert_head(1) # 1 is value of data part of node 
# ll_1.insert_head(2) # 2   ,,,
# ll_1.insert_head(3) # 3 ,, ,,, 
# ll_1.insert_head(4) # 4 ,,,  ,,,,

# printing length of the linked list, it should be 4 , cz added 4 nodes above.
# print('Length of linkedlist ll_1 is : ',len(ll_1))
# ll_1.traverse() # o/p will be reverse means printed like this -->> 4,3,2,1 kyo ki hum head pakad kar new_node insert kar rhe hai LL m isliye last wala 4 insert huwa hai LL k head m , matlab head k jagah par 4 hai then next node 3, then next node 2 and so on.

# since we have craeted magic method for traverse we will use that , see bewlo 
# print(ll_1)  # O/P will be like this 4-->3-->2-->1

# appending new node from tail
# ll_1.append(5)
# ll_1.append(6)
# print(ll_1) # O/P is : 4->3->2->1->5->6
# print(len(ll_1)) # O/P is 6

# ll_1.insert_after(20,30)
# print(ll_1) # O/P is : 4->3->30->2->1->5->6 
# print(len(ll_1)) # O/P is 6
# ll_1.clear()
ll_1.pop()
print(f"Length of linkedlist is {len(ll_1)} and linkedlist is {ll_1}")
# ll_1.delete_head()
# print(f"Length of linkedlist is {len(ll_1)} and linkedlist is {ll_1}")





