# BinaryTree class

from BinaryNode import *

class BinaryTree:

    # default constructor
    # makes an empty tree
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    # tests if tree is empty
    def isEmpty(self):
        return self.root == None

    # returns root of tree
    def getRoot(self):
        return self.root
    
    # sets root to newNode 
    def setRoot(self, newNode):
        self.root = newNode

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
        
    def getLeftChild(self):
        return self.left
        
    def getRightChild(self):
        return self.right


            

