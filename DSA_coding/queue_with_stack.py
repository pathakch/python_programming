class StackQueue:
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def enqueue(self, value):
        if len(self.first_stack) == 0:
            self.first_stack.append(value)
        else:
            while len(self.first_stack) != 0:
                self.second_stack.append(self.first_stack.pop())
            self.first_stack.append(value)
            while len(self.second_stack) != 0:
                self.first_stack.append(self.second_stack.pop())

    def print_queue(self):
        if len(self.first_stack) == 0:
            print("Queue is Empty")
        else:
            for i in range(len(self.first_stack)):
                print(self.first_stack[i])

    def dequeue(self):
        if len(self.first_stack) == 0:
            return None
        return self.first_stack.pop()
        

sq = StackQueue()
sq.enqueue(1)
# sq.print_queue()
sq.enqueue(2)
# print("Before")
sq.print_queue()
print("After insetion")
sq.enqueue(3)
sq.print_queue()
print("Removed : ",sq.dequeue())
sq.print_queue()


