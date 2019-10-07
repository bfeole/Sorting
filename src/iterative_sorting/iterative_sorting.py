import math
import random

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for k in range(cur_index+1, len(arr)):
            if arr[k] < arr[smallest_index]:
                smallest_index = k
        # TO-DO: swap
        if smallest_index != cur_index:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# Notes / testing

    # if arr[smallest_index] < arr[i]:
    # smallest_index = i
    # arr.insert(smallest_index, arr[i])
    # The second for loops allows to search the elements to the right of the current index.
    # Without this, I don't know if its possible but this also makes it very costly.

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr2 = []
# arr3 = [0, 1, 2, 3, 4, 5]
# arr4 = random.sample(range(200), 50)
# print(selection_sort(arr3))
# print(arr1)


# # TO-DO:  implement the Bubble Sort function below
"""
1. Loop through your array
    - Compare each element to its neighbor
    - If elements in wrong position (relative to each other, swap them)
2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
"""


def bubble_sort(arr):
    # loop through array -1 items times
    for b in range(0, len(arr) - 1):
        # loop through remainder of array - current index ignore last element since it should be in place if rest passing
        for u in range(0, len(arr) - 1 - b):
            # compare neighbor indexes if current index [u] is > than current index + 1 SWAP
            if arr[u] > arr[u+1]:
                arr[u], arr[u+1] = arr[u+1], arr[u]
                # else:
                # break
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
