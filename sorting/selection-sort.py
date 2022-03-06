def selection_sort(unsortedList):
    for i in range(len(unsortedList)):
        lastIndex = len(unsortedList)-i
        maxIndex = get_max_index(unsortedList, 0, lastIndex)
        unsortedList[lastIndex -
                     1], unsortedList[maxIndex] = unsortedList[maxIndex], unsortedList[lastIndex-1]
    print(unsortedList)


def get_max_index(arr, startIndex, lastIndex):
    maxIndex = startIndex
    for i in range(startIndex, lastIndex):
        if(arr[i] > arr[maxIndex]):
            maxIndex = i
    print("********************************")
    print(arr)
    print(startIndex, lastIndex, maxIndex)
    print("********************************")
    return maxIndex


if __name__ == '__main__':
    unsortedList = [3, 1, 5, 4, 2]
    selection_sort(unsortedList)
