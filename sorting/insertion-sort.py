

import random


def insertion_sort(unsortedList):
    for i in range(len(unsortedList)):
        for j in range(i, 0, -1):
            print(
                f'Iteration:{i},Current Element:{unsortedList[j]} previous Element:{unsortedList[j-1]}')
            if(unsortedList[j-1] > unsortedList[j]):
                # SWAP
                unsortedList[j-1], unsortedList[j] = unsortedList[j], unsortedList[j-1]
            else:
                break
        print(unsortedList)
        print("****************************************************************")


if __name__ == '__main__':
    unsortedList = random.sample(range(100), 10)
    insertion_sort(unsortedList)
