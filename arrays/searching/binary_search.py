def binary_search(arr, val, start, end):
    if start > end:
        return None

    mid = start + (end - start) // 2

    if arr[mid] == val:
        return mid
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    return binary_search(arr, val, start, mid - 1)


def main():
    arr = list(range(20))
    val = 5
    print(arr)
    idx = binary_search(arr, val, 0, len(arr))
    if idx is not None:
        print(f"{val} is in {idx}th index")
    else:
        print(f"{val} is not found")


if __name__ == "__main__":
    main()
