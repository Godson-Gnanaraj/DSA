def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main():
    arr = [1, 0, 3, 5, 6, 8, 9, 2, 4, 7]
    selection_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
