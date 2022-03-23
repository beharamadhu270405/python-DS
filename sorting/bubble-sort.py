def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(1, len(unsorted_list)-i):
            print(f'Iteration:{i},Current Index:{j} previous Index:{j-1}')
            if unsorted_list[j] < unsorted_list[j-1]:
                print("Bubble Sort Condition SWAPPING DONE")
                unsorted_list[j], unsorted_list[j -
                                                1] = unsorted_list[j-1], unsorted_list[j]

        print(unsorted_list)
        print("***********************************")
    print(unsorted_list)


if __name__ == '__main__':
    unsorted_list = [3, 1, 5, 4, 2]
    bubble_sort(unsorted_list)
