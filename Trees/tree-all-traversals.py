
import colorama
from colorama import Fore


class Node:
    def __init__(self, value):
        self.value = value
        self.rightNode = None
        self.leftNode = None


def preOrder(treeNode):
    if treeNode.value:
        print(Fore.RED + f'{treeNode.value}')

    if treeNode.leftNode:
        printTree(treeNode.leftNode)

    if treeNode.rightNode:
        printTree(treeNode.rightNode)


def postOrder(treeNode):
    if treeNode.leftNode:
        printTree(treeNode.leftNode)

    if treeNode.rightNode:
        printTree(treeNode.rightNode)

    if treeNode.value:
        print(Fore.GREEN + f'{treeNode.value}')


def inOrder(treeNode):
    if treeNode.leftNode:
        printTree(treeNode.leftNode)
    if treeNode.value:
        print(Fore.WHITE + f'{treeNode.value}')
    if treeNode.rightNode:
        printTree(treeNode.rightNode)


def printTree(treeNode):
    if treeNode.leftNode:
        printTree(treeNode.leftNode)
    if treeNode.rightNode:
        printTree(treeNode.rightNode)
    if treeNode.value:
        print(Fore.MAGENTA + f'{treeNode.value}')


def log(msg):
    print("*******************************")
    print(msg)
    print("*******************************")


if __name__ == '__main__':
    print(Fore.WHITE)
    rootElement = Node(1)
    rootElement.rightNode = Node(2)
    rootElement.leftNode = Node(3)
    rootElement.leftNode.leftNode = Node(4)
    rootElement.leftNode.rightNode = Node(5)
    log("INORDER")
    inOrder(rootElement)
    log("POSTORDER")
    postOrder(rootElement)
    log("PREORDER")
    preOrder(rootElement)
