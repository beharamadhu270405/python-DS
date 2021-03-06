"""
A Stack is a Linear Data structure that stores items in LIFO(Last In First Out)manner.
The functions associated with stack are:

empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

"""
from typing import List, Union


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> Union[int, str, float]:
        return self.items.pop()

    def isEmpty(self) -> List:
        return self.items == []

    def peek(self) -> Union[int, str, float]:
        if not self.isEmpty():
            return self.items[-1]
        return None

    def getStack(self) -> List:
        return self.items


if __name__ == '__main__':
    myStack = Stack()
    myStack.push("A")
    myStack.push("2")
    myStack.push("3")
    myStack.push("24")
    print("Stack:", myStack.getStack())
    print("Popping:", myStack.pop())
    print("Stack:", myStack.getStack())
    print("Peeking the Top element in the Stack:", myStack.peek())
    print("Stack:", myStack.getStack())
    print("Checking is Stack empty:", myStack.isEmpty())
