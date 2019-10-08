# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # TO-DO

    return merged_arr


"""
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled
"""


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # if array has more than one item?
    # if len(arr) == 1:
    #     return arr
    # while len(arr) >= 1:
        # split in half
    half = len(arr) // 2
    sliced = arr[:half]
    arr.append(sliced)
    print(f"sliced: {sliced}")
    # for i in range(0, len(arr)):
    # print(arr[len(arr) / 2:])
    # if len(arr) <= 1:
    #     return arr

    return arr


test_arr = [1, 3, 4, 6, 5, 4, 2]

print(test_arr[:4])
print(merge_sort(test_arr))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
