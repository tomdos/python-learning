#!/usr/bin/env python3

class TreeNode:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, nodeList):
        self.root = None;
        for value in nodeList:
            self.add(value)
            
    def __add(self, node):
        if self.root == None:
            raise RuntimeError("root element can't be empty")
        
        next = self.root
        
        while next != None:
            prev = next
            if next.value > node.value:
                next = next.left
            else:
                next = next.right
                
        if prev.value > node.value:
            prev.left = node
        else:
            prev.right = node
            

    def add(self, value):
        """ Add new value into tree. """
        node = TreeNode(value)
        if self.root == None:
            self.root = node
        else:
            self.__add(node)
            
    def del(self, value):
        pass
        
    
    def __printTree(self, root):
        if root == None:
            return
        
        self.__printTree(root.left)
        print("{} ".format(root.value))
        self.__printTree(root.right)
        
    
    def printTree(self):
        """ Print tree """
        self.__printTree(self.root)
        
        
    def __getList(self, root, array):
        if root == None:
            return
        
        self.__getList(root.left, array)
        array.append(root.value)
        self.__getList(root.right, array)

    
    def getList(self):
        """ Return tree in a list structure. """
        array = []
        self.__getList(self.root, array)
        return array

        
    def __eq__(self, tree):
        a1 = self.getList()
        a2 = tree.getList()

        return a1 == a2

if __name__ == "__main__":
    v1 = (10,5,6,1,3,4,2,7)
    v2 = (10,5,6,1,3,4,2,7)
    
    tree1 = Tree(v1)
    tree2 = Tree(v2)
    
    tree1.printTree()
    print(tree1 == tree2)
    