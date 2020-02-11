def insertion_Sort(arr):
    arrlen = len(arr)

    for i in range(1, arrlen):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j-1
    return arr
