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

            
    def delete(self, value):
        pass

    
    def __preorderIteration(self, root):
        pass

        
    def preorderIteration(self, root):
        pass
        
        
    def __preorder(self, root, array = []):
        """ Implementation of preorder. """
        if root == None:
            return array
            
        array.append(root)
        array = self.__preorder(root.left, array)
        array = self.__preorder(root.right, array)
        
        return array
        
        
    def preorder(self):
        """ Return list of preordered nodes. """
        return self.__preorder(self.root)
        
    
    def __inorder(self, root, array = []):
        """ Implementation of inorder - return list of nodes. """
        if root == None:
            return array
            
        array = self.__inorder(root.left, array)
        array.append(root)
        array = self.__inorder(root.right, array)
        
        return array
        
    
    def inorder(self):
        """ Return list of inorder sorted nodes. """
        return self.__inorder(self.root)
        
    
    def printTree(self, type = "inorder"):
        """ Print tree. """
        if type == "inorder":
            arr = self.inorder()
        elif type == "preorder":
            arr = self.preorder()
        elif type == "postorder":
            print ("Not implemented yet.")
            return
        else:
            raise ValueError("Type must be inorder, preorder or postorder.")
        
        for node in arr:
            print(node.value)
        
        
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

        
    #def __eq__(self, tree):
    #    a1 = self.getList()
    #    a2 = tree.getList()
    #
    #    return a1 == a2

if __name__ == "__main__":
    v1 = (10,5,6,1,3,4,2,7)
    v2 = (10,5,6,1,3,4,2,7)
    
    tree1 = Tree(v1)
    tree2 = Tree(v2)
    tree1.printTree(type="inorder")
    
    #print(tree1 == tree2)
    