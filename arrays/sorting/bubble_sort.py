def bubble_sort(arr):
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    arr = [1, 0, 3, 5, 6, 8, 9, 2, 4, 7]
    bubble_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
