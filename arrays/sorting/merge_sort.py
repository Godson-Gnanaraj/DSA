def merge_sort(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return

    mid = arr_len // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    llen = len(left_arr)
    rlen = len(right_arr)
    lpos = rpos = pos = 0

    while lpos < llen and rpos < rlen:
        if left_arr[lpos] < right_arr[rpos]:
            arr[pos] = left_arr[lpos]
            lpos += 1
        else:
            arr[pos] = right_arr[rpos]
            rpos += 1
        pos += 1

    while lpos < llen:
        arr[pos] = left_arr[lpos]
        lpos += 1
        pos += 1

    while rpos < rlen:
        arr[pos] = right_arr[rpos]
        rpos += 1
        pos += 1


def main():
    arr = [1, 0, 3, 5, 6, 8, 9, 2, 4, 7]
    merge_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
