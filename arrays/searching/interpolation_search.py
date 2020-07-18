def interpolation_search(arr, val, start, end):
    if start > end or val < arr[start] or val > arr[end]:
        return None

    pos = start + ((end - start) // (arr[end] - arr[start]) *
                   (val - arr[start]))

    if arr[pos] == val:
        return pos
    if arr[pos] < val:
        return interpolation_search(arr, val, pos + 1, end)
    return interpolation_search(arr, val, start, pos - 1)


def main():
    arr = list(range(20))
    val = 5
    print(arr)
    idx = interpolation_search(arr, val, 0, len(arr) - 1)
    if idx is not None:
        print(f"{val} is in {idx}th index")
    else:
        print(f"{val} is not found")


if __name__ == "__main__":
    main()
