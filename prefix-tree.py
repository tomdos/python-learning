#!/usr/bin/env python3
import sys

class PrefixTree:
    def __init__(self):
        self._root = self.Node()

    def __str__(self):
        return self._root.__str__()

    def add(self, word):
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

    def _dbgPrint(self, node, str):
        if node.getValue():
            str = str + node.getValue()

        sys.stdout.write(str + ": ") # root

        for key in node.getAllSiblings():
            sys.stdout.write(key + " ")

        sys.stdout.write("\n")

        for key in node.getAllSiblings():
            sibNode = node.getSiblingByKey(key)
            self._dbgPrint(sibNode, str)

    def dbgPrint(self):
        self._dbgPrint(self._root, "")


    class Node:
        def __init__(self, value = None):
            self._value = value
            self._siblings = {}

        def __str__(self):
            return "v: {} s: {}".format(self._value, self._siblings)

        def getValue(self):
            return self._value

        def setValue(self, value):
            self._value = value

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
        tree.add(w)
        
    tree.dbgPrint()


if __name__ == "__main__":
    main()
