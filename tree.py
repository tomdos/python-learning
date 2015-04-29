#!/usr/bin/env python3
import sys

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
        
        
    def __depth(self, node):
        """ Implementation of depth. """
        if node == None:
            return 0
            
        nLeft = self.__depth(node.left)
        nRight = self.__depth(node.right)
        
        return (nLeft + 1) if (nLeft > nRight) else (nRight + 1)
        
        
    def depth(self):
        """ Return maximal depth of the tree. """
        return self.__depth(self.root)        

    
    def __preorderIteration(self, node):
        """ Implementation of preorder using iterative approach instead of recursion. """
        array = []
        stack = []
        
        # visit
        # left
        # right (save)
        while node:
            array.append(node)
    
            if node.right:
                stack.append(node.right)
                
            if node.left:
                node = node.left
            else:
                try:
                    node = stack.pop()
                except:
                    node = None
                    
        return array
        
        
    def preorderIteration(self):
        """ Preorder traversal without recursion. """
        return self.__preorderIteration(self.root)
        
        
    def __inorderIteration(self, node):
        """ Implementation of inorder using iteration. """
        array = []
        stack = []
        
        while len(stack) or node:                        
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                array.append(node)
                node = node.right
            
        return array
    
    
    def inorderIteration(self):
        """ Inorder traversal without recursion. """
        return self.__inorderIteration(self.root)
        
        
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
        elif type == "inorderIter":
            arr = self.inorderIteration()
        elif type == "preorder":
            arr = self.preorder()
        elif type == "preorderIter":
            arr = self.preorderIteration()
        elif type == "postorder":
            print ("Not implemented yet.")
            return
        elif type == "postorderIter":
            print ("Not implemented yet.")
            return
        else:
            raise ValueError
        
        for node in arr:
            sys.stdout.write("{} ".format(node.value))
        sys.stdout.write("\n")
        

        
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
    
    tree1.printTree(type="preorder")
    tree1.printTree(type="preorderIter")
    
    tree1.printTree(type="inorder")
    tree1.printTree(type="inorderIter")
    
    print(tree1.depth())
    
    #print(tree1 == tree2)
    