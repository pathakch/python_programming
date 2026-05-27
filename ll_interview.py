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
          if self.length == 0:
               self.head = new_node
               self.tail = new_node
          else:
               self.tail.next = new_node
               self.tail = new_node
          self.length += 1

     def print_list(self):
          if self.length == 0:
               print("LinkedList is Empty")
          else:
               temp = self.head
               while temp != None:
                    print(temp.value)
                    temp = temp.next

     def partition_list(self,num):
        d1 = Node(0)
        prev1 = d1
        d2 = Node(0)
        prev2 = d2
        curr = self.head
        while curr != None:
            if curr.value < num:
                prev1.next = curr
                prev1 = curr
                # prev1.next = None
            else:
                prev2.next = curr
                prev2 = curr 
                # prev2.next = None
            curr = curr.next
        prev1.next = d2.next
        self.head = d1.next
        d1.next = None
        prev2.next = None

     def reverse_between(self, start, end):
          if self.length <=1:
               return True
          
          dummy = Node(0)
          dummy.next = self.head
          prev = dummy
          for _ in range(start):
               prev = prev.next
          curr = prev.next
          for _ in range(end - start):
               node_to_move = curr.next
               curr.next = node_to_move.next
               node_to_move.next = prev.next
               prev.next = node_to_move
          self.head = dummy.next

     def remove_nodes(self):
        l = []
        curr = self.head
        while curr != None:
          runner = curr
          while runner != None:
               if curr.value < runner.value:
                break
               runner = runner.next
          else:
              l.append(curr.value)
                   
          curr = curr.next
        for num in l:
            head = Node(num)
            



ll = LinkedList(5)
ll.append(2)
ll.append(13)
ll.append(3)
ll.append(8)
# ll.append(1)
# ll.print_list()
# ll.partition_list(7)
# ll.reverse_between(1, 4)
print("After Processing")

print(ll.remove_nodes())
# ll.print_list()



