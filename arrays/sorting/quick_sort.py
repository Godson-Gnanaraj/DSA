"""
Quick Sort
----------
Takes first element or last element or median element as pivot.
Traverse through the given array and sort it according to the pivot
and sort it again until sub array becomes empty.
"""


def quick_sort(arr, left, right):
    if left >= right:
        return

    pos = left - 1
    for i in range(left, right):
        if arr[i] <= arr[left]:
            pos += 1
            arr[i], arr[pos] = arr[pos], arr[i]

    arr[pos], arr[left] = arr[left], arr[pos]
    quick_sort(arr, left, pos - 1)
    quick_sort(arr, pos + 1, right)


def main():
    """Driver function"""
    arr = [1, 0, 3, 5, 6, 8, 9, 2, 4, 7]
    quick_sort(arr, 0, len(arr))
    print(arr)


if __name__ == "__main__":
    main()
