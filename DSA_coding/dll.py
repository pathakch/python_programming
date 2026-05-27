class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def print_list(self):
        if self.length == 0:
            print("Doubly LinkedList is Empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.value)
                temp = temp.next

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
                temp.next = None
            return temp
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
            

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        return True
    
    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 :
            return self.pop()
        curr = self.get(index)
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.length -= 1
        return curr
    
    def is_palindrome(self):
        if self.length <= 1:
            return True
        before = self.head
        after = self.tail
        for _ in range(int(self.length/2)):
            if before.value == after.value:
                before = before.next
                after = after.prev
            else:
                return False
        return True
    
    def reverse(self):
        if self.length == 0:
            return True
        if self.length == 1:
            return True
        
        curr = self.head
        temp = self.head.prev
        new_tail = self.head
        for _ in range(self.length):
        # while curr != None:
            curr.prev = curr.next
            curr.next = temp
            temp = curr
            curr = curr.prev

        self.head = self.tail
        self.tail = new_tail

        return True
    
    def partition_list(self, num):
        if self.length == 0:
            return False
        d1 = Node(0)
        prev1 = d1
        d2 = Node(0)
        prev2 = d2
        curr = self.head
        while curr != None:
            if curr.value <= num:
                prev1.next = curr
                curr.prev = prev1
                prev1 = curr
            else:
                prev2.next = curr
                curr.prev = prev2
                prev2 = curr
            curr = curr.next
        prev1.next = d2.next
        if d2.next != None:
            d2.next.prev = prev1
            d2.next = None
        self.head = d1.next
        self.head.prev = None
        prev2.next = None

dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
print("before")
dll.print_list()
# print("pop : ",dll.pop().value)
# dll.prepend(5)
# print("After prepend\n")
# print("pop first value:",dll.pop_first().value)
# print("\nGet item : ",dll.get(0).value)
print("After")
# dll.set_value(2,10)
# dll.insert(1,100)
# print("Removed Item : :",dll.remove(2).value)
# print("Is_Palindrom : ",dll.is_palindrome())
dll.reverse()
dll.print_list()
