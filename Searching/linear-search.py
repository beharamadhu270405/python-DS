

# Linear Search in Python
from datetime import datetime
from icecream import ic


def time_format():
    return f'{datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}|> '


ic.configureOutput(prefix=time_format)


def linear_search(arr, target_element):
    if len(arr):
        for index, ele in enumerate(arr):
            if ele == target_element:
                return True, index
    return False, -1


if __name__ == '__main__':
    arr = [2, 4, 0, 1, 9]
    target_element = 1
    search_status, index = linear_search(arr, target_element)
    if not search_status:
        ic("Element not found")
    else:
        ic("Element found at index: ", index)
