# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:22:14 2024

@author: gilbe
"""

## HW4

# Problem 1
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
node1 = Node(5)
print("Problem 1:")
print(node1.value)

# Problem 2
class BinaryTree:
    def __init__(self):
        self.root = None
    
    # Code to insert value in the tree
    def insert(self, value):
        # Fill root if NONE
        if self.root == None:
            self.root = Node(value)
            return
        
        #Create refrence value
        ref = self.root
        
        while ref != None:
            if ref.value == value:
                return("duplicate value")
            if ref.value > value:
                if ref.left == None:
                    ref.left = Node(value)
                    return
                ref = ref.left
            if ref.value < value:
                if ref.right == None:
                    ref.right = Node(value)
                    return
                ref = ref.right
                
    def inorder_dfs(self, node):
        if node is not None:
            self.inorder_dfs(node.left)
            print(node.value)
            self.inorder_dfs(node.right)
            
    def bfs(self, node):
        Queue = [node]
        while Queue:
            print(Queue[0].value)
            if Queue[0].left != None:    
                Queue.append(Queue[0].left)
            if Queue[0].right != None:
                Queue.append(Queue[0].right)
            Queue.pop(0)
 
print("\nProblem 3:")
Example = BinaryTree()
Example.insert(10)
Example.insert(5)
Example.insert(3)
Example.insert(7)
Example.insert(15)
Example.insert(12)
Example.insert(18)
Example.inorder_dfs(Example.root)     
                
print("\nProblem 4:")                
Example.bfs(Example.root)
                
                
                
                
                
                
        
        