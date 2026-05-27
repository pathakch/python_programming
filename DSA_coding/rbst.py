"""
This file contains Binary search Tree and it's basic methods
All the methods are created using recursion not iteration.
These are the three methods created for Binary search Tree
1.insert
2.contains
3.Delete
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def _r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
            
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def _r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                current_node = None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)    
        return current_node

    def _delete_node(self, value):
        self.__delete_node(self.root, value)
    
    def min_value(self, current_node):
        while current_node.left != None:
            current_node = current_node.left
        return current_node.value

def main():
    rbst = BinarySearchTree()
    rbst._r_insert(2)
    rbst._r_insert(1)
    rbst._r_insert(3)
    # rbst._r_insert(90)
    # rbst._r_insert(95)
    print(f"This is the Tree:\nroot-> : {rbst.root.value}\nleft-> : {rbst.root.left.value}\nright-> : {rbst.root.right.value}")
    rbst._delete_node(2)
    print(f"This is the Tree:\nroot-> : {rbst.root.value}\nleft-> : {rbst.root.left.value}\nright-> : {rbst.root.right}")
    # print(rbst._r_contains(90))

if __name__ == main:
    main()

