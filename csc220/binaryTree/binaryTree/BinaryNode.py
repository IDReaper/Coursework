# BinaryNode class
# Modified code from Listings 5.5, 5.6, 5.7, 5.8 & 5.12

class BinaryNode:

    # default constructor
    # makes an empty node
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None

    # constructor for nodes
    # assigns initial value to key
    def __init__(self,rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    # return value of current node
    def getRootVal(self):
        return self.key

    # set value of current node 
    def setRootVal(self,obj):
        self.key = obj

    # return root of left subtree of current node
    def getLeftChild(self):
        return self.left

    # insert newNode as left child of current node
    def setLeftChild(self,newNode):
        self.left = newNode

    # return root of right subtree of current node
    def getRightChild(self):
        return self.right

    # insert newNode as right child of current node
    def setRightChild(self,newNode):
        self.right = newNode

    # returns a string from a preorder traversal
    def strPreorder(self):
        print self.key
        if self.left:
            self.left.strPreorder()
        if self.right:
            self.right.strPreorder()

    # returns a string from an inorder traversal
    def strInorder(self):
        if self.left:
            self.left.strInorder()
        print self.key
        if self.right:
            self.right.strInorder()

    # returns a string from a postorder traversal
    def strPostorder(self):
        if self.left:
            self.left.strPostorder()
        if self.right:
            self.right.strPostorder()
        print self.key

