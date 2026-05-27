l = [4,2,6,5,1,3]
def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

# print(bubble_sort(l))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def print_list(self):
        if self.head == None:
            print("LinkedList is Empty")
        else:
            curr = self.head
            res = ''
            while curr != None:
                res += (f"{curr.value} -> ")
                curr = curr.next
            print(res[:-3])
        
    def bubble_sort(self):
        if self.length == 1:
            return self.head
        if self.head == None:
            return None
        for i in range(self.length-1, 0, -1):
            temp = self.head
            after = temp.next
            for j in range(i):
                if temp.value > after.value:
                    moving_value = after.value
                    after.value = temp.value
                    temp.value = moving_value
                temp = temp.next
                after = temp.next

    def selection_sort(self):
        if self.length < 2:
            return 
        temp_2 = self.head
        for i in range(self.length -1):
            min_node = temp_2
            temp_3 = temp_2.next
            for j in range(i+1, (self.length)):
                
                if min_node.value > temp_3.value:
                    min_node = temp_3
                temp_3 = temp_3.next
            if temp_2 != min_node:
                temp_2.value, min_node.value = min_node.value, temp_2.value
            temp_2 = temp_2.next
    
    def selection_sort_while(self):
        if self.length < 2:
            return
        current = self.head
        while current != None:
            smallest = current
            inner_current = current.next
            while inner_current != None:
                if smallest.value > inner_current.value:
                    smallest = inner_current
                inner_current = inner_current.next
            if current != smallest:
                current.value, smallest.value = smallest.value, current.value
            current = current.next

    def selection_sort_tut(self):
        if self.length < 2:
                return
        current = self.head
        while current.next != None:
            smallest = current
            inner_current = current.next
            while inner_current != None:
                if inner_current.value < smallest.value:
                    smallest = inner_current
                inner_current = inner_current.next
            if smallest != current:
                current.value, smallest.value = smallest.value, current.value        
            current = current.next

    def insertion_sort(self):
        if self.length < 2:
            return
        
        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None

        while unsorted_list_head != None:
            current = unsorted_list_head
            search_pointer = sorted_list_head
            if current.value < search_pointer.value:
                unsorted_list_head = unsorted_list_head.next
                current.next = search_pointer
                sorted_list_head = current
            else:
                while search_pointer != None and current.value > search_pointer.value:
                    temp = search_pointer
                    search_pointer = search_pointer.next
                unsorted_list_head = unsorted_list_head.next
                current.next = search_pointer
                temp.next = current

        self.head = sorted_list_head    
        while sorted_list_head != None:
            temp = sorted_list_head
            sorted_list_head = sorted_list_head.next
        self.tail = temp

    # function to apply merge helper function in linkedlist (This function is created by me without any hint therefore it has some extra code)
    def merge(self, ll):
        dummy = Node(0)
        current = dummy
        temp = self.head
        other_head = ll.head
        while temp != None and other_head != None:
            if temp.value < other_head.value:
                current.next = temp
                temp = temp.next   
            else:
                current.next = other_head
                other_head = other_head.next   
            current = current.next
            current.next = None
        while temp != None:
            current.next = temp
            temp = temp.next
            current = current.next
            current.next = None
        while other_head != None:
            current.next = other_head
            other_head = other_head.next
            current = current.next
            current.next = None
        self.head = dummy.next
        temp = self.head
        while temp.next != None:
            temp = temp.next
        self.tail = temp

        counter = 0
        temp = self.head
        while temp != None:
            temp= temp.next
            counter += 1
        self.length = counter

    # this helper function is created with the help of udemy solution hint, it's optimized and contains less number of lines of code than my function
    def merge_udemy_hint(self, ll):
        # create one dummy node with value = 0
        dummy = Node(0)
        # create one pointer 'current' to point this dummy node.
        current = dummy
        # get the head of second linkedlist
        other_head = ll.head
        while self.head != None and other_head != None:
            if self.head.value < other_head.value:
                current.next = self.head
                self.head = self.head.next   
            else:
                current.next = other_head
                other_head = other_head.next   
            current = current.next
        # if any node left in first linkedlist then add the complete left part to the new  resulting linkedlist
        # for that just need to get the head of left part and attach it to the resulting linkedlist as it is
        if self.head != None:
            current.next = self.head

        # if any node in second linkedlist is left then do the same as above, also update the tail of resulting linkedlist  
        else:
            current.next = other_head
            self.tail = ll.tail
        # update head of resulting linkedlist  
        self.head = dummy.next
        # update length of resulting linkedlist
        self.length += ll.length
        
        




        


        






ll = LinkedList(3)
ll.prepend(1)
ll.append(5)
ll.append(7)


ll2 = LinkedList(2)
ll2.append(4)
ll2.append(6)
ll2.append(8)
ll2.append(10)
ll2.append(12)
ll.print_list()
ll2.print_list()
# ll.bubble_sort()
# ll.selection_sort_tut()
# ll.insertion_sort()
ll.merge_udemy_hint(ll2)
print(ll.length)
ll.print_list()

