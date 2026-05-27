class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
    #insert a new node into linkedlist from head
    def insert_node(self, value):
        #create new node
        new_node = Node(value)

        #create connection
        new_node.next = self.head

        #reassign head
        self.head = new_node
        
        #increment size of ll
        self.n += 1
    
    # traverse through linkedlist
    def __str__(self):
        curr = self.head
        res = ''
        while curr != None:
            res = res + str(curr.data) + '->'
            curr = curr.next
        return res[:-2]
    
    # insert a new node into likedlist from tail (inserting from tail is called append)
    def append(self, value):
        #create a new node
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n += 1
            return

        #travesre through linkedlist to the tail
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n += 1
        
    def insert_after(self, after, value):
        #create new node
        new_node = Node(value)
        #traverse through ll and reach to 'after'
        curr = self.head
        while curr != None:
            #comapre data of node if it equals to after then break the loop or continue
            if curr.data == after:
                break 
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return f'{after} Not Found in LinkedList'

    # Make a LinkedList empty
    def clear(self):
        self.head = None
        self.n = 0

    # Delete one node from head(delete head)
    def delete_head(self):
        if self.head == None:
            return 'LinkedList is Empty'
        
        self.head = self.head.next
        self.n -= 1

    # delete any item by its value
    def remove(self, value):
        #check if LinkedList is empty or not 
        if self.head == None:
            return 'LinkedList is Empty'
        
        #check if the node to be deleted is head, if yes then call function 'delete_head', no need new code
        if self.head.data == value:
            return self.delete_head()
        
        curr = self.head
        while curr.next != None:
            #break the loop one node before the value node
            if curr.next.data == value:
                break
            curr = curr.next

        # check if the loop traverse through complete LL or not
        if curr.next != None:
            curr.next = curr.next.next
            self.n -= 1
        # Loop traverse through complete LL, means item not found
        else:
            return f"{value} Not Found"

    # Delete node from tail
    def pop(self):
        #check if LL is a an Empty LL
        if self.head == None:
            return "LinkedList is Empty"
        
        #check if LinkedList has only one node
        if self.head.next == None:
            #since LL has only one node that is head, we will call the function to delete the head, 
            # no need to write separate code
            return self.delete_head()

        #traverse through linkedlist and go to one node before tail
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n -= 1

    #--------- Search by Value ------
    #search a value in LL and return it's index
    def find(self, value):
        #traverse through LL and check if data match with node data
        curr = self.head
        idx = 0
        while curr != None:
            if curr.data == value:
                return idx
            curr = curr.next
            idx += 1
        return f"Item {value} Not Found in LL"
      
    #--- Search by Index --- 
    def __getitem__(self, idx): # this is magic method, when we will give l[index] it will return value on 
        # that index, like list of python
        #check if LL is Empty
        if self.head == None:
            return "LL is Empty"
        
        pos = 0
        curr = self.head
        while curr != None:
            if pos == idx:
                return curr.data
            curr = curr.next
            pos += 1
        return f"Index {idx} out of range"
        
    # Que: Replace max value of LL with a given value
    def replace_max(self, value):
        temp = self.head
        max = temp
        while temp != None:
            if temp.data > max.data:
                max = temp
            temp = temp.next
        max.data = value

    # sum of values at odd positions
    def odd_sum(self):
        curr = self.head
        pos = 0
        sum = 0
        while curr != None:
            if pos%2 != 0:
                sum += curr.data
            curr = curr.next
            pos += 1
        return sum
    
    # Reverse the LL
    def reverse(self):
        
        prev_node = None
        curr = self.head

        while curr != None:
            temp_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = temp_node
        self.head = prev_node

    def merge(self, l2):
        i = j = 0
        curr1 = self.head
        curr2 = l2
        while curr1 != None and l2 != None:
            if curr1.data < l2.data:

l1 = Linkedlist()
l1.insert_node(4)
l1.insert_node(5)
l1.insert_node(6)
l1.insert_node(7)
l1.insert_node(8)
l1.insert_node(9)

# print(l1.pop())
# l1.append(7)
# print(l1.delete())
# print(l1.pop())
# print(l1.remove(4))
# print(l1.insert_after(50, 10))
# print(l1.find(10))
# print(l1[2])
# print(l1.replace_max(500))
# print(l1.odd_sum())
# l1.reverse()

print(f"Number of nodes in LL = {len(l1)}")
print(f"Linkedlist is : {l1}")
