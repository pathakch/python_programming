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
            self.tail = new_node
        self.length += 1

    def print_list(self):
        if self.length == 0:
            print("LinkedList is Empty")
        else:
            temp = self.head
            res = ''
            while temp != None:
                res += str(temp.value) + " <-> "
                temp = temp.next
            print(res[:-4])

    def reverse_between(self, start, end):
        if self.length <= 1:
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
            if node_to_move.next != None:
                node_to_move.next.prev = curr
            else:
                curr.next = None
            node_to_move.next = prev.next
            node_to_move.prev = prev
            prev.next.prev = node_to_move
            prev.next = node_to_move
        self.head = dummy.next

    def swap_nodes_pair(self):
        if self.length <= 1:
            return True
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        first = self.head
        prev = first.prev
        for _ in range(int(self.length/2)):
            prev = first.prev
            second = first.next
            first.next = second.next
            if second.next != None:
                second.next.prev = first
            prev.next.prev = second
            second.next = prev.next
            prev.next = second
            second.prev = prev
            first = first.next
        self.head = dummy.next

    



class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverse_between(head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left):
            prev = prev.next
        curr = prev.next
        for _ in range(right - left):
            move = curr.next
            curr.next = move.next
            move.next = prev.next
            prev.next = move
        head = dummy.next

    def remove_nodes(head):
        curr = head
        while curr != None:
            runner = curr
            while runner != None:
                if curr < runner:
                    break
            curr = curr.next
            head = curr.next
        return head







dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
# dll.append(1)
dll.print_list()

# dll.reverse_between(0,4)
dll.swap_nodes_pair()
print("After")
dll.print_list()