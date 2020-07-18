def linear_search(arr, val):
    for idx, elem in enumerate(arr):
        if elem == val:
            return idx
    return None


def main():
    arr = list(range(20))
    val = 5
    print(arr)
    idx = linear_search(arr, val)
    if idx is not None:
        print(f"{val} is in {idx}th index")
    else:
        print(f"{val} is not found")


if __name__ == "__main__":
    main()
