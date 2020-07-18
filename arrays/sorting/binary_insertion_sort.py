"""
Binary Insertion Sort
--------------
Find the postion in which the element to be inserted
using binary search and do the insert the element.
"""


def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        return start + 1

    if start > end:
        return start

    mid = (start + end) // 2

    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    if arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    return mid


def insertion_sort(arr):
    for i in range(len(arr)):
        val = arr[i]
        j = i - 1
        pos = binary_search(arr, val, 0, j)
        while j >= pos:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val


def main():
    """Driver function"""
    arr = [1, 0, 3, 5, 6, 8, 9, 2, 4, 7]
    insertion_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
