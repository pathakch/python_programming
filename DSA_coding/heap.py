class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2*index + 1
    
    def _right_child(self, index):
        return 2*index + 2
    
    def _parent(self, index):
        return (index - 1)//2
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def print_heap(self):
        print(self.heap)

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self.swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

    def _sink_down(self, index):
        max_index = index
        while True:
            left_child = self._left_child(index)
            right_child = self._right_child(index)

            if (left_child < len(self.heap)) and self.heap[left_child] > self.heap[max_index]:
                max_index = left_child

            if (right_child < len(self.heap)) and self.heap[right_child] > self.heap[max_index]:
                max_index = right_child

            if max_index != index:
                self.swap(index, max_index)
                index = max_index
            else:
                return 


def main():
    pass

# myheap = MaxHeap()
# myheap.insert(80)
# myheap.insert(95)
# myheap.insert(75)
# myheap.insert(50)
# print("Initial Heap")
# myheap.print_heap()
# myheap.insert(60)
# print("After inserting 60")
# myheap.print_heap()
# myheap.insert(65)
# myheap.insert(55)
# print("After inserting 55")
# myheap.print_heap()

# print("Removed Value : ",myheap.remove())
# myheap.print_heap()

# print("Next Removed Value : ",myheap.remove())
# myheap.print_heap()

if __name__ == 'main':
    main()