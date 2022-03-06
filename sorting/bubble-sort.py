def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(1, len(unsorted_list)-i):
            if unsorted_list[j] < unsorted_list[j-1]:
                print("SWAP")
                swap = True
                unsorted_list[j], unsorted_list[j -
                                                1] = unsorted_list[j-1], unsorted_list[j]
            print(i, j, j-1)
        print("***********************************")
    print(unsorted_list)


if __name__ == '__main__':
    unsorted_list = [3, 1, 5, 4, 2]
    bubble_sort(unsorted_list)
