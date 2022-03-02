
# Time complexity is O(log n)
import random


def round_down(value, decimals):
    factor = 1 / (10 ** decimals)
    return (value // factor) * factor


def binary_search_recursive(nums, target):
    start_pos = 0
    end_pos = len(nums)
    middle_pos = int((start_pos+end_pos)/2)
    if start_pos >= end_pos:
        return -1
    print(
        f"Now search from {start_pos}---->{middle_pos}--->{end_pos} and mid_element-->{arr[middle_pos]}")
    if nums[middle_pos] == target:
        return middle_pos
    if target > nums[middle_pos]:
        start_pos = middle_pos+1
    elif target < nums[middle_pos]:
        end_pos = middle_pos-1
    return binary_search_recursive(nums[start_pos:end_pos+1], target)


def leet_code(nums, target):
    start_pos = 0
    end_pos = len(nums)-1
    while start_pos <= end_pos:
        middle_pos = int((start_pos+end_pos)//2)
        print(
            f"Now search from {start_pos}---->{middle_pos}--->{end_pos} and mid_element-->{nums[middle_pos]}")
        if nums[middle_pos] == target:
            return middle_pos
        if target > nums[middle_pos]:
            start_pos = middle_pos+1
        elif target < nums[middle_pos]:
            end_pos = middle_pos-1
    return -1


def binary_search(arr, search_element):
    # Sorted Array
    # making the arr to ascending order
    isAsc = True if arr[0] <= arr[len(arr)-1] else False
    start_pos = 0
    end_pos = len(arr)-1
    no_of_comparions = 0
    while start_pos <= end_pos:
        mid_pos = int(round_down((start_pos+end_pos)/2, 0))
        print(
            f"Now search from {start_pos}---->{mid_pos}--->{end_pos} and mid_element-->{arr[mid_pos]}")
        if arr[mid_pos] == search_element:
            print("Found the search element at position:", mid_pos)
            # return the arr[mid_pos] as we found the ans
            break

        if isAsc:
            # If given array is sorted in ascending order
            if search_element < arr[mid_pos]:
                end_pos = mid_pos-1
            else:
                start_pos = mid_pos+1
        else:
            # If the array is sorted in descending order
            if arr[mid_pos] < search_element:
                end_pos = mid_pos-1

            else:
                start_pos = mid_pos+1

        no_of_comparions += 1

    # return -1 if code executes this line it means the element is not found in the array
    print("NO OF COMPARISIONS FOR SEARCHING THE VARIABLE:", no_of_comparions)


if __name__ == '__main__':
    range_of_list = int(input("Enter the maxium Range of List:")) or 10000000
    total_elements = int(input("Enter the total_elements:")) or 5863
    search_element = int(input("Enter the search element:"))
    arr = random.sample(range(range_of_list), total_elements)
    arr.sort(reverse=True)
    binary_search_recursive(arr, search_element)
    print(leet_code([-1, 0, 3, 5, 9, 12], 13))
