''' 
Interview que: Write a method to invert binary search tree meaning swap it's left and right child
To solve this question first we will create one BinarySearchTree having insert method to insert value in it, Then we will create 
required function 'invert'. This 'invert' method will call one another recursive method __invert_tree() internally.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTreeInterview:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node == None:
            current_node = Node(value)
            return current_node
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __invert_tree(self, current_node):
        if current_node == None:
            return None
        temp = current_node.left 
        current_node.left = self.__invert_tree(current_node.right)
        current_node.right = self.__invert_tree(temp)
        return current_node

    def invert(self):
        self.__invert_tree(self.root)

def test_inversion():
    print(f"-------------Testing Inversion of BinarySearchTree -----------")
    irbst = BinarySearchTreeInterview()
    irbst.r_insert(20)
    irbst.r_insert(22)
    irbst.r_insert(18)
    print(f"root -> {irbst.root.value}\nleft -> {irbst.root.left.value}\nright -> {irbst.root.right.value}")
    irbst.invert()
    print("After Inversion:-->>")
    print(f"root -> {irbst.root.value}\nleft -> {irbst.root.left.value}\nright -> {irbst.root.right.value}")

test_inversion()