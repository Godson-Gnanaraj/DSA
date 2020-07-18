"""
Bubble Sort
-----------
Traverse through array and swaps the adjacent element if its
smaller than the current element
"""


def bubble_sort(arr):
    """Sort the given array using bubble sort alogrithm"""
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    """Driver function"""
    arr = [1, 0, 3, 5, 6, 8, 9, 2, 4, 7]
    bubble_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
