


##-------------------------------------- Implemenattion of stack using inbuilt python List ------------------------------------

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def reverse_string(st):
    l = Stack()
    for char in st:
        l.push(char)
        
    new_st = ''
    for _ in range((l.size())):
        new_st = new_st + l.pop()
    return new_st

def is_balanced_parentheses(st):
    s = Stack()
    for p in st:
        if p == '(':
            s.push(p)
        else:
            if s.is_empty() or s.pop() != '(':
                return False
    if not s.is_empty():
        return False
    return True

def sorted_stack(st):
    sorted_stack = Stack()
    while not st.is_empty():
        temp = st.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
                st.push(sorted_stack.pop())
        sorted_stack.push(temp)
    while not sorted_stack.is_empty():
        st.push(sorted_stack.pop())
    return st

my_string = 'hello'
# print ( reverse_string(my_string))
st = Stack()
st.push(2)
st.push(4)
st.push(1)
st.push(3)
st.print_stack()
# print(is_balanced_parentheses(st))
print("After")
(sorted_stack(st).print_stack())
