# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # for i in range(len(elements)):
    #     for k in range(0, len(elements)):
    #         if arrA[0] < arrB[0]:
    #             merged_arr[0] =

# How it's working:
# Until arrA and arrB are empty:
# If first element A or B is determined less than:
# Pop judged element and Append to empty array
# Return merged_arr and passed in arrays

    while len(arrA) and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
            # merged_arr[0], arrA[0] = arrA[0], merged_arr[0]
            # merged_arr.push(arrA)
            # merged_arr.pop()
            # arrA.pop(arrA[0])
        elif arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))
            # merged_arr[0] = arrB[0]
            # merged_arr[0], arrB[0] = arrB[0], merged_arr[0]
            # arrB.pop(arrB[0])
        # elif arrA == arrB:
        #     return

    # TO-DO

    return merged_arr + arrA + arrB


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
    # base case
    if len(arr) == 1:
        return arr

    # recursive case
    if len(arr) > 1:
        # split in half
        # new_empty = []

        half = len(arr) // 2

        one_half = arr[:half]
        second_half = arr[half:]

        # arr.append(sliced)
        print(f"first: {one_half}")
        print(f"second: {second_half}")

        first_result = merge_sort(one_half)
        second_result = merge_sort(second_half)
        arr = merge(first_result, second_result)

        # new_empty.append(one_half)
        # new_empty.append(second_half)

        # merge_sort(new_empty)
        # arr.append(new_empty)
    # for i in range(0, len(arr)):
    # print(arr[len(arr) / 2:])
    # if len(arr) <= 1:
    #     return arr

    return arr


test_arr = [1, 3, 4, 6, 5, 7, 2, 8]

# print(test_arr)
print(merge_sort(test_arr))
# print(f"one half outside: {one_half}")


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
