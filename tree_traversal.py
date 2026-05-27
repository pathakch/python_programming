'''
In this module we will understand BFS and DFS (PreOrder, PostOrder InOrder), We '''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node == None:
            current_node = Node(value)
            return current_node
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def BFS(self):
        queue = []
        results = []
        current_node = self.root
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results = []

        def traverse(current_node):

            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            # call recursive method if there is left child nodes present for current node.
            if current_node.left is not None:
                traverse(current_node.left)
            # call recursive method if there is right child node present for the current node.
            if current_node.right is not None:
                traverse(current_node.right)
            # add value of current node in 'results' list if there is no any further child node of the current node
            results.append(current_node.value)
        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    ''' Interview Question : - check if bst is valid bst or not
        sol: create results list using in order method and since this results list is already sorted in ascending order
        check if any number is greater than its previous number if no then bst is valid.
    '''
    def is_valid(self):
        results = self.dfs_in_order()
        for i in range(len(results)-1):
            for j in (i, len(results)-1):
                if results[i] > results[j]:
                    return False
        return True
    
    def is_valid_bst(self):
        results = self.dfs_in_order()
        for i in range(1, len(results)):
            if results[i] < results[i-1]:
                return False 
        return True
    
    def find_kth_smallest_value(self, k):
        results = []
        if self.root == None:
            return None
        def traverse(current_node, k):
            if current_node.left is not None:
                traverse(current_node.left, k)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right, k)
        traverse(self.root, k)
        if k < 1 or k > len(results):
            return None
        return results[k-1]

    

def test_bfs():
    print(f"This is the results of BFS: {rbst.BFS()}")

def test_dfs_pre_order():
    print(f"This is the results of dfs_pre_order: {rbst.dfs_pre_order()}")

def test_dfs_post_order():
    print(f"This is the results of dfs_post_order: {rbst.dfs_post_order()}")

def test_dfs_in_order():
    print(f"This is the results of dfs_in_order: {rbst.dfs_in_order()}")



rbst = BinarySearchTree()
rbst.r_insert(47)
rbst.r_insert(21)
rbst.r_insert(76)
rbst.r_insert(18)
rbst.r_insert(27)
rbst.r_insert(52)
rbst.r_insert(82)
print(f"\nroot -> {rbst.root.value}\nleft -> {rbst.root.left.value}\nright -> {rbst.root.right.value}\n")
# print(f"This Tree is valid : {rbst.is_valid()}")
# print(f"This Tree is valid : {rbst.is_valid_bst()}")
print(f"This is kth of smallest number : {rbst.find_kth_smallest_value(3)}")
#           ------------------------------------------  Testing Code  -------------------------------------
# test_bfs()
# test_dfs_pre_order()
# test_dfs_post_order()
# test_dfs_in_order()

#---------------------- Interview Question -------------
# check if a tree is valid BinarySearchTree ?


