def binary_search(arr, val, start, end):
    if start > end:
        return None

    mid = start + (end - start) // 2

    if arr[mid] == val:
        return mid
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    return binary_search(arr, val, start, mid - 1)


def exponential_search(arr, val):
    if arr[0] == val:
        return 0

    n = len(arr)
    pos = 1

    while pos < n and arr[pos] <= val:
        pos *= 2

    return binary_search(arr, val, pos // 2, min(pos, n))


def main():
    arr = list(range(20))
    val = 5
    print(arr)
    idx = exponential_search(arr, val)
    if idx is not None:
        print(f"{val} is in {idx}th index")
    else:
        print(f"{val} is not found")


if __name__ == "__main__":
    main()
