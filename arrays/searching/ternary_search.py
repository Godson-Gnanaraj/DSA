def ternary_search(arr, val, start, end):
    if start > end:
        return None
    mid1 = start + (end - start) // 3
    mid2 = mid1 + (end - start) // 3
    if arr[mid1] == val:
        return mid1
    if arr[mid2] == val:
        return mid2
    if arr[mid1] < val:
        return ternary_search(arr, val, start, mid1 - 1)
    if arr[mid2] > val:
        return ternary_search(arr, val, mid2 + 1, end)
    return ternary_search(arr, val, mid1 + 1, mid2 - 1)


def main():
    arr = list(range(20))
    val = 5
    print(arr)
    idx = ternary_search(arr, val, 0, len(arr))
    if idx is not None:
        print(f"{val} is in {idx}th index")
    else:
        print(f"{val} is not found")


if __name__ == "__main__":
    main()
