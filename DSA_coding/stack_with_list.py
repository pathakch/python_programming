#   ------------------------------- Implemenation of Stack Using inbuilt python List -----------------------
class Stack:
    def __init__(self):
        stack_list = []
        self.stack_list = stack_list
    
    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False
        
    def push(self, value):
        self.stack_list.append(value)

    def print_stack(self):
        if len(self.stack_list) == 0:
            print("Stack is Empty")
        else:
            for i in range(len(self.stack_list)-1, -1, -1):
                print(self.stack_list[i])

    def peek(self):
        if self.stack_list == 0:
            return None
        return self.stack_list[-1]
    
    def size(self):
        return len(self.stack_list)
    
    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()
    
stack = Stack()
print(stack.is_empty())   
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.print_stack() 
print(stack.is_empty())