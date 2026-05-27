#####################################################################################################
####  ------------------------------Implemenation of Stack Using LinkedList --------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def print_stack(self):
        if self.height == 0:
            print("Stack is EMpty")
        else:
            temp = self.top
            while temp != None:
                
                print(temp.value)
                temp = temp.next

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
        
st = Stack(1)
st.push(2)
st.push(3)
st.print_stack()
print("removed : ",st.pop().value)
st.print_stack()

# ------
st = 'word'

l = []
for char in st:
    l.append(char)

new_st = ''
for _ in range(len(l)):
    new_st = new_st + l.pop()

print(new_st)
