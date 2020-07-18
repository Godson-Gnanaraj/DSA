def jump_search(arr, val, n):
    start = 0
    end = int(n**0.5)

    while arr[min(end, n) - 1] < val:
        start = end
        end += int(n**0.5)
        if end >= n:
            return None

    for i in range(start, end):
        if arr[i] == val:
            return i
    return None


def main():
    arr = list(range(20))
    val = 5
    print(arr)
    idx = jump_search(arr, val, len(arr))
    if idx is not None:
        print(f"{val} is in {idx}th index")
    else:
        print(f"{val} is not found")


if __name__ == "__main__":
    main()
