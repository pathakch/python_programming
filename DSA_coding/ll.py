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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next != None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value
        
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head 
            self.head = temp.next
            temp.next = None
            self.length -= 1

            if self.length == 0:
                self.tail = None
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, value, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return self.prepend(value)
        temp = self.head
        new_node = Node(value)
        for _ in range(index-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def set_value(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index-1)
        temp =pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            


ll = LinkedList(2)
ll.append(3)
ll.prepend(1)
ll.print_list()
print('removed item :', ll.reverse())   
print("after")
ll.print_list()