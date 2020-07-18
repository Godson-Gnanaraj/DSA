"""
Insertion Sort
--------------
Traverse through the given array and inserts the
smaller element in order.
"""


def insertion_sort(arr):
    for i in range(len(arr)):
        val = arr[i]
        j = i - 1
        while j > 0 and val < arr[j]:
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
