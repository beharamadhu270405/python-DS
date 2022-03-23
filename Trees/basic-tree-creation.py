class Node:
    def __init__(self, value):
        self.leftNode = None
        self.rightNode = None
        self.value = value


def printTree(treeNode):
    if treeNode:
        print(treeNode.value)
        if treeNode.rightNode:
            printTree(treeNode.rightNode)
        if treeNode.leftNode:
            printTree(treeNode.leftNode)


if __name__ == '__main__':
    rootNode = Node(5)
    rootNode.leftNode = Node(1)
    rootNode.rightNode = Node(6)
    printTree(rootNode)
