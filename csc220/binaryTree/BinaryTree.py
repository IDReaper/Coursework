# BinaryTree class

from BinaryNode import *

class BinaryTree:

    # default constructor
    # makes an empty tree
    def __init__(self):
        self.root = None

    # tests if tree is empty
    def isEmpty(self):
        return self.root == None

    # returns root of tree
    def getRoot(self):
        return self.root

    # sets root to newNode 
    def setRoot(self, newNode):
        self.root = newNode

