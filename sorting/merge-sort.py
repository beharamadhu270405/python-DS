

import random
from icecream import ic
from sympy import re

ic.enable = True


def mergeFinalLists(leftList, rightList):
    finalList = []
    pointer = leftListIndex = rightListIndex = 0
    while(leftListIndex < len(leftList) and rightListIndex < len(rightList)):
        if leftList[leftListIndex] < rightList[rightListIndex]:
            finalList.insert(pointer, leftList[leftListIndex])
            leftListIndex += 1
        else:
            finalList.insert(pointer, rightList[rightListIndex])
            rightListIndex += 1
        pointer += 1
    while leftListIndex < len(leftList):
        finalList.insert(pointer, leftList[leftListIndex])
        leftListIndex += 1
        pointer += 1
    while rightListIndex < len(rightList):
        finalList.insert(pointer, rightList[rightListIndex])
        rightListIndex += 1
        pointer += 1
    ic(leftList, rightList, finalList)
    return finalList


def merge_sort(unsortedList):
    if len(unsortedList) == 1:
        return unsortedList
    midIndex = len(unsortedList)//2
    leftUnsortedList = merge_sort(unsortedList[:midIndex])
    rightUnsortedList = merge_sort(unsortedList[midIndex:])
    ic(leftUnsortedList, rightUnsortedList)
    return ic(mergeFinalLists(leftUnsortedList, rightUnsortedList))


if __name__ == '__main__':
    unsortedList = random.sample(range(100), 10)
    ic(unsortedList)
    merge_sort(unsortedList)
