################
# -------------------------- Implementation Of Queue using LinkedList -----------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        if self.first == None:
            print("Queue is Empty")
        else:
            temp = self.first
            while temp != None:
                print(temp.value)
                temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.first == None:
            return None
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp

q = Queue(1)
q.enqueue(2)
q.enqueue(3)
q.print_queue()
print("Removed : ",q.dequeue().value)
print("Removed : ",q.dequeue().value)
print("Removed : ",q.dequeue().value)
print("Removed : ",q.dequeue())
print("After")
q.print_queue()

