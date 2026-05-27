class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def __str__(self):
       curr = self.head
       res = ""
       while curr != None:
           res += str(curr.value)+'->'
           curr = curr.next
       return res[:-2]

l1 = LinkedList(1)
print(l1.append(2))
print(l1)



