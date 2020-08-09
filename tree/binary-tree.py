# Node Class
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = self.right = None
    
# Binary Tree Class
class BinaryTree:
    def __init__(self, arr):
        self.root = None
        self.root = self.insertLevelOrder(arr, self.root, 0, len(arr))

    # Function to insert nodes in level order  
    def insertLevelOrder(self, arr, root, i, n): 
        
        # Base case for recursion  
        if i < n: 
            temp = Node(arr[i])  
            root = temp  
    
            # insert left child  
            root.left = self.insertLevelOrder(arr, root.left, 2 * i + 1, n)  
    
            # insert right child  
            root.right = self.insertLevelOrder(arr, root.right, 2 * i + 2, n) 
        return root
    
    # Function to  print level order traversal of tree 
    def printLevelOrder(self): 
        h = self.height(self.root) 
        for i in range(1, h+1): 
            self.printGivenLevel(self.root, i) 
    
    
    # Print nodes at a given level 
    def printGivenLevel(self, root , level): 
        if root is None: 
            return
        if level == 1: 
            print(root.data) 
        elif level > 1 : 
            self.printGivenLevel(root.left , level-1) 
            self.printGivenLevel(root.right , level-1)
    
    def height(self, node): 
        if node is None: 
            return 0 
        else :
            # Compute the height of each subtree  
            lheight = self.height(node.left) 
            rheight = self.height(node.right) 
    
            #Use the larger one 
            if lheight > rheight : 
                return lheight+1
            else: 
                return rheight+1

# Code execution starts here 
if __name__=='__main__': 
    print('<== START ==>')
    arr = [1, 2, 3, 4, 5, 6]
    print('Data Array', arr)

    print('inserting into/ creating a binary tree from data array')
    btree = BinaryTree(arr)

    # traversing binary tree
    print('trversing a binary tree')
    btree.printLevelOrder()


    print('<== END ==>')