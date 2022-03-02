
# Time complexity is O(log n)

def binary_search():
    # Sorted Array
    arr = [int(no) for no in range(10000)]
    search_element = 567
    start_pos = 0
    end_pos = len(arr)-1
    no_of_comparions = 0
    while start_pos <= end_pos:
        mid_pos = (start_pos+end_pos)//2
        if arr[mid_pos] == search_element:
            print("Found the search element at position:", mid_pos)
            break
        elif arr[mid_pos] < search_element:
            start_pos = mid_pos+1
        else:
            end_pos = mid_pos-1
        no_of_comparions += 1
        print(f"Now search from {start_pos}---->{end_pos}")
    print("NO OF COMPARISIONS FOR SEARCHING THE VARIABLE:", no_of_comparions)


if __name__ == '__main__':
    binary_search()
