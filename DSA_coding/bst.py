'''
This file contains Binary Search Tree and its methods
All the methods are created using iteration (using loop - while loop)
These are the two methods created in this class
1.insert
2.contains

Generally There are all the questions of Binary Search Tree are asked using recursion, so we have again created these methods and 
many more methods and interview questions in recursive Binary Search Tree.That code will be found in 'rbst.py' module.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            if temp.value > new_node.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
               
    def contains(self, value):
        if self.root == None:
            return False
        temp = self.root
        while temp != None:
            if temp.value > value:
               temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else:
                return True
        return False



bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(10)
bst.insert(15)
bst.insert(12)

print("Root : ",bst.root.value)
print("Left child : ", bst.root.left.value)
print("Right Child : ", bst.root.right.value)
print(bst.contains(10))
    