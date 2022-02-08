from icecream import ic
from stack import Stack
from datetime import datetime


def time_format():
    return f'{datetime.now().strftime("%m/%d/%Y, %I:%M:%S")}|> '


ic.configureOutput(prefix=time_format, includeContext=True)


def nextLargestElment(items):
    tempStack = Stack()
    returnStack = Stack()
    tempStack.push(items[0])
    print("Intial tempStack:", tempStack.getStack())
    print("-----------------------------------------")
    for current_item in items[1::]:
        print("current_item:", current_item)
        print("stack_top_item:", tempStack.peek())

        if tempStack.isEmpty() == False:
            stack_top_item = tempStack.pop()
            while stack_top_item < current_item:
                print(str(stack_top_item) + " -- " + str(current_item))
                returnStack.push(current_item)
                if tempStack.isEmpty():
                    break
                stack_top_item = tempStack.pop()
            if stack_top_item > current_item:
                tempStack.push(stack_top_item)
        tempStack.push(current_item)
        print("tempStack:", tempStack.getStack())
        print("-----------------------------------------")
    while tempStack.isEmpty() == False:
        element = tempStack.pop()
        returnStack.push(-1)
        next = -1
        print(str(element) + " -- " + str(next))
    return returnStack.getStack()


if __name__ == '__main__':
    # ic(nextLargestElment([int(item)
    #                       for item in input("Enter the list items : ").strip().split()]))

    ic(nextLargestElment([2, 6, 5, 4, 19]))
