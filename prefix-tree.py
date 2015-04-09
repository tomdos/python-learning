#!/usr/bin/env python3
import sys

class PrefixTree:
    def __init__(self):
        self._root = self.Node()


    def __str__(self):
        return self._root.__str__()


    def add(self, word, description):
        '''
        Add new word to the tree. The last node (representing the word itself) 
        contains description of the word.
        '''
        currentNode = self._root

        for i in range(len(word)):
            nextNode = currentNode.getSiblingByKey(word[i])
            if nextNode == None:
                break;
                
            currentNode = nextNode

        for j in range(i, len(word)):
            node = self.Node(word[j])
            currentNode.addSibling(node)
            currentNode = node
            
        currentNode.setDescription(description)
        
        
    def remove(self, word):
        '''
        Remove the word in this tree. Return True on success and False if the word
        is not in tree.
        '''
        pass
        
        
    def find(self, word):
        '''
        Find the word and return its description or None.
        '''
        
        currentNode = self._root
        for i in range(len(word)):
            currentNode = currentNode.getSiblingByKey(word[i])
            if currentNode == None:
                return None
        
        return currentNode.getDescription()


    def _printTree(self, node, path):
        if node.getValue():
            path = path + node.getValue()

        sys.stdout.write(path + ": ") # root

        for key in node.getAllSiblings():
            sys.stdout.write(key + " ")

        sys.stdout.write("\n")

        for key in node.getAllSiblings():
            sibNode = node.getSiblingByKey(key)
            self._printTree(sibNode, path)


    def printTree(self):
        '''
        Print structure of this tree. Path (prefix of a word) and all 
        silblings of a node are printed for each node.
        '''
        self._printTree(self._root, "")
        
    
    def _printContent(self, node, path):
        if node.getValue():
            path = path + node.getValue()
            
        if node.getDescription():
            print("{} = {}".format(path, node.getDescription()))
            
        for key in node.getAllSiblings():
            newNode = node.getSiblingByKey(key)
            self._printContent(newNode, path)
            
    
    def printContent(self):
        '''
        Print all words with description in this tree.
        '''
        self._printContent(self._root, "")


    class Node:
        '''
        Prefix tree node. Each node has value, description and siblings. The value is 
        single letter from the word. The description describes concrete word. Thus every
        node with defined description is the last node (letter) of the word. The siblings
        is dict where a key is value (letter) of sibling's node and dict's value is node iself.
        '''
        def __init__(self, value = None, description = None):
            self._value = value
            self._description = description
            self._siblings = {}

        def __str__(self):
            return "v: {} s: {}".format(self._value, self._siblings)

        def getValue(self):
            return self._value

        def setValue(self, value):
            self._value = value
            
        def getDescription(self):
            return self._description
            
        def setDescription(self, desc):
            self._description = desc

        def getAllSiblings(self):
            return self._siblings

        def getSiblingByKey(self, key):
            try:
                return self._siblings[key]
            except KeyError:
                return None

        def addSibling(self, node):
            self._siblings[node.getValue()] = node


def main():
    words = (
    'amok',
    'amoks',
    'amole',
    'amoles',
    'among',
    'amongst',
    'amontillado',
    'amontillados',
    'amoral',
    'amorality',
    'amorally',
    'amoretti',
    'amoretto',
    'amorists',
    'amoroso',
    'amorous',
    'amorously',
    'amorousness',
    'amorphous',
    'amorphously',
    'amorphousness',
    )

    tree = PrefixTree()
    for w in words:
        tree.add(w, "This is description of the word: " + w)
        
    #tree.printTree()
    #tree.printContent()
    print("amok: ", tree.find("amok"))
    print("amorphousness: ", tree.find("amorphousness"))
    print("amorphoNotExists: ", tree.find("amorphoNotExists"))


if __name__ == "__main__":
    main()
